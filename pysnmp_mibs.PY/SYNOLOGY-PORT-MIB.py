#
# PySNMP MIB module SYNOLOGY-PORT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file://./SYNOLOGY-PORT-MIB.txt
# Produced by pysmi-1.1.11 at Wed Jan 10 17:46:14 2024
# On host pablo-VBox platform Linux version 6.2.0-39-generic by user pablo
# Using Python version 3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
IpAddress, Counter64, MibIdentifier, Integer32, enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ObjectIdentity, Counter32, Gauge32, Unsigned32, TimeTicks, NotificationType, Bits, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Counter64", "MibIdentifier", "Integer32", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ObjectIdentity", "Counter32", "Gauge32", "Unsigned32", "TimeTicks", "NotificationType", "Bits", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
synoEthPort = ModuleIdentity((1, 3, 6, 1, 4, 1, 6574, 109))
synoEthPort.setRevisions(('2020-12-20 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: synoEthPort.setRevisionsDescriptions(('Initial version.',))
if mibBuilder.loadTexts: synoEthPort.setLastUpdated('202012200000Z')
if mibBuilder.loadTexts: synoEthPort.setOrganization('www.synology.com')
if mibBuilder.loadTexts: synoEthPort.setContactInfo('Synology Inc. Email: snmp@synology.com')
if mibBuilder.loadTexts: synoEthPort.setDescription('The MIB module describes Ethernet port status.')
synology = MibIdentifier((1, 3, 6, 1, 4, 1, 6574))
ethPortTable = MibTable((1, 3, 6, 1, 4, 1, 6574, 109, 1), )
if mibBuilder.loadTexts: ethPortTable.setStatus('current')
if mibBuilder.loadTexts: ethPortTable.setDescription('A list of Ethernet port entries.')
ethPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6574, 109, 1, 1), ).setIndexNames((0, "SYNOLOGY-PORT-MIB", "ethPortIndex"))
if mibBuilder.loadTexts: ethPortEntry.setStatus('current')
if mibBuilder.loadTexts: ethPortEntry.setDescription('An entry containing management information of an Ethernet port')
ethPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 109, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: ethPortIndex.setStatus('current')
if mibBuilder.loadTexts: ethPortIndex.setDescription('A unique value for each Ethernet port present on the device.')
ethPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 109, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("up", 2), ("down", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethPortStatus.setStatus('current')
if mibBuilder.loadTexts: ethPortStatus.setDescription('The port status of the Ethernet port.')
ethPortSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 109, 1, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethPortSpeed.setStatus('current')
if mibBuilder.loadTexts: ethPortSpeed.setDescription('An estimated of the Ethernet port link speed in units of 1,000,000 bits per second.')
ethPortConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6574, 109, 2))
ethPortCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6574, 109, 2, 1))
ethPortGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6574, 109, 2, 2))
ethPortCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6574, 109, 2, 1, 1)).setObjects(("SYNOLOGY-PORT-MIB", "ethPortGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ethPortCompliance = ethPortCompliance.setStatus('current')
if mibBuilder.loadTexts: ethPortCompliance.setDescription('The compliance statement for synoEthPort entities which implement the SYNOLOGY PORT MIB.')
ethPortGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6574, 109, 2, 2, 1)).setObjects(("SYNOLOGY-PORT-MIB", "ethPortStatus"), ("SYNOLOGY-PORT-MIB", "ethPortSpeed"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ethPortGroup = ethPortGroup.setStatus('current')
if mibBuilder.loadTexts: ethPortGroup.setDescription('The Ethernet port attribute group.')
mibBuilder.exportSymbols("SYNOLOGY-PORT-MIB", synoEthPort=synoEthPort, ethPortCompliances=ethPortCompliances, ethPortSpeed=ethPortSpeed, ethPortIndex=ethPortIndex, ethPortGroups=ethPortGroups, ethPortCompliance=ethPortCompliance, synology=synology, PYSNMP_MODULE_ID=synoEthPort, ethPortStatus=ethPortStatus, ethPortTable=ethPortTable, ethPortGroup=ethPortGroup, ethPortEntry=ethPortEntry, ethPortConformance=ethPortConformance)
