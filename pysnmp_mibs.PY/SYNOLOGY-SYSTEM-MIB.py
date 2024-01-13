#
# PySNMP MIB module SYNOLOGY-SYSTEM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file://./SYNOLOGY-SYSTEM-MIB.txt
# Produced by pysmi-1.1.11 at Wed Jan 10 17:46:50 2024
# On host pablo-VBox platform Linux version 6.2.0-39-generic by user pablo
# Using Python version 3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Counter64, NotificationType, enterprises, Gauge32, Unsigned32, IpAddress, iso, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, ObjectIdentity, Bits, Counter32, MibIdentifier, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "NotificationType", "enterprises", "Gauge32", "Unsigned32", "IpAddress", "iso", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "ObjectIdentity", "Bits", "Counter32", "MibIdentifier", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
synoSystem = ModuleIdentity((1, 3, 6, 1, 4, 1, 6574, 1))
synoSystem.setRevisions(('2013-09-11 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: synoSystem.setRevisionsDescriptions(('Second draft.',))
if mibBuilder.loadTexts: synoSystem.setLastUpdated('201309110000Z')
if mibBuilder.loadTexts: synoSystem.setOrganization('www.synology.com')
if mibBuilder.loadTexts: synoSystem.setContactInfo('Synology Inc. Email: snmp@synology.com')
if mibBuilder.loadTexts: synoSystem.setDescription('Characteristics of the system information')
synology = MibIdentifier((1, 3, 6, 1, 4, 1, 6574))
systemStatus = MibScalar((1, 3, 6, 1, 4, 1, 6574, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemStatus.setStatus('current')
if mibBuilder.loadTexts: systemStatus.setDescription('Synology system status Each meanings of status represented describe below. Normal(1): System functionals normally. Failed(2): Volume has crashed. ')
temperature = MibScalar((1, 3, 6, 1, 4, 1, 6574, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: temperature.setStatus('current')
if mibBuilder.loadTexts: temperature.setDescription('Synology system temperature The temperature of Disk Station uses Celsius degree. ')
powerStatus = MibScalar((1, 3, 6, 1, 4, 1, 6574, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: powerStatus.setStatus('current')
if mibBuilder.loadTexts: powerStatus.setDescription('Synology power status Each meanings of status represented describe below. Normal(1): All power supplies functional normally. Failed(2): One of power supply has failed. ')
fan = MibIdentifier((1, 3, 6, 1, 4, 1, 6574, 1, 4))
systemFanStatus = MibScalar((1, 3, 6, 1, 4, 1, 6574, 1, 4, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemFanStatus.setStatus('current')
if mibBuilder.loadTexts: systemFanStatus.setDescription('Synology system fan status Each meanings of status represented describe below. Normal(1): All Internal fans functional normally. Failed(2): One of internal fan stopped. ')
cpuFanStatus = MibScalar((1, 3, 6, 1, 4, 1, 6574, 1, 4, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpuFanStatus.setStatus('current')
if mibBuilder.loadTexts: cpuFanStatus.setDescription('Synology cpu fan status Each meanings of status represented describe below. Normal(1): All CPU fans functional normally. Failed(2): One of CPU fan stopped. ')
dsmInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 6574, 1, 5))
modelName = MibScalar((1, 3, 6, 1, 4, 1, 6574, 1, 5, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: modelName.setStatus('current')
if mibBuilder.loadTexts: modelName.setDescription('The Model name of this NAS')
serialNumber = MibScalar((1, 3, 6, 1, 4, 1, 6574, 1, 5, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: serialNumber.setStatus('current')
if mibBuilder.loadTexts: serialNumber.setDescription('The serial number of this NAS')
version = MibScalar((1, 3, 6, 1, 4, 1, 6574, 1, 5, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: version.setStatus('current')
if mibBuilder.loadTexts: version.setDescription('The version of this DSM')
upgradeAvailable = MibScalar((1, 3, 6, 1, 4, 1, 6574, 1, 5, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 5))).setMaxAccess("readonly")
if mibBuilder.loadTexts: upgradeAvailable.setStatus('current')
if mibBuilder.loadTexts: upgradeAvailable.setDescription('This oid is for checking whether there is a latest DSM can be upgraded. Available(1): There is version ready for download. Unavailable(2): The DSM is latest version. Connecting(3): Checking for the latest DSM. Disconnected(4): Failed to connect to server. Others(5): If DSM is upgrading or downloading, the status will show others.')
controllerNumber = MibScalar((1, 3, 6, 1, 4, 1, 6574, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: controllerNumber.setStatus('current')
if mibBuilder.loadTexts: controllerNumber.setDescription('Synology system controller number Controller A(0) Controller B(1) ')
systemConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6574, 1, 7))
systemCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6574, 1, 7, 1))
systemGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6574, 1, 7, 2))
systemCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6574, 1, 7, 1, 1)).setObjects(("SYNOLOGY-SYSTEM-MIB", "systemGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    systemCompliance = systemCompliance.setStatus('current')
if mibBuilder.loadTexts: systemCompliance.setDescription('The compliance statement for synoSystem entities which implement the SYNOLOGY SYSTEM MIB.')
systemGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6574, 1, 7, 2, 1)).setObjects(("SYNOLOGY-SYSTEM-MIB", "systemStatus"), ("SYNOLOGY-SYSTEM-MIB", "temperature"), ("SYNOLOGY-SYSTEM-MIB", "powerStatus"), ("SYNOLOGY-SYSTEM-MIB", "systemFanStatus"), ("SYNOLOGY-SYSTEM-MIB", "cpuFanStatus"), ("SYNOLOGY-SYSTEM-MIB", "modelName"), ("SYNOLOGY-SYSTEM-MIB", "serialNumber"), ("SYNOLOGY-SYSTEM-MIB", "version"), ("SYNOLOGY-SYSTEM-MIB", "upgradeAvailable"), ("SYNOLOGY-SYSTEM-MIB", "controllerNumber"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    systemGroup = systemGroup.setStatus('current')
if mibBuilder.loadTexts: systemGroup.setDescription('A collection of objects providing basic information of an synology system entity.')
mibBuilder.exportSymbols("SYNOLOGY-SYSTEM-MIB", systemCompliance=systemCompliance, fan=fan, systemCompliances=systemCompliances, cpuFanStatus=cpuFanStatus, dsmInfo=dsmInfo, systemStatus=systemStatus, upgradeAvailable=upgradeAvailable, systemGroup=systemGroup, serialNumber=serialNumber, powerStatus=powerStatus, temperature=temperature, version=version, controllerNumber=controllerNumber, PYSNMP_MODULE_ID=synoSystem, synology=synology, modelName=modelName, systemConformance=systemConformance, synoSystem=synoSystem, systemGroups=systemGroups, systemFanStatus=systemFanStatus)
