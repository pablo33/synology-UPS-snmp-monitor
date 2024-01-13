#
# PySNMP MIB module SYNOLOGY-GPUINFO-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file://./SYNOLOGY-GPUINFO-MIB.txt
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
gpuInfo = ModuleIdentity((1, 3, 6, 1, 4, 1, 6574, 108))
gpuInfo.setRevisions(('2018-12-03 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: gpuInfo.setRevisionsDescriptions(('First draft.',))
if mibBuilder.loadTexts: gpuInfo.setLastUpdated('201812030000Z')
if mibBuilder.loadTexts: gpuInfo.setOrganization('www.synology.com')
if mibBuilder.loadTexts: gpuInfo.setContactInfo('Synology Inc. Email: snmp@synology.com')
if mibBuilder.loadTexts: gpuInfo.setDescription('Characteristics of the gpu information')
synology = MibIdentifier((1, 3, 6, 1, 4, 1, 6574))
gpuInfoSupported = MibScalar((1, 3, 6, 1, 4, 1, 6574, 108, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gpuInfoSupported.setStatus('current')
if mibBuilder.loadTexts: gpuInfoSupported.setDescription('Synology gpu Supported.')
gpuUtilization = MibScalar((1, 3, 6, 1, 4, 1, 6574, 108, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gpuUtilization.setStatus('current')
if mibBuilder.loadTexts: gpuUtilization.setDescription('Synology gpu utilization %.')
gpuMemoryUtilization = MibScalar((1, 3, 6, 1, 4, 1, 6574, 108, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gpuMemoryUtilization.setStatus('current')
if mibBuilder.loadTexts: gpuMemoryUtilization.setDescription('Synology gpu memory utilization %.')
gpuMemoryFree = MibScalar((1, 3, 6, 1, 4, 1, 6574, 108, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gpuMemoryFree.setStatus('current')
if mibBuilder.loadTexts: gpuMemoryFree.setDescription('Synology gpu free memory in kB.')
gpuMemoryUsed = MibScalar((1, 3, 6, 1, 4, 1, 6574, 108, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gpuMemoryUsed.setStatus('current')
if mibBuilder.loadTexts: gpuMemoryUsed.setDescription('Synology gpu used memory in kB.')
gpuMemoryTotal = MibScalar((1, 3, 6, 1, 4, 1, 6574, 108, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gpuMemoryTotal.setStatus('current')
if mibBuilder.loadTexts: gpuMemoryTotal.setDescription('Synology gpu total memory in kB.')
gpuInfoConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6574, 108, 7))
gpuInfoCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6574, 108, 7, 1))
gpuInfoGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6574, 108, 7, 2))
gpuInfoCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6574, 108, 7, 1, 1)).setObjects(("SYNOLOGY-GPUINFO-MIB", "gpuInfoGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    gpuInfoCompliance = gpuInfoCompliance.setStatus('current')
if mibBuilder.loadTexts: gpuInfoCompliance.setDescription('The compliance statement for syno gpuInfo which implement the SYNOLOGY GPUINFO MIB.')
gpuInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6574, 108, 7, 2, 1)).setObjects(("SYNOLOGY-GPUINFO-MIB", "gpuInfoSupported"), ("SYNOLOGY-GPUINFO-MIB", "gpuUtilization"), ("SYNOLOGY-GPUINFO-MIB", "gpuMemoryUtilization"), ("SYNOLOGY-GPUINFO-MIB", "gpuMemoryFree"), ("SYNOLOGY-GPUINFO-MIB", "gpuMemoryUsed"), ("SYNOLOGY-GPUINFO-MIB", "gpuMemoryTotal"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    gpuInfoGroup = gpuInfoGroup.setStatus('current')
if mibBuilder.loadTexts: gpuInfoGroup.setDescription("A collection of objects providing basic information of a synology gpu. If platform doesn't support gpu, it will get 0 for every oids.")
mibBuilder.exportSymbols("SYNOLOGY-GPUINFO-MIB", PYSNMP_MODULE_ID=gpuInfo, gpuMemoryUsed=gpuMemoryUsed, gpuInfo=gpuInfo, gpuInfoConformance=gpuInfoConformance, synology=synology, gpuMemoryFree=gpuMemoryFree, gpuInfoGroups=gpuInfoGroups, gpuInfoSupported=gpuInfoSupported, gpuMemoryUtilization=gpuMemoryUtilization, gpuMemoryTotal=gpuMemoryTotal, gpuInfoCompliances=gpuInfoCompliances, gpuInfoGroup=gpuInfoGroup, gpuInfoCompliance=gpuInfoCompliance, gpuUtilization=gpuUtilization)
