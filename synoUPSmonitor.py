#!/usr/bin/python3
__author__ 	= "pablo33"
__version__	= "1.0"

import settings
import time
import os
from pysnmp.hlapi import *


""" 
User config data:
Put this lines in a config.ini file besides your script

	hostIP = "10.218.1.20"		# Your NAS IP on the lan. The nas is from where you fetch the UPS information.
	snmpComunity = "sparrow"	# Your SNMP comunity por snmp v1/v2. You have to configure it at your NAS device.
	exTonBm		= 50*60			# Expected time for the UPS to run in batery mode until it empties.
	shutdowntime	= 60		# Expected time the system needs to do a normal shutdown.
"""

class Connection ():
	def __init__ (self, name):
		self.name = name
		self.hostIP = None
		self.snmpComunity = None
		self.exTonBm = None					# Expected time to run on battery mode
		self.shutdowntime = None			# Time to perform a shutdown

		self.status				= None		# Known Values:	 'OL'	'OL CHRG'	'OB DISCHRG'	'OB DISCHRG LB'  # Synology shoots down at status 'OB DISCHRG LB'
		self.maxcharge			= 0			# (snmp float) Max charge, value retrieved from snmp 'BatteryChargeValue' when self.status is 'OL'	4.488648099260006e+16  (100% of battery)
		self.charge				= 0			# (snmp float) Level of battery
		self.warningcharge		= 0			# (snmp float) Value reached for warning alarm  'BatteryChargeWarning'	:  4.488648097320141e+16  (20% of battery)
		self.nextsafeiter		= 30		# seconds to perform next iteration

		self.hostIsReachable 	= None		# True / False / None
		self.hostLastContact 	= None		# None: if never had been contacted since fresh start / System Datetime of last contact.
		self.LifeLevel	= None		# Percent of life running in battery mode.



	## Decorators
	def needinitialized (fx):
		def decorator (*args, **kw_args):
			self = args[0]
			if self.is_iniatilized:
				return fx(*args, **kw_args)
			else:
				print ("This instance is not initilized, please give some connection data")
		return decorator
	 
	@needinitialized
	def getdata (self, targetdata):
		""" Tries to contact the host and get data.
			targetdata is a tuple with: mibname, valuename and expected format for returned data
			"""
		mibname, valuename, formatdata = targetdata
		port = 161							# default port for snmp comunication

		iterator = getCmd(
				SnmpEngine(),
				CommunityData(self.snmpComunity),
				UdpTransportTarget((self.hostIP, port)),
				ContextData(),
				ObjectType (ObjectIdentity(mibname, valuename, 0).addMibSource('./pysnmp_mibs.PY'))
				)
		
		errorIndication, errorStatus, errorIndex, varBinds = next(iterator)

		if errorIndication:
			print(errorIndication)

		elif errorStatus:
			print('%s at %s' % (errorStatus,
								errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))

		else:
			for varBind in varBinds:
				id,value = [x.strip() for x in str(varBind).split("=")]
				if formatdata == 'Float':
					value = float.fromhex(value)
					#value = round(((value/1000000000-44886480)*8000-7840.800488)/100, 2)
				self.hostIsReachable = True
				return id,value
		
		self.hostIsReachable = False
		return None, None

	@needinitialized
	def updatevalues (self):
		""" Update values retrieved from snmp """
		## updating Status and max charge value
		id, status = Con.getdata(datadict['InfoStatus'])
		if id != None:
			self.status = status
			id, value = Con.getdata(datadict['BatteryChargeValue'])
			if id != None:
				self.charge = value
				if self.status == 'OL' or (self.status == 'OL CHRG' and self.maxcharge < value):
					# Unit is Online or charging, charge is at max or is greater
					self.maxcharge = value

		## updating warning value
		id, value = Con.getdata(datadict['BatteryChargeWarning'])
		if id != None:
			self.warningcharge = value

		## updating charge level
		if self.maxcharge and self.charge and self.warningcharge:
			self.LifeLevel = round((self.charge - self.warningcharge) / (self.maxcharge - self.warningcharge), 2)
		
			## updating minutes to wait next iter
			if self.status == 'OL' or self.status == 'OL CHRG':
				hurry = 2
			else:
				hurry = 5
			self.nextsafeiter = int(((self.exTonBm - self.shutdowntime) * self.LifeLevel) / hurry)

			if self.nextsafeiter < 20:
				self.nextsafeiter = 20
		
	def prt_config(self):
		""" Prints 
			"""
		print(
		'Running with this config',
		f'Instance name: {self.name}',
		f'Host IP: {self.hostIP}',
		f'snmpComunity: {self.snmpComunity}',
		f'Expected lifetime on battery mode (seconds): {self.exTonBm}',
		f'Expected time to shutdown the system (seconds): {self.shutdowntime}',
		sep="\n"
		)

	def prt_values(self):
		vars = (
		("hostIsReachable", self.hostIsReachable),
		("status", self.status),
		("maxcharge", self.maxcharge),
		("charge",self.charge),
		("warningcharge", self.warningcharge),
		("nextsafeiter",self.nextsafeiter),
		("LifeLevel", self.LifeLevel),
		)
		print ("======")
		for n,v in vars:
			print (n," = ", v)

	@property
	def is_iniatilized (self):
		""" The clas has been initilized with the data to contact the host
			"""
		return bool(self.hostIP and self.snmpComunity and self.exTonBm and self.shutdowntime)

	@property
	def has_data (self):
		""" The class has contacted with host and has data to self-management
			"""
		return bool(self.is_iniatilized and self.LifeLevel != None)


if __name__ == '__main__':
	Con = Connection(name="NasDS220")
	#1 Reading server config from settings.ini
	Con.hostIP 			= settings.hostIP
	Con.snmpComunity	= settings.snmpComunity
	Con.exTonBm			= settings.exTonBm
	Con.shutdowntime	= settings.shutdowntime

	datadict = {
		'DeviceModel'			: ('SYNOLOGY-UPS-MIB','upsDeviceModel',			 'Sring'),
		'DeviceManufacturer'	: ('SYNOLOGY-UPS-MIB','upsDeviceManufacturer',	 'String'),
		'DeviceSerial'			: ('SYNOLOGY-UPS-MIB','upsDeviceSerial',		 'String'),
		'InfoStatus'			: ('SYNOLOGY-UPS-MIB','upsInfoStatus',			 'String'),
		'InfoMfrDate'			: ('SYNOLOGY-UPS-MIB','upsInfoMfrDate',			 'String'),
		'InfoLoadValue'			: ('SYNOLOGY-UPS-MIB','upsInfoLoadValue',		 'Float'),
		'BatteryChargeValue'	: ('SYNOLOGY-UPS-MIB','upsBatteryChargeValue',	 'Float'),
		'BatteryChargeWarning'	: ('SYNOLOGY-UPS-MIB','upsBatteryChargeWarning', 'Float'),
		'upsBatteryType'		: ('SYNOLOGY-UPS-MIB','upsBatteryType',			 'String'),
		'ethPortStatus'			: ('SYNOLOGY-PORT-MIB','ethPortStatus',			 'Integer'),
	}

	Con.prt_config()

	while True:
		Con.updatevalues()
		if Con.has_data:
			if Con.LifeLevel <= 0:
				break
		Con.prt_values()
		time.sleep(Con.nextsafeiter)

	# perform a Shutdown system
	print ("Performing a shutdown")
	#os.system('shutdown -k +1')
	os.system('shutdown -h now')
