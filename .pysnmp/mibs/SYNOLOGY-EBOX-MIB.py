#
# PySNMP MIB module SYNOLOGY-EBOX-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file://./SYNOLOGY-EBOX-MIB.txt
# Produced by pysmi-1.1.11 at Wed Jan 10 17:45:24 2024
# On host pablo-VBox platform Linux version 6.2.0-39-generic by user pablo
# Using Python version 3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
NotificationType, Unsigned32, Gauge32, Counter64, TimeTicks, MibIdentifier, ModuleIdentity, enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Bits, Counter32, Integer32, ObjectIdentity, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Unsigned32", "Gauge32", "Counter64", "TimeTicks", "MibIdentifier", "ModuleIdentity", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Bits", "Counter32", "Integer32", "ObjectIdentity", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
synologyEbox = ModuleIdentity((1, 3, 6, 1, 4, 1, 6574, 105))
synologyEbox.setRevisions(('2017-06-26 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: synologyEbox.setRevisionsDescriptions(('First draft.',))
if mibBuilder.loadTexts: synologyEbox.setLastUpdated('201706260000Z')
if mibBuilder.loadTexts: synologyEbox.setOrganization('www.synology.com')
if mibBuilder.loadTexts: synologyEbox.setContactInfo('Synology Inc. Email: snmp@synology.com')
if mibBuilder.loadTexts: synologyEbox.setDescription('List ebox info in DS')
synology = MibIdentifier((1, 3, 6, 1, 4, 1, 6574))
eboxTable = MibTable((1, 3, 6, 1, 4, 1, 6574, 105, 1), )
if mibBuilder.loadTexts: eboxTable.setStatus('current')
if mibBuilder.loadTexts: eboxTable.setDescription('Table of ebox data.')
eboxEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6574, 105, 1, 1), ).setIndexNames((0, "SYNOLOGY-EBOX-MIB", "eboxIndex"))
if mibBuilder.loadTexts: eboxEntry.setStatus('current')
if mibBuilder.loadTexts: eboxEntry.setDescription('An entry containing ebox information')
eboxIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 105, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eboxIndex.setStatus('current')
if mibBuilder.loadTexts: eboxIndex.setDescription('Ebox info index')
eboxModel = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 105, 1, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eboxModel.setStatus('current')
if mibBuilder.loadTexts: eboxModel.setDescription('Ebox model')
eboxPower = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 105, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eboxPower.setStatus('current')
if mibBuilder.loadTexts: eboxPower.setDescription('Ebox Power')
eboxRedundantPower = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 105, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eboxRedundantPower.setStatus('current')
if mibBuilder.loadTexts: eboxRedundantPower.setDescription('Ebox Redundant Power')
synologyEboxConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6574, 105, 2))
synologyEboxCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6574, 105, 2, 1))
synologyEboxGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6574, 105, 2, 2))
synologyEboxCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6574, 105, 2, 1, 1)).setObjects(("SYNOLOGY-EBOX-MIB", "synologyEboxGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    synologyEboxCompliance = synologyEboxCompliance.setStatus('current')
if mibBuilder.loadTexts: synologyEboxCompliance.setDescription('The compliance statement for ebox information.')
synologyEboxGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6574, 105, 2, 2, 1)).setObjects(("SYNOLOGY-EBOX-MIB", "eboxIndex"), ("SYNOLOGY-EBOX-MIB", "eboxModel"), ("SYNOLOGY-EBOX-MIB", "eboxPower"), ("SYNOLOGY-EBOX-MIB", "eboxRedundantPower"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    synologyEboxGroup = synologyEboxGroup.setStatus('current')
if mibBuilder.loadTexts: synologyEboxGroup.setDescription('A collection of objects providing basic information of an synology ebox entity.')
mibBuilder.exportSymbols("SYNOLOGY-EBOX-MIB", eboxPower=eboxPower, synologyEboxConformance=synologyEboxConformance, eboxModel=eboxModel, synologyEboxGroups=synologyEboxGroups, synologyEbox=synologyEbox, eboxEntry=eboxEntry, eboxIndex=eboxIndex, synologyEboxCompliance=synologyEboxCompliance, eboxRedundantPower=eboxRedundantPower, synologyEboxGroup=synologyEboxGroup, PYSNMP_MODULE_ID=synologyEbox, synology=synology, synologyEboxCompliances=synologyEboxCompliances, eboxTable=eboxTable)
