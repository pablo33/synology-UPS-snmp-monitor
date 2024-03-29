#
# PySNMP MIB module SYNOLOGY-STORAGEIO-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file://./SYNOLOGY-STORAGEIO-MIB.txt
# Produced by pysmi-1.1.11 at Wed Jan 10 17:46:50 2024
# On host pablo-VBox platform Linux version 6.2.0-39-generic by user pablo
# Using Python version 3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
TimeTicks, Gauge32, NotificationType, enterprises, Unsigned32, IpAddress, iso, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, ObjectIdentity, Bits, Counter32, MibIdentifier, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Gauge32", "NotificationType", "enterprises", "Unsigned32", "IpAddress", "iso", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "ObjectIdentity", "Bits", "Counter32", "MibIdentifier", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
storageIO = ModuleIdentity((1, 3, 6, 1, 4, 1, 6574, 101))
storageIO.setRevisions(('2013-09-11 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: storageIO.setRevisionsDescriptions(('Second draft.',))
if mibBuilder.loadTexts: storageIO.setLastUpdated('201309110000Z')
if mibBuilder.loadTexts: storageIO.setOrganization('www.synology.com')
if mibBuilder.loadTexts: storageIO.setContactInfo('Synology Inc. Email: snmp@synology.com')
if mibBuilder.loadTexts: storageIO.setDescription('Characteristics of the storage io information')
synology = MibIdentifier((1, 3, 6, 1, 4, 1, 6574))
storageIOTable = MibTable((1, 3, 6, 1, 4, 1, 6574, 101, 1), )
if mibBuilder.loadTexts: storageIOTable.setStatus('current')
if mibBuilder.loadTexts: storageIOTable.setDescription('Table of IO devices and how much data they have read/written.')
storageIOEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6574, 101, 1, 1), ).setIndexNames((0, "SYNOLOGY-STORAGEIO-MIB", "storageIOIndex"))
if mibBuilder.loadTexts: storageIOEntry.setStatus('current')
if mibBuilder.loadTexts: storageIOEntry.setDescription('An entry containing a device and its statistics.')
storageIOIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 101, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: storageIOIndex.setStatus('current')
if mibBuilder.loadTexts: storageIOIndex.setDescription('Reference index for each observed device.')
storageIODevice = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 101, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: storageIODevice.setStatus('current')
if mibBuilder.loadTexts: storageIODevice.setDescription('The name of the device we are counting/checking.')
storageIONRead = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 101, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: storageIONRead.setStatus('current')
if mibBuilder.loadTexts: storageIONRead.setDescription('The number of bytes read from this device since boot.')
storageIONWritten = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 101, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: storageIONWritten.setStatus('current')
if mibBuilder.loadTexts: storageIONWritten.setDescription('The number of bytes written to this device since boot.')
storageIOReads = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 101, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: storageIOReads.setStatus('current')
if mibBuilder.loadTexts: storageIOReads.setDescription('The number of read accesses from this device since boot.')
storageIOWrites = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 101, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: storageIOWrites.setStatus('current')
if mibBuilder.loadTexts: storageIOWrites.setDescription('The number of write accesses to this device since boot.')
storageIOLA = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 101, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: storageIOLA.setStatus('current')
if mibBuilder.loadTexts: storageIOLA.setDescription('The load of disk (%)')
storageIOLA1 = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 101, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: storageIOLA1.setStatus('current')
if mibBuilder.loadTexts: storageIOLA1.setDescription('The 1 minute average load of disk (%)')
storageIOLA5 = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 101, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: storageIOLA5.setStatus('current')
if mibBuilder.loadTexts: storageIOLA5.setDescription('The 5 minute average load of disk (%)')
storageIOLA15 = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 101, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: storageIOLA15.setStatus('current')
if mibBuilder.loadTexts: storageIOLA15.setDescription('The 15 minute average load of disk (%)')
storageIONReadX = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 101, 1, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: storageIONReadX.setStatus('current')
if mibBuilder.loadTexts: storageIONReadX.setDescription('The number of bytes read from this device since boot.')
storageIONWrittenX = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 101, 1, 1, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: storageIONWrittenX.setStatus('current')
if mibBuilder.loadTexts: storageIONWrittenX.setDescription('The number of bytes written to this device since boot.')
storageIODeviceSerial = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 101, 1, 1, 14), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: storageIODeviceSerial.setStatus('current')
if mibBuilder.loadTexts: storageIODeviceSerial.setDescription('The name of the device we are counting/checking.')
storageIOConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6574, 101, 2))
storageIOCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6574, 101, 2, 1))
storageIOGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6574, 101, 2, 2))
storageIOCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6574, 101, 2, 1, 1)).setObjects(("SYNOLOGY-STORAGEIO-MIB", "storageIOGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    storageIOCompliance = storageIOCompliance.setStatus('current')
if mibBuilder.loadTexts: storageIOCompliance.setDescription('The compliance statement for storage IO entities which implement the SYNOLOGY STORAGEIO MIB.')
storageIOGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6574, 101, 2, 2, 1)).setObjects(("SYNOLOGY-STORAGEIO-MIB", "storageIODevice"), ("SYNOLOGY-STORAGEIO-MIB", "storageIONRead"), ("SYNOLOGY-STORAGEIO-MIB", "storageIONWritten"), ("SYNOLOGY-STORAGEIO-MIB", "storageIOReads"), ("SYNOLOGY-STORAGEIO-MIB", "storageIOWrites"), ("SYNOLOGY-STORAGEIO-MIB", "storageIOLA"), ("SYNOLOGY-STORAGEIO-MIB", "storageIOLA1"), ("SYNOLOGY-STORAGEIO-MIB", "storageIOLA5"), ("SYNOLOGY-STORAGEIO-MIB", "storageIOLA15"), ("SYNOLOGY-STORAGEIO-MIB", "storageIONReadX"), ("SYNOLOGY-STORAGEIO-MIB", "storageIONWrittenX"), ("SYNOLOGY-STORAGEIO-MIB", "storageIODeviceSerial"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    storageIOGroup = storageIOGroup.setStatus('current')
if mibBuilder.loadTexts: storageIOGroup.setDescription('A collection of objects providing basic information of an synology storage io entity.')
mibBuilder.exportSymbols("SYNOLOGY-STORAGEIO-MIB", storageIOTable=storageIOTable, storageIOEntry=storageIOEntry, storageIOLA15=storageIOLA15, storageIOConformance=storageIOConformance, storageIOIndex=storageIOIndex, storageIOWrites=storageIOWrites, storageIOLA1=storageIOLA1, storageIOGroups=storageIOGroups, storageIOCompliance=storageIOCompliance, storageIONWrittenX=storageIONWrittenX, storageIODeviceSerial=storageIODeviceSerial, storageIONRead=storageIONRead, storageIONWritten=storageIONWritten, storageIOReads=storageIOReads, PYSNMP_MODULE_ID=storageIO, storageIONReadX=storageIONReadX, synology=synology, storageIO=storageIO, storageIODevice=storageIODevice, storageIOLA=storageIOLA, storageIOCompliances=storageIOCompliances, storageIOGroup=storageIOGroup, storageIOLA5=storageIOLA5)
