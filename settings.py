#This is a python file, see the syntaxt

#NAS
hostIP = "192.168.1.33"		# Your NAS IP on the lan. The nas is from where you fetch the UPS information.
snmpComunity = "public"	# Your SNMP comunity por snmp v1/v2. You have to configure it at your NAS device.

#UPS
exTonBm		= 39*60			# Expected time for the UPS to run in batery mode until it empties.

#SYSTEM
shutdowntime	= 60		# Expected time the system needs to do a normal shutdown.
