#
# PySNMP MIB module SYNOLOGY-SERVICES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file://./SYNOLOGY-SERVICES-MIB.txt
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
synologyService = ModuleIdentity((1, 3, 6, 1, 4, 1, 6574, 6))
synologyService.setRevisions(('2016-05-27 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: synologyService.setRevisionsDescriptions(('First draft.',))
if mibBuilder.loadTexts: synologyService.setLastUpdated('201605270000Z')
if mibBuilder.loadTexts: synologyService.setOrganization('www.synology.com')
if mibBuilder.loadTexts: synologyService.setContactInfo('Synology Inc. Email: snmp@synology.com')
if mibBuilder.loadTexts: synologyService.setDescription('List number of users using each service in DS')
synology = MibIdentifier((1, 3, 6, 1, 4, 1, 6574))
serviceTable = MibTable((1, 3, 6, 1, 4, 1, 6574, 6, 1), )
if mibBuilder.loadTexts: serviceTable.setStatus('current')
if mibBuilder.loadTexts: serviceTable.setDescription('Table of Services data.')
serviceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6574, 6, 1, 1), ).setIndexNames((0, "SYNOLOGY-SERVICES-MIB", "serviceInfoIndex"))
if mibBuilder.loadTexts: serviceEntry.setStatus('current')
if mibBuilder.loadTexts: serviceEntry.setDescription('An entry containing Service information')
serviceInfoIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 6, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: serviceInfoIndex.setStatus('current')
if mibBuilder.loadTexts: serviceInfoIndex.setDescription('Service info index')
serviceName = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 6, 1, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: serviceName.setStatus('current')
if mibBuilder.loadTexts: serviceName.setDescription('Service name')
serviceUsers = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 6, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: serviceUsers.setStatus('current')
if mibBuilder.loadTexts: serviceUsers.setDescription('Number of users using this service')
synologyServiceConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6574, 6, 2))
synologyServiceCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6574, 6, 2, 1))
synologyServiceGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6574, 6, 2, 2))
synologyServiceCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6574, 6, 2, 1, 1)).setObjects(("SYNOLOGY-SERVICES-MIB", "synologyServiceGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    synologyServiceCompliance = synologyServiceCompliance.setStatus('current')
if mibBuilder.loadTexts: synologyServiceCompliance.setDescription('The compliance statement for service information.')
synologyServiceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6574, 6, 2, 2, 1)).setObjects(("SYNOLOGY-SERVICES-MIB", "serviceName"), ("SYNOLOGY-SERVICES-MIB", "serviceUsers"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    synologyServiceGroup = synologyServiceGroup.setStatus('current')
if mibBuilder.loadTexts: synologyServiceGroup.setDescription('A collection of objects providing basic information of an synology service entity.')
mibBuilder.exportSymbols("SYNOLOGY-SERVICES-MIB", serviceEntry=serviceEntry, serviceName=serviceName, serviceTable=serviceTable, serviceUsers=serviceUsers, synologyServiceCompliances=synologyServiceCompliances, synologyServiceConformance=synologyServiceConformance, serviceInfoIndex=serviceInfoIndex, synologyServiceGroups=synologyServiceGroups, PYSNMP_MODULE_ID=synologyService, synologyServiceCompliance=synologyServiceCompliance, synologyServiceGroup=synologyServiceGroup, synology=synology, synologyService=synologyService)
