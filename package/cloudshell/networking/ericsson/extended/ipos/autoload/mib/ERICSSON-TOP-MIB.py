#
# PySNMP MIB module ERICSSON-TOP-MIB (http://pysnmp.sf.net)
# ASN.1 source file://C:\MIBS\text_mibs\ERICSSON-TOP-MIB.my
# Produced by pysmi-0.0.6 at Tue Dec 20 11:45:36 2016
# On host ? platform ? version ? by user ?
# Using Python version 2.7.9 (default, Dec 10 2014, 12:24:55) [MSC v.1500 32 bit (Intel)]
#
(Integer, ObjectIdentifier, OctetString,) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier",
                                                                     "OctetString")
(NamedValues,) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
(ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint,
 ValueRangeConstraint,) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint",
                                                   "ConstraintsIntersection", "ValueSizeConstraint",
                                                   "ValueRangeConstraint")
(NotificationGroup, ModuleCompliance,) = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup",
                                                                  "ModuleCompliance")
(Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, IpAddress, TimeTicks,
 Counter64, Unsigned32, enterprises, iso, Gauge32, ModuleIdentity, ObjectIdentity, Bits,
 Counter32,) = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow",
                                        "MibTableColumn", "NotificationType", "MibIdentifier", "IpAddress", "TimeTicks",
                                        "Counter64", "Unsigned32", "enterprises", "iso", "Gauge32", "ModuleIdentity",
                                        "ObjectIdentity", "Bits", "Counter32")
(DisplayString, TextualConvention,) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ericsson = ModuleIdentity((1, 3, 6, 1, 4, 1, 193)).setRevisions(("2008-10-17 00:00", "2002-05-28 00:00",))
ericssonModules = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 183))
mibBuilder.exportSymbols("ERICSSON-TOP-MIB", PYSNMP_MODULE_ID=ericsson, ericssonModules=ericssonModules,
                         ericsson=ericsson)
