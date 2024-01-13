# Description
This is a little script to shoot down a linux system once an UPS is going to run out of battery, and the ups is connected to a synology NAS.



#The problem:
I recently, bought an UPS to enhance my home server and home-land. It is a CyberPower VP700ELCD. The router, one switch, a Synology NAS  DS220+ and a Raspberrypi 3B+ is attached to the UPS.  
The UPS is compatible with Synology systems, and is connected via USB. So when the UPS is going to run out of battery, the Synology-NAS system can detect it and perform a system-shutdown.  
The problem is that the Rasberrypi is not aware of none of that and can't perform a shutdown before the battery runs out.    

#The idea:
Take advantage of snmp capabilities over the Synology NAS and read the UPS status vian SNMP protocol to perform a controlled shutdown on the system.  

#The tools:
PySNMP: is an open source library wich this script relies on.

So here I go again just for fun and to enjoy the trip of coding. I hope this script could help someone with similar needings.  


#DOCs
[https://pysnmp.readthedocs.io/en/latest/
](https://pysnmp.readthedocs.io/en/latest/)  

[https://codigospython.com/monitoreo-de-dispositivos-snmp-con-pysnmp-en-python/](https://codigospython.com/monitoreo-de-dispositivos-snmp-con-pysnmp-en-python/)  

[https://kb.synology.com/es-es/DSM/help/DSM/AdminCenter/system_snmp?version=7
](https://kb.synology.com/es-es/DSM/help/DSM/AdminCenter/system_snmp?version=7
)


#Dependencies:
python3 (This script)
PySNMP
Synology py-compiled MIBs files (bundled with this source code)
Other py-compiled MIBs files (bundled with this source code)

you can install it by tiping on your python environment:  

python3 -m pip install pysnmp
python3 -m pip install pysnmp-pysmi



