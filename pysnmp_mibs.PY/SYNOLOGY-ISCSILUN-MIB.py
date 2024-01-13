#
# PySNMP MIB module SYNOLOGY-ISCSILUN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file://./SYNOLOGY-ISCSILUN-MIB.txt
# Produced by pysmi-1.1.11 at Wed Jan 10 17:45:53 2024
# On host pablo-VBox platform Linux version 6.2.0-39-generic by user pablo
# Using Python version 3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
NotificationType, ModuleIdentity, enterprises, Counter32, MibIdentifier, ObjectIdentity, Unsigned32, Integer32, Counter64, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, iso, Gauge32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "ModuleIdentity", "enterprises", "Counter32", "MibIdentifier", "ObjectIdentity", "Unsigned32", "Integer32", "Counter64", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "iso", "Gauge32", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
synologyiSCSILUN = ModuleIdentity((1, 3, 6, 1, 4, 1, 6574, 104))
synologyiSCSILUN.setRevisions(('2020-08-12 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: synologyiSCSILUN.setRevisionsDescriptions(('New entry iSCSILUNThinProvisionVolFreeMBs',))
if mibBuilder.loadTexts: synologyiSCSILUN.setLastUpdated('202008120000Z')
if mibBuilder.loadTexts: synologyiSCSILUN.setOrganization('www.synology.com')
if mibBuilder.loadTexts: synologyiSCSILUN.setContactInfo('Synology Inc. Email: snmp@synology.com')
if mibBuilder.loadTexts: synologyiSCSILUN.setDescription('Characteristics of the iscsi lun information')
synology = MibIdentifier((1, 3, 6, 1, 4, 1, 6574))
iSCSILUNTable = MibTable((1, 3, 6, 1, 4, 1, 6574, 104, 1), )
if mibBuilder.loadTexts: iSCSILUNTable.setStatus('current')
if mibBuilder.loadTexts: iSCSILUNTable.setDescription('Table of iSCSI LUN data.')
iSCSILUNEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6574, 104, 1, 1), ).setIndexNames((0, "SYNOLOGY-ISCSILUN-MIB", "iSCSILUNInfoIndex"))
if mibBuilder.loadTexts: iSCSILUNEntry.setStatus('current')
if mibBuilder.loadTexts: iSCSILUNEntry.setDescription('An entry containing iscsi lun information')
iSCSILUNInfoIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 104, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: iSCSILUNInfoIndex.setStatus('current')
if mibBuilder.loadTexts: iSCSILUNInfoIndex.setDescription('LUN info index')
iSCSILUNUUID = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 104, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: iSCSILUNUUID.setStatus('current')
if mibBuilder.loadTexts: iSCSILUNUUID.setDescription('LUN uuid')
iSCSILUNName = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 104, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: iSCSILUNName.setStatus('current')
if mibBuilder.loadTexts: iSCSILUNName.setDescription('LUN name')
iSCSILUNThroughputReadHigh = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 104, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iSCSILUNThroughputReadHigh.setStatus('current')
if mibBuilder.loadTexts: iSCSILUNThroughputReadHigh.setDescription('LUN read throughput over 32 bits part')
iSCSILUNThroughputReadLow = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 104, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iSCSILUNThroughputReadLow.setStatus('current')
if mibBuilder.loadTexts: iSCSILUNThroughputReadLow.setDescription('LUN read throughput in unsigned 32 bit')
iSCSILUNThroughputWriteHigh = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 104, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iSCSILUNThroughputWriteHigh.setStatus('current')
if mibBuilder.loadTexts: iSCSILUNThroughputWriteHigh.setDescription('LUN write throughput over 32 bits part')
iSCSILUNThroughputWriteLow = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 104, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iSCSILUNThroughputWriteLow.setStatus('current')
if mibBuilder.loadTexts: iSCSILUNThroughputWriteLow.setDescription('LUN write throughput in unsigned 32 bit')
iSCSILUNIopsRead = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 104, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iSCSILUNIopsRead.setStatus('current')
if mibBuilder.loadTexts: iSCSILUNIopsRead.setDescription('LUN read iops')
iSCSILUNIopsWrite = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 104, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iSCSILUNIopsWrite.setStatus('current')
if mibBuilder.loadTexts: iSCSILUNIopsWrite.setDescription('LUN write iops')
iSCSILUNDiskLatencyRead = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 104, 1, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iSCSILUNDiskLatencyRead.setStatus('current')
if mibBuilder.loadTexts: iSCSILUNDiskLatencyRead.setDescription('LUN disk latency when reading')
iSCSILUNDiskLatencyWrite = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 104, 1, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iSCSILUNDiskLatencyWrite.setStatus('current')
if mibBuilder.loadTexts: iSCSILUNDiskLatencyWrite.setDescription('LUN disk latency when writing')
iSCSILUNNetworkLatencyTx = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 104, 1, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iSCSILUNNetworkLatencyTx.setStatus('current')
if mibBuilder.loadTexts: iSCSILUNNetworkLatencyTx.setDescription('LUN transfer data network latency')
iSCSILUNNetworkLatencyRx = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 104, 1, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iSCSILUNNetworkLatencyRx.setStatus('current')
if mibBuilder.loadTexts: iSCSILUNNetworkLatencyRx.setDescription('LUN receive data network latency')
iSCSILUNIoSizeRead = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 104, 1, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iSCSILUNIoSizeRead.setStatus('current')
if mibBuilder.loadTexts: iSCSILUNIoSizeRead.setDescription('LUN average io size when reading')
iSCSILUNIoSizeWrite = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 104, 1, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iSCSILUNIoSizeWrite.setStatus('current')
if mibBuilder.loadTexts: iSCSILUNIoSizeWrite.setDescription('LUN average io size when writing')
iSCSILUNQueueDepth = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 104, 1, 1, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iSCSILUNQueueDepth.setStatus('current')
if mibBuilder.loadTexts: iSCSILUNQueueDepth.setDescription('Num of iSCSI commands in LUN queue')
iSCSILUNType = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 104, 1, 1, 17), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: iSCSILUNType.setStatus('current')
if mibBuilder.loadTexts: iSCSILUNType.setDescription('LUN type')
iSCSILUNDiskLatencyAvg = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 104, 1, 1, 18), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iSCSILUNDiskLatencyAvg.setStatus('current')
if mibBuilder.loadTexts: iSCSILUNDiskLatencyAvg.setDescription('Average latency of LUN disk')
iSCSILUNThinProvisionVolFreeMBs = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 104, 1, 1, 19), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iSCSILUNThinProvisionVolFreeMBs.setStatus('current')
if mibBuilder.loadTexts: iSCSILUNThinProvisionVolFreeMBs.setDescription("Free space(MB) of thin provisioning lun's volume")
synologyiSCSILUNConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6574, 104, 2))
synologyiSCSILUNCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6574, 104, 2, 1))
synologyiSCSILUNGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6574, 104, 2, 2))
synologyiSCSILUNCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6574, 104, 2, 1, 1)).setObjects(("SYNOLOGY-ISCSILUN-MIB", "synologyiSCSILUNGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    synologyiSCSILUNCompliance = synologyiSCSILUNCompliance.setStatus('current')
if mibBuilder.loadTexts: synologyiSCSILUNCompliance.setDescription('The compliance statement for iSCSI LUN information.')
synologyiSCSILUNGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6574, 104, 2, 2, 1)).setObjects(("SYNOLOGY-ISCSILUN-MIB", "iSCSILUNUUID"), ("SYNOLOGY-ISCSILUN-MIB", "iSCSILUNName"), ("SYNOLOGY-ISCSILUN-MIB", "iSCSILUNThroughputReadHigh"), ("SYNOLOGY-ISCSILUN-MIB", "iSCSILUNThroughputReadLow"), ("SYNOLOGY-ISCSILUN-MIB", "iSCSILUNThroughputWriteHigh"), ("SYNOLOGY-ISCSILUN-MIB", "iSCSILUNThroughputWriteLow"), ("SYNOLOGY-ISCSILUN-MIB", "iSCSILUNIopsRead"), ("SYNOLOGY-ISCSILUN-MIB", "iSCSILUNIopsWrite"), ("SYNOLOGY-ISCSILUN-MIB", "iSCSILUNDiskLatencyRead"), ("SYNOLOGY-ISCSILUN-MIB", "iSCSILUNDiskLatencyWrite"), ("SYNOLOGY-ISCSILUN-MIB", "iSCSILUNNetworkLatencyTx"), ("SYNOLOGY-ISCSILUN-MIB", "iSCSILUNNetworkLatencyRx"), ("SYNOLOGY-ISCSILUN-MIB", "iSCSILUNIoSizeRead"), ("SYNOLOGY-ISCSILUN-MIB", "iSCSILUNIoSizeWrite"), ("SYNOLOGY-ISCSILUN-MIB", "iSCSILUNQueueDepth"), ("SYNOLOGY-ISCSILUN-MIB", "iSCSILUNType"), ("SYNOLOGY-ISCSILUN-MIB", "iSCSILUNDiskLatencyAvg"), ("SYNOLOGY-ISCSILUN-MIB", "iSCSILUNThinProvisionVolFreeMBs"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    synologyiSCSILUNGroup = synologyiSCSILUNGroup.setStatus('current')
if mibBuilder.loadTexts: synologyiSCSILUNGroup.setDescription('A collection of objects providing basic information of an synology iSCSI LUN entity.')
mibBuilder.exportSymbols("SYNOLOGY-ISCSILUN-MIB", synologyiSCSILUNGroup=synologyiSCSILUNGroup, iSCSILUNThroughputReadHigh=iSCSILUNThroughputReadHigh, iSCSILUNThinProvisionVolFreeMBs=iSCSILUNThinProvisionVolFreeMBs, synologyiSCSILUNCompliance=synologyiSCSILUNCompliance, iSCSILUNIoSizeWrite=iSCSILUNIoSizeWrite, iSCSILUNName=iSCSILUNName, iSCSILUNIoSizeRead=iSCSILUNIoSizeRead, iSCSILUNThroughputWriteHigh=iSCSILUNThroughputWriteHigh, synologyiSCSILUNConformance=synologyiSCSILUNConformance, iSCSILUNTable=iSCSILUNTable, iSCSILUNDiskLatencyWrite=iSCSILUNDiskLatencyWrite, iSCSILUNIopsRead=iSCSILUNIopsRead, synologyiSCSILUNGroups=synologyiSCSILUNGroups, iSCSILUNThroughputWriteLow=iSCSILUNThroughputWriteLow, iSCSILUNEntry=iSCSILUNEntry, iSCSILUNThroughputReadLow=iSCSILUNThroughputReadLow, synologyiSCSILUN=synologyiSCSILUN, iSCSILUNDiskLatencyAvg=iSCSILUNDiskLatencyAvg, synologyiSCSILUNCompliances=synologyiSCSILUNCompliances, iSCSILUNUUID=iSCSILUNUUID, iSCSILUNType=iSCSILUNType, iSCSILUNQueueDepth=iSCSILUNQueueDepth, PYSNMP_MODULE_ID=synologyiSCSILUN, iSCSILUNInfoIndex=iSCSILUNInfoIndex, iSCSILUNNetworkLatencyRx=iSCSILUNNetworkLatencyRx, iSCSILUNDiskLatencyRead=iSCSILUNDiskLatencyRead, iSCSILUNNetworkLatencyTx=iSCSILUNNetworkLatencyTx, synology=synology, iSCSILUNIopsWrite=iSCSILUNIopsWrite)
