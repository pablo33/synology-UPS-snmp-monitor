#
# PySNMP MIB module SYNOLOGY-SHA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file://./SYNOLOGY-SHA-MIB.txt
# Produced by pysmi-1.1.11 at Wed Jan 10 17:46:50 2024
# On host pablo-VBox platform Linux version 6.2.0-39-generic by user pablo
# Using Python version 3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Counter64, NotificationType, enterprises, Gauge32, Unsigned32, IpAddress, iso, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, ObjectIdentity, Bits, Counter32, MibIdentifier, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "NotificationType", "enterprises", "Gauge32", "Unsigned32", "IpAddress", "iso", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "ObjectIdentity", "Bits", "Counter32", "MibIdentifier", "TimeTicks")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
synologyHA = ModuleIdentity((1, 3, 6, 1, 4, 1, 6574, 106))
synologyHA.setRevisions(('2018-07-25 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: synologyHA.setRevisionsDescriptions(('First revision',))
if mibBuilder.loadTexts: synologyHA.setLastUpdated('201807250000Z')
if mibBuilder.loadTexts: synologyHA.setOrganization('www.synology.com')
if mibBuilder.loadTexts: synologyHA.setContactInfo('Synology Inc. Email: snmp@synology.com')
if mibBuilder.loadTexts: synologyHA.setDescription('Status of Synology High-Availability')
synology = MibIdentifier((1, 3, 6, 1, 4, 1, 6574))
class HostName(TextualConvention, OctetString):
    description = 'Host name'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 256)

class ClusterStatusType(TextualConvention, Integer32):
    description = 'This TC enumerates cluster status.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("normal", 0), ("warning", 1), ("critical", 2), ("upgrading", 3), ("processing", 4))

class HeartbeatStatusType(TextualConvention, Integer32):
    description = 'This TC enumerates heartbeat status.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("normal", 0), ("abnormal", 1), ("disconnected", 2), ("empty", 3))

activeNodeName = MibScalar((1, 3, 6, 1, 4, 1, 6574, 106, 1), HostName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: activeNodeName.setStatus('current')
if mibBuilder.loadTexts: activeNodeName.setDescription('Hostname of node providing services')
passiveNodeName = MibScalar((1, 3, 6, 1, 4, 1, 6574, 106, 2), HostName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: passiveNodeName.setStatus('current')
if mibBuilder.loadTexts: passiveNodeName.setDescription('Hostname of node not providing services')
clusterAutoFailover = MibScalar((1, 3, 6, 1, 4, 1, 6574, 106, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clusterAutoFailover.setStatus('current')
if mibBuilder.loadTexts: clusterAutoFailover.setDescription('Whether cluster can launch failover')
clusterName = MibScalar((1, 3, 6, 1, 4, 1, 6574, 106, 4), HostName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clusterName.setStatus('current')
if mibBuilder.loadTexts: clusterName.setDescription('Hostname of node providing services')
clusterStatus = MibScalar((1, 3, 6, 1, 4, 1, 6574, 106, 5), ClusterStatusType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clusterStatus.setStatus('current')
if mibBuilder.loadTexts: clusterStatus.setDescription('One of critical, upgrading, processing, warning, normal')
heartbeatStatus = MibScalar((1, 3, 6, 1, 4, 1, 6574, 106, 6), HeartbeatStatusType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: heartbeatStatus.setStatus('current')
if mibBuilder.loadTexts: heartbeatStatus.setDescription('One of empty, disconnected, normal, abnormal')
heartbeatTxRate = MibScalar((1, 3, 6, 1, 4, 1, 6574, 106, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: heartbeatTxRate.setStatus('current')
if mibBuilder.loadTexts: heartbeatTxRate.setDescription('Transfer speed of heartbeat in kilo-byte-per-second')
heartbeatLatency = MibScalar((1, 3, 6, 1, 4, 1, 6574, 106, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: heartbeatLatency.setStatus('current')
if mibBuilder.loadTexts: heartbeatLatency.setDescription('Heartbeat latency in microseconds')
synologyHAConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6574, 106, 9))
synologyHACompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6574, 106, 9, 1))
synologyHAGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6574, 106, 9, 2))
synologyHACompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6574, 106, 9, 1, 1)).setObjects(("SYNOLOGY-SHA-MIB", "synologyHAGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    synologyHACompliance = synologyHACompliance.setStatus('current')
if mibBuilder.loadTexts: synologyHACompliance.setDescription('The compliance statement for SHA information.')
synologyHAGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6574, 106, 9, 2, 1)).setObjects(("SYNOLOGY-SHA-MIB", "activeNodeName"), ("SYNOLOGY-SHA-MIB", "passiveNodeName"), ("SYNOLOGY-SHA-MIB", "clusterAutoFailover"), ("SYNOLOGY-SHA-MIB", "clusterName"), ("SYNOLOGY-SHA-MIB", "clusterStatus"), ("SYNOLOGY-SHA-MIB", "heartbeatStatus"), ("SYNOLOGY-SHA-MIB", "heartbeatTxRate"), ("SYNOLOGY-SHA-MIB", "heartbeatLatency"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    synologyHAGroup = synologyHAGroup.setStatus('current')
if mibBuilder.loadTexts: synologyHAGroup.setDescription('A collection of objects providing basic information of an synology High-availability cluster.')
mibBuilder.exportSymbols("SYNOLOGY-SHA-MIB", ClusterStatusType=ClusterStatusType, passiveNodeName=passiveNodeName, clusterName=clusterName, synologyHACompliances=synologyHACompliances, synologyHAConformance=synologyHAConformance, heartbeatStatus=heartbeatStatus, PYSNMP_MODULE_ID=synologyHA, heartbeatLatency=heartbeatLatency, synologyHACompliance=synologyHACompliance, clusterStatus=clusterStatus, synologyHA=synologyHA, clusterAutoFailover=clusterAutoFailover, HeartbeatStatusType=HeartbeatStatusType, heartbeatTxRate=heartbeatTxRate, synology=synology, synologyHAGroups=synologyHAGroups, HostName=HostName, activeNodeName=activeNodeName, synologyHAGroup=synologyHAGroup)
