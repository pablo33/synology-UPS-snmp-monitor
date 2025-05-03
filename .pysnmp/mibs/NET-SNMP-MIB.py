#
# PySNMP MIB module NET-SNMP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file://./NET-SNMP-MIB.mib
# Produced by pysmi-1.1.11 at Wed Jan 10 17:39:04 2024
# On host pablo-VBox platform Linux version 6.2.0-39-generic by user pablo
# Using Python version 3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, iso, Gauge32, NotificationType, Bits, ObjectIdentity, IpAddress, Integer32, Counter32, ModuleIdentity, enterprises, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "iso", "Gauge32", "NotificationType", "Bits", "ObjectIdentity", "IpAddress", "Integer32", "Counter32", "ModuleIdentity", "enterprises", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
netSnmp = ModuleIdentity((1, 3, 6, 1, 4, 1, 8072))
netSnmp.setRevisions(('2002-01-30 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: netSnmp.setRevisionsDescriptions(('First draft',))
if mibBuilder.loadTexts: netSnmp.setLastUpdated('200201300000Z')
if mibBuilder.loadTexts: netSnmp.setOrganization('www.net-snmp.org')
if mibBuilder.loadTexts: netSnmp.setContactInfo('postal: Wes Hardaker P.O. Box 382 Davis CA 95617 email: net-snmp-coders@lists.sourceforge.net')
if mibBuilder.loadTexts: netSnmp.setDescription('Top-level infrastructure of the Net-SNMP project enterprise MIB tree')
netSnmpObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 1))
netSnmpEnumerations = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 3))
netSnmpModuleIDs = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 3, 1))
netSnmpAgentOIDs = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 3, 2))
netSnmpDomains = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 3, 3))
netSnmpExperimental = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 9999))
netSnmpPlaypen = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 9999, 9999))
netSnmpNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 4))
netSnmpNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 4, 0))
netSnmpNotificationObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 4, 1))
netSnmpConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 5))
netSnmpCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 5, 1))
netSnmpGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 5, 2))
mibBuilder.exportSymbols("NET-SNMP-MIB", PYSNMP_MODULE_ID=netSnmp, netSnmpEnumerations=netSnmpEnumerations, netSnmpAgentOIDs=netSnmpAgentOIDs, netSnmpNotificationObjects=netSnmpNotificationObjects, netSnmpPlaypen=netSnmpPlaypen, netSnmpNotificationPrefix=netSnmpNotificationPrefix, netSnmpModuleIDs=netSnmpModuleIDs, netSnmpExperimental=netSnmpExperimental, netSnmpDomains=netSnmpDomains, netSnmpObjects=netSnmpObjects, netSnmpNotifications=netSnmpNotifications, netSnmpGroups=netSnmpGroups, netSnmpConformance=netSnmpConformance, netSnmp=netSnmp, netSnmpCompliances=netSnmpCompliances)
