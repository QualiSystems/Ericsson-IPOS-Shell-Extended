#
# PySNMP MIB module ERICSSON-ROUTER-PRODUCT-MIB (http://pysnmp.sf.net)
# ASN.1 source file://C:\MIBS\text_mibs\ERICSSON-ROUTER-PRODUCT-MIB.my
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
(eriRouterProducts, eriRouterEntities, eriRouterModules,) = mibBuilder.importSymbols("ERICSSON-ROUTER-SMI",
                                                                                     "eriRouterProducts",
                                                                                     "eriRouterEntities",
                                                                                     "eriRouterModules")
(NotificationGroup, ModuleCompliance,) = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup",
                                                                  "ModuleCompliance")
(Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, IpAddress, TimeTicks,
 Counter64, Unsigned32, iso, Gauge32, ModuleIdentity, ObjectIdentity, Bits, Counter32,) = mibBuilder.importSymbols(
    "SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType",
    "MibIdentifier", "IpAddress", "TimeTicks", "Counter64", "Unsigned32", "iso", "Gauge32", "ModuleIdentity",
    "ObjectIdentity", "Bits", "Counter32")
(DisplayString, TextualConvention,) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
eriRouterProductMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 193, 218, 5, 1)).setRevisions(("2015-08-25 18:00",
                                                                                       "2015-01-14 18:00",
                                                                                       "2014-09-22 18:00",
                                                                                       "2013-10-17 18:00",
                                                                                       "2013-09-16 18:00",
                                                                                       "2013-06-19 18:00",
                                                                                       "2013-04-18 18:00",
                                                                                       "2013-01-14 18:00",
                                                                                       "2012-06-25 18:00",
                                                                                       "2012-03-19 18:00",
                                                                                       "2012-02-10 18:00",
                                                                                       "2011-06-02 18:00",
                                                                                       "2011-01-19 18:00",
                                                                                       "2010-10-01 00:00",
                                                                                       "2010-08-27 00:00",
                                                                                       "2010-04-01 00:00",
                                                                                       "2010-01-27 00:00",
                                                                                       "2009-10-05 00:00",
                                                                                       "2009-09-24 00:00",
                                                                                       "2009-09-13 00:00",
                                                                                       "2009-09-10 00:00",
                                                                                       "2009-07-16 00:00",
                                                                                       "2009-02-04 00:00",
                                                                                       "2009-01-20 00:00",
                                                                                       "2008-09-23 00:00",
                                                                                       "2008-07-02 00:00",
                                                                                       "2008-05-20 00:00",
                                                                                       "2008-05-08 00:00",
                                                                                       "2007-09-20 00:00",
                                                                                       "2007-08-08 00:00",
                                                                                       "2007-05-09 00:00",
                                                                                       "2007-02-28 00:00",
                                                                                       "2007-02-14 00:00",
                                                                                       "2007-02-05 00:00",
                                                                                       "2005-12-27 00:00",
                                                                                       "2005-03-01 00:00",
                                                                                       "2004-11-05 00:00",
                                                                                       "2004-05-11 00:00",
                                                                                       "2003-09-25 00:00",
                                                                                       "2003-07-24 00:00",
                                                                                       "2003-05-19 17:00",
                                                                                       "2003-05-05 00:00",
                                                                                       "2003-03-25 00:00",
                                                                                       "2002-06-13 00:00",
                                                                                       "2002-06-06 00:00",
                                                                                       "2001-12-12 00:00",
                                                                                       "2001-09-26 17:00",
                                                                                       "2001-07-25 10:00",
                                                                                       "2001-05-15 15:07",
                                                                                       "2001-05-04 16:42",
                                                                                       "2001-02-13 18:57",
                                                                                       "2001-02-13 10:07",
                                                                                       "2001-02-01 17:07",
                                                                                       "2001-01-05 18:34",
                                                                                       "2000-12-28 17:04",
                                                                                       "2000-11-15 17:04",
                                                                                       "2000-11-02 14:54",
                                                                                       "2000-10-25 15:23",
                                                                                       "2000-10-20 17:30",
                                                                                       "2000-09-26 13:30",
                                                                                       "2000-09-25 11:20",
                                                                                       "2000-07-19 15:44",
                                                                                       "2000-07-06 21:50",
                                                                                       "2000-06-16 17:00",
                                                                                       "2000-06-13 17:00",
                                                                                       "2000-05-18 00:00",
                                                                                       "1999-07-08 17:12",
                                                                                       "1998-08-05 19:00",))
eriRouterSMS1000 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 1, 1))
eriRouterSMS500 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 1, 2))
eriRouterSMS1800 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 1, 3))
eriRouterSMS10000 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 1, 4))
eriRouterSmartEdge800 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 1, 10))
eriRouterSmartEdge400 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 1, 11))
eriRouterSmartEdge100 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 1, 12))
eriRouterSmartEdge1200 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 1, 13))
eriRouterSM480 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 1, 14))
eriRouterSmartEdge600 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 1, 15))
eriRouterSM240 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 1, 16))
eriRouterSSR8020 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 1, 17))
eriRouterSSR8010 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 1, 18))
eriRouterSSR8004 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 1, 19))
eriRouterSP415 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 1, 20))
eriRouterSP420 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 1, 21))
eriRouterIposRefChassis = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 1, 22))
eriRouterIposRefPizza = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 1, 23))
eriRouterSSR8801 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 1, 30))
eriRouterEntityTypeOther = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 1))
eriRouterEntityTypeUnknown = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 2))
eriRouterEntityTypeChassis = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 3))
eriRouterEntChassisSMS1000 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 3, 1))
eriRouterEntChassisSMS500 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 3, 2))
eriRouterEntChassisSMS1800 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 3, 3))
eriRouterEntChassisSMS10000 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 3, 4))
eriRouterEntChassisSE800 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 3, 6))
eriRouterEntChassisSE400 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 3, 7))
eriRouterEntChassisSE100 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 3, 8))
eriRouterEntChassisSE1200 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 3, 9))
eriRouterEntChassisSM480 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 3, 10))
eriRouterEntChassisSE600 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 3, 11))
eriRouterEntChassisSM240 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 3, 12))
eriRouterEntChassisSE1200H = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 3, 13))
eriRouterEntChassisSSR8020 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 3, 14))
eriRouterEntChassisSSR8010 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 3, 15))
eriRouterEntChassisSSR8004 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 3, 16))
eriRouterEntChassisSP415 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 3, 17))
eriRouterEntChassisSP420 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 3, 18))
eriRouterEntityTypeBackplane = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 4))
eriRouterEntBackplaneSMS1000Data = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 4, 1))
eriRouterEntBackplaneSMS1000Power = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 4, 2))
eriRouterEntBackplaneSMS500Data = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 4, 3))
eriRouterEntBackplaneSMS500Power = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 4, 4))
eriRouterEntBackplaneSMS1800Data = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 4, 5))
eriRouterEntBackplaneSMS1800Power = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 4, 6))
eriRouterEntBackplaneSMS10000Midplane = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 4, 7))
eriRouterEntBackplaneSE800Data = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 4, 10))
eriRouterEntBackplaneSE400Data = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 4, 11))
eriRouterEntBackplaneSE100Data = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 4, 12))
eriRouterEntBackplaneSE1200Data = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 4, 13))
eriRouterEntBackplaneSM480Data = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 4, 14))
eriRouterEntBackplaneSE600Data = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 4, 15))
eriRouterEntBackplaneSM240Data = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 4, 16))
eriRouterEntBackplaneSE1200HData = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 4, 17))
eriRouterEntBackplaneSSR8020Data = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 4, 18))
eriRouterEntBackplaneSSR8010Data = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 4, 19))
eriRouterEntBackplaneSSR8004Data = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 4, 20))
eriRouterEntBackplaneSP415Data = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 4, 21))
eriRouterEntBackplaneSP420Data = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 4, 22))
eriRouterEntityTypeContainer = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 5))
eriRouterEntContainerSMS1000Data = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 5, 1))
eriRouterEntContainerSMS1000Power = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 5, 2))
eriRouterEntContainerSMS500Data = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 5, 3))
eriRouterEntContainerSMS500Power = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 5, 4))
eriRouterEntContainerSMS1800Data = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 5, 5))
eriRouterEntContainerSMS1800Power = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 5, 6))
eriRouterEntContainerSMS10000Fabric = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 5, 7))
eriRouterEntContainerSMS10000Timing = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 5, 8))
eriRouterEntContainerSMS10000SMCM = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 5, 9))
eriRouterEntContainerSMS10000IO = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 5, 10))
eriRouterEntContainerSE800Data = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 5, 14))
eriRouterEntContainerSE400Data = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 5, 15))
eriRouterEntContainerSE100Data = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 5, 16))
eriRouterEntContainerSE100Carrier = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 5, 17))
eriRouterEntContainerSE1200Data = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 5, 18))
eriRouterEntContainerSM480Data = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 5, 19))
eriRouterEntContainerSE600Data = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 5, 20))
eriRouterEntContainerSM240Data = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 5, 21))
eriRouterEntContainerSE1200HData = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 5, 22))
eriRouterEntContainerSSR8020FanTray = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 5, 23))
eriRouterEntContainerSSR8020PowerModule = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 5, 24))
eriRouterEntContainerSSR8020Data = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 5, 25))
eriRouterEntContainerSSR8010FanTray = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 5, 26))
eriRouterEntContainerSSR8010PowerModule = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 5, 27))
eriRouterEntContainerSSR8010Data = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 5, 28))
eriRouterEntContainerSSR8004FanTray = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 5, 29))
eriRouterEntContainerSSR8004PowerModule = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 5, 30))
eriRouterEntContainerSSR8004Data = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 5, 31))
eriRouterEntContainerSPSC1FanTray = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 5, 32))
eriRouterEntContainerSPSC1PowerModule = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 5, 33))
eriRouterEntContainerSPSC1Data = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 5, 34))
eriRouterEntityTypePowerSupply = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 6))
eriRouterEntPowerSupplyUnknown = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 6, 1))
eriRouterEntPowerSupplySMS1000AC = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 6, 2))
eriRouterEntPowerSupplySMS1000DC = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 6, 3))
eriRouterEntPowerSupplySMS500AC = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 6, 4))
eriRouterEntPowerSupplySMS500DC = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 6, 5))
eriRouterEntPowerSupplySMS1800AC = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 6, 6))
eriRouterEntPowerSupplySMS1800DC = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 6, 7))
eriRouterEntPowerModuleSSR = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 6, 10))
eriRouterEntPowerModuleSPSC1AC = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 6, 11))
eriRouterEntPowerModuleSPSC1DC = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 6, 12))
eriRouterEntityTypeFan = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 7))
eriRouterEntFanSE800 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 7, 1))
eriRouterEntFanSE400 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 7, 2))
eriRouterEntFanSE1200 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 7, 3))
eriRouterEntFanSM480 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 7, 4))
eriRouterEntFanSE600 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 7, 5))
eriRouterEntFanSM240 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 7, 6))
eriRouterEntFanSE1200H = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 7, 7))
eriRouterEntFanTraySSR = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 7, 8))
eriRouterEntFanTraySPSC1 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 7, 9))
eriRouterEntFanTrayAlarmIOSPSC1 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 7, 10))
eriRouterEntityTypeSensor = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 8))
eriRouterEntSensorAlarmSE400 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 8, 1))
eriRouterEntSensorAlarmSE600 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 8, 2))
eriRouterEntSensorAlarmSM240 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 8, 3))
eriRouterEntityTypeModule = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 9))
eriRouterEntModuleUnknown = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 9, 1))
eriRouterEntModuleSMSCE1 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 9, 16))
eriRouterEntModuleSMSCE2 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 9, 17))
eriRouterEntModuleSMSCE3 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 9, 18))
eriRouterEntModuleSMSFE1 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 9, 10))
eriRouterEntModuleSMSFE2 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 9, 12))
eriRouterEntModuleSMSFE3 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 9, 35))
eriRouterEntModuleSMSXFE = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 9, 40))
eriRouterEntModuleSMSFABRIC = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 9, 29))
eriRouterEntModuleSMSTIMING = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 9, 31))
eriRouterEntModuleSMSCM = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 9, 30))
eriRouterEntModuleSMSSM = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 9, 32))
eriRouterEntModuleSMSEIM = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 9, 6))
eriRouterEntModuleSMSGIGEIM = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 9, 26))
eriRouterEntModuleSMSAIMDS3 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 9, 4))
eriRouterEntModuleSMSPIME3 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 9, 8))
eriRouterEntModuleSMSPIME1 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 9, 22))
eriRouterEntModuleSMSAIME3 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 9, 5))
eriRouterEntModuleSMSAIME1 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 9, 23))
eriRouterEntModuleSMSAIMT1 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 9, 20))
eriRouterEntModuleSMSAIMOC3 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 9, 3))
eriRouterEntModuleSMSAIMOC12 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 9, 27))
eriRouterEntModuleSMSPOSOC3 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 9, 24))
eriRouterEntModuleSMSPOSOC12 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 9, 25))
eriRouterEntModuleSMSIPSEC = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 9, 28))
eriRouterEntModuleSMSPIMDS1 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 9, 14))
eriRouterEntModuleSMSPIMDS3 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 9, 7))
eriRouterEntModuleSMSPIMCDS3 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 9, 15))
eriRouterEntModuleSMSPIMHSSI = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 9, 9))
eriRouterEntModuleSEXC = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 9, 41))
eriRouterEntModuleSEEIM = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 9, 42))
eriRouterEntModuleSEGIGEIM = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 9, 43))
eriRouterEntModuleSEPOSOC12 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 9, 44))
eriRouterEntModuleSEPOSOC48 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 9, 45))
eriRouterEntModuleSEPOSOC3 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 9, 46))
eriRouterEntModuleSECHOC12DS1 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 9, 47))
eriRouterEntModuleSECHOC12DS3 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 9, 48))
eriRouterEntModuleSEAIMOC3 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 9, 49))
eriRouterEntModuleSEAIMOC12 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 9, 50))
eriRouterEntModuleSECHDS3 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 9, 51))
eriRouterEntModuleSEDS3 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 9, 52))
eriRouterEntModuleSEAIMDS3 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 9, 53))
eriRouterEntModuleSECHSTM1E1 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 9, 54))
eriRouterEntModuleSEE1 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 9, 55))
eriRouterEntModuleSEXC3 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 9, 56))
eriRouterEntModuleSEE3 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 9, 57))
eriRouterEntModuleSEAIMOC12E = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 9, 58))
eriRouterEntModuleSEGIGETM = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 9, 59))
eriRouterEntModuleSE10GIGEIM = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 9, 60))
eriRouterEntModuleSE100XC = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 9, 61))
eriRouterEntModuleSE100EMIC = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 9, 62))
eriRouterEntModuleSE100FXMIC = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 9, 63))
eriRouterEntModuleSE100GERJMIC = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 9, 64))
eriRouterEntModuleSE100GEFXMIC = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 9, 65))
eriRouterEntModuleSEXC4 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 9, 66))
eriRouterEntModuleSE100AIMOC3MIC = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 9, 67))
eriRouterEntModuleSEASE = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 9, 68))
eriRouterEntModuleSEFE60GE2 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 9, 69))
eriRouterEntModuleSEPOSOC192 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 9, 70))
eriRouterEntModuleSE5PortGIGE = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 9, 71))
eriRouterEntModuleSE20PortGIGE = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 9, 72))
eriRouterEntModuleSE4Port10GIGE = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 9, 73))
eriRouterEntModuleSE10GIGETM = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 9, 74))
eriRouterEntModuleSESSE = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 9, 75))
eriRouterEntModuleSE10PortGIGEDDR2 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 9, 76))
eriRouterEntModuleSE4PortOC48 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 9, 77))
eriRouterEntModuleSE8PortOC3 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 9, 78))
eriRouterEntModuleSE8OR2PORTCHOC3OC12 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 9, 79))
eriRouterEntModuleSEASE2 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 9, 80))
eriRouterEntModuleSE1Port10GEOC192 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 9, 81))
eriRouterEntModuleSEPos8xOC3 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 9, 82))
eriRouterEntModuleSEPos4xOC12 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 9, 83))
eriRouterEntModuleSEAtm2xOC12 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 9, 84))
eriRouterEntModuleSM10GIGEIM = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 9, 101))
eriRouterEntModuleSMRP2 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 9, 102))
eriRouterEntModuleSMGIGEIM = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 9, 104))
eriRouterEntModuleSMGIGETM = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 9, 105))
eriRouterEntModuleSM10GIGETM = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 9, 106))
eriRouterEntModuleSMFE60GE2 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 9, 107))
eriRouterEntModuleSM20PortGIGE = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 9, 108))
eriRouterEntModuleSM4Port10GIGE = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 9, 109))
eriRouterEntModuleSM10PortGIGEDDR2 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 9, 110))
eriRouterEntModuleSM1Port10GEOC192 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 9, 111))
eriRouterEntModuleSM8OR2PORTCHOC3OC12 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 9, 112))
eriRouterEntModuleSSRALSW = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 9, 201))
eriRouterEntModuleSSRRPSW = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 9, 202))
eriRouterEntModuleSSRSW = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 9, 203))
eriRouterEntModuleSSR40Port1GE = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 9, 204))
eriRouterEntModuleSSR10Port10GE = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 9, 205))
eriRouterEntModuleSSC1 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 9, 207))
eriRouterEntModuleSSC2 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 9, 208))
eriRouterEntModuleSSR20Port1GEor10GE = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 9, 209))
eriRouterEntModuleSSR2Port40GEor100GE = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 9, 210))
eriRouterEntModuleSSR20Port1GEor4Port10GE = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 9, 211))
eriRouterEntModuleSPSC1SC = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 9, 212))
eriRouterEntModuleSPSC11Port10GE = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 9, 213))
eriRouterEntModuleSPSC18PortCES = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 9, 214))
eriRouterEntModuleSPSC116Port1GE = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 9, 215))
eriRouterEntModuleSPSC120and2Port1and10GE = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 9, 216))
eriRouterEntModuleSSR20PortOC3orOC12orOC48orOC192 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 9, 217))
eriRouterEntityTypePort = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 10))
eriRouterEntPortUnknown = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 10, 1))
eriRouterEntPortSMSCE1MGMT = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 10, 16))
eriRouterEntPortSMSCE2MGMT = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 10, 17))
eriRouterEntPortSMSCE3MGMT = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 10, 18))
eriRouterEntPortSMSEIM = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 10, 6))
eriRouterEntPortSMSGIGEIM = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 10, 26))
eriRouterEntPortSMSAIMDS3 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 10, 4))
eriRouterEntPortSMSPIME3 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 10, 8))
eriRouterEntPortSMSPIME1 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 10, 22))
eriRouterEntPortSMSAIME3 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 10, 5))
eriRouterEntPortSMSAIME1 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 10, 23))
eriRouterEntPortSMSAIMT1 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 10, 20))
eriRouterEntPortSMSAIMOC3 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 10, 3))
eriRouterEntPortSMSAIMOC12 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 10, 27))
eriRouterEntPortSMSPOSOC3 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 10, 24))
eriRouterEntPortSMSPOSOC12 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 10, 25))
eriRouterEntPortSMSPIMDS1 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 10, 14))
eriRouterEntPortSMSPIMDS3 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 10, 7))
eriRouterEntPortSMSPIMCDS3 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 10, 15))
eriRouterEntPortSMSPIMHSSI = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 10, 9))
eriRouterEntPortSEXCMGMT = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 10, 41))
eriRouterEntPortSEEIM = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 10, 42))
eriRouterEntPortSEGIGEIM = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 10, 43))
eriRouterEntPortSEPOSOC12 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 10, 44))
eriRouterEntPortSEPOSOC48 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 10, 45))
eriRouterEntPortSEPOSOC3 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 10, 46))
eriRouterEntPortSECHOC12DS1 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 10, 47))
eriRouterEntPortSECHOC12DS3 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 10, 48))
eriRouterEntPortSEAIMOC3 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 10, 49))
eriRouterEntPortSEAIMOC12 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 10, 50))
eriRouterEntPortSECHDS3 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 10, 51))
eriRouterEntPortSEDS3 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 10, 52))
eriRouterEntPortSEAIMDS3 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 10, 53))
eriRouterEntPortSECHSTM1E1 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 10, 54))
eriRouterEntPortSEE1 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 10, 55))
eriRouterEntPortSEXC3MGMT = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 10, 56))
eriRouterEntPortSEE3 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 10, 57))
eriRouterEntPortSEAIMOC12E = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 10, 58))
eriRouterEntPortSEGIGETM = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 10, 59))
eriRouterEntPortSE10GIGEIM = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 10, 60))
eriRouterEntPortSE100XCMGMT = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 10, 61))
eriRouterEntPortSE100EIM = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 10, 62))
eriRouterEntPortSE100FXIM = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 10, 63))
eriRouterEntPortSE100GERJIM = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 10, 64))
eriRouterEntPortSE100GEFXIM = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 10, 65))
eriRouterEntPortSEXC4MGMT = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 10, 66))
eriRouterEntPortSE100AIMOC3 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 10, 67))
eriRouterEntPortSEPOSOC192 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 10, 68))
eriRouterEntPortSE10GIGETM = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 10, 69))
eriRouterEntPortSECHOC3OC12 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 10, 70))
eriRouterEntPortSECHOC3 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 10, 71))
eriRouterEntPortSM10GIGEIM = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 10, 101))
eriRouterEntPortSMRPMGMT = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 10, 103))
eriRouterEntPortSMGIGEIM = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 10, 104))
eriRouterEntPortSMGIGETM = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 10, 105))
eriRouterEntPortSM10GIGETM = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 10, 106))
eriRouterEntPortSMEIM = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 10, 107))
eriRouterEntPortSMCHOC3OC12 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 10, 108))
eriRouterEntPortSMCHOC3 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 10, 109))
eriRouterEntPortSSR1GE = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 10, 201))
eriRouterEntPortSSR10GE = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 10, 202))
eriRouterEntPortSSRRPSWMgmt = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 10, 203))
eriRouterEntPortSSR100GE = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 10, 204))
eriRouterEntPortSSR40GE = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 10, 205))
eriRouterEntPortSSR40GEor100GE = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 10, 206))
eriRouterEntPortSPSC11GE = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 10, 207))
eriRouterEntPortSPSC110GE = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 10, 208))
eriRouterEntPortSPSC1SCMgmt = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 10, 209))
eriRouterEntPortSPSC1AlarmIn = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 10, 210))
eriRouterEntPortSPSC1AlarmOut = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 10, 211))
eriRouterEntPortSSR20POSOCorOC12orOC48orOC192 = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 10, 212))
eriRouterEntityTypeStack = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 11))
eriRouterEntityTypeCPU = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 12))
eriRouterEntCpuUnknown = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 12, 1))
eriRouterEntCpuOcteon = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 12, 2))
eriRouterEntityTypeDisk = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 13))
eriRouterEntDiskUnknown = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 13, 1))
eriRouterEntDiskSSE = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 13, 2))
eriRouterEntityTypeMemory = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 218, 6, 14))
mibBuilder.exportSymbols("ERICSSON-ROUTER-PRODUCT-MIB", eriRouterEntPortSMSAIME3=eriRouterEntPortSMSAIME3,
                         eriRouterEntModuleSE100FXMIC=eriRouterEntModuleSE100FXMIC,
                         eriRouterEntModuleSM20PortGIGE=eriRouterEntModuleSM20PortGIGE,
                         eriRouterEntPortSMSAIMDS3=eriRouterEntPortSMSAIMDS3,
                         eriRouterEntContainerSMS10000Fabric=eriRouterEntContainerSMS10000Fabric,
                         eriRouterEntPortSEE1=eriRouterEntPortSEE1, eriRouterEntFanSM480=eriRouterEntFanSM480,
                         eriRouterEntFanSE600=eriRouterEntFanSE600,
                         eriRouterEntPortSPSC1SCMgmt=eriRouterEntPortSPSC1SCMgmt,
                         eriRouterEntityTypeFan=eriRouterEntityTypeFan, eriRouterEntFanSE1200=eriRouterEntFanSE1200,
                         eriRouterEntModuleSMSEIM=eriRouterEntModuleSMSEIM,
                         eriRouterEntContainerSE800Data=eriRouterEntContainerSE800Data,
                         eriRouterEntPortSMSPIMDS1=eriRouterEntPortSMSPIMDS1,
                         eriRouterSmartEdge1200=eriRouterSmartEdge1200,
                         eriRouterEntPortSECHSTM1E1=eriRouterEntPortSECHSTM1E1, eriRouterSMS1000=eriRouterSMS1000,
                         eriRouterEntModuleSEPos4xOC12=eriRouterEntModuleSEPos4xOC12,
                         eriRouterEntChassisSP420=eriRouterEntChassisSP420,
                         eriRouterEntBackplaneSMS1800Power=eriRouterEntBackplaneSMS1800Power,
                         eriRouterEntModuleSEXC3=eriRouterEntModuleSEXC3,
                         eriRouterEntChassisSE1200H=eriRouterEntChassisSE1200H,
                         eriRouterEntModuleSSRALSW=eriRouterEntModuleSSRALSW,
                         eriRouterEntPortSMSCE2MGMT=eriRouterEntPortSMSCE2MGMT,
                         eriRouterEntityTypeSensor=eriRouterEntityTypeSensor,
                         eriRouterEntPortSEGIGETM=eriRouterEntPortSEGIGETM,
                         eriRouterEntModuleSMSIPSEC=eriRouterEntModuleSMSIPSEC,
                         eriRouterEntBackplaneSP420Data=eriRouterEntBackplaneSP420Data,
                         eriRouterEntPortSMSPIMHSSI=eriRouterEntPortSMSPIMHSSI,
                         eriRouterEntityTypeContainer=eriRouterEntityTypeContainer,
                         eriRouterEntModuleSM8OR2PORTCHOC3OC12=eriRouterEntModuleSM8OR2PORTCHOC3OC12,
                         eriRouterEntPortUnknown=eriRouterEntPortUnknown,
                         eriRouterEntModuleSEAIMOC12=eriRouterEntModuleSEAIMOC12,
                         eriRouterEntChassisSM240=eriRouterEntChassisSM240,
                         eriRouterEntPortSPSC1AlarmIn=eriRouterEntPortSPSC1AlarmIn,
                         eriRouterEntModuleSEE1=eriRouterEntModuleSEE1, eriRouterEntPortSEE3=eriRouterEntPortSEE3,
                         eriRouterEntModuleSMRP2=eriRouterEntModuleSMRP2,
                         eriRouterEntContainerSE100Carrier=eriRouterEntContainerSE100Carrier,
                         eriRouterEntModuleSM10GIGEIM=eriRouterEntModuleSM10GIGEIM,
                         eriRouterEntChassisSE100=eriRouterEntChassisSE100,
                         eriRouterEntContainerSSR8010PowerModule=eriRouterEntContainerSSR8010PowerModule,
                         eriRouterEntModuleSMSAIME3=eriRouterEntModuleSMSAIME3,
                         eriRouterEntPortSEPOSOC12=eriRouterEntPortSEPOSOC12,
                         eriRouterEntModuleSEPos8xOC3=eriRouterEntModuleSEPos8xOC3, eriRouterSMS10000=eriRouterSMS10000,
                         eriRouterEntModuleSEXC4=eriRouterEntModuleSEXC4,
                         eriRouterEntPortSMSPOSOC12=eriRouterEntPortSMSPOSOC12,
                         eriRouterEntFanTrayAlarmIOSPSC1=eriRouterEntFanTrayAlarmIOSPSC1,
                         eriRouterEntContainerSSR8020Data=eriRouterEntContainerSSR8020Data,
                         eriRouterEntPortSM10GIGEIM=eriRouterEntPortSM10GIGEIM,
                         eriRouterEntPortSEAIMOC12=eriRouterEntPortSEAIMOC12,
                         eriRouterEntBackplaneSE800Data=eriRouterEntBackplaneSE800Data,
                         eriRouterEntityTypeStack=eriRouterEntityTypeStack,
                         eriRouterEntModuleSMSCE3=eriRouterEntModuleSMSCE3,
                         eriRouterEntityTypePowerSupply=eriRouterEntityTypePowerSupply,
                         eriRouterEntPortSSR40GEor100GE=eriRouterEntPortSSR40GEor100GE,
                         eriRouterEntModuleSPSC18PortCES=eriRouterEntModuleSPSC18PortCES,
                         eriRouterEntModuleSMSFE1=eriRouterEntModuleSMSFE1,
                         eriRouterEntPowerSupplySMS1800DC=eriRouterEntPowerSupplySMS1800DC,
                         eriRouterEntModuleSMSSM=eriRouterEntModuleSMSSM,
                         eriRouterEntPowerSupplySMS1000AC=eriRouterEntPowerSupplySMS1000AC,
                         eriRouterEntBackplaneSSR8004Data=eriRouterEntBackplaneSSR8004Data,
                         eriRouterEntContainerSMS1000Data=eriRouterEntContainerSMS1000Data,
                         eriRouterEntBackplaneSMS1000Power=eriRouterEntBackplaneSMS1000Power,
                         eriRouterEntityTypeModule=eriRouterEntityTypeModule,
                         eriRouterEntPortSSRRPSWMgmt=eriRouterEntPortSSRRPSWMgmt,
                         eriRouterEntCpuUnknown=eriRouterEntCpuUnknown,
                         eriRouterEntBackplaneSM240Data=eriRouterEntBackplaneSM240Data,
                         eriRouterEntContainerSE1200Data=eriRouterEntContainerSE1200Data,
                         eriRouterEntContainerSPSC1FanTray=eriRouterEntContainerSPSC1FanTray,
                         eriRouterEntContainerSE400Data=eriRouterEntContainerSE400Data,
                         eriRouterEntModuleSEPOSOC48=eriRouterEntModuleSEPOSOC48,
                         eriRouterEntModuleSMSXFE=eriRouterEntModuleSMSXFE,
                         eriRouterEntModuleSEAIMOC3=eriRouterEntModuleSEAIMOC3,
                         eriRouterEntModuleSMSPIMHSSI=eriRouterEntModuleSMSPIMHSSI,
                         eriRouterEntPortSMSAIME1=eriRouterEntPortSMSAIME1,
                         eriRouterEntPortSEXC4MGMT=eriRouterEntPortSEXC4MGMT,
                         eriRouterEntBackplaneSE400Data=eriRouterEntBackplaneSE400Data,
                         eriRouterEntModuleSMGIGEIM=eriRouterEntModuleSMGIGEIM,
                         eriRouterEntModuleSMSAIMDS3=eriRouterEntModuleSMSAIMDS3,
                         eriRouterIposRefChassis=eriRouterIposRefChassis,
                         eriRouterEntModuleSMSPIMCDS3=eriRouterEntModuleSMSPIMCDS3, eriRouterSMS1800=eriRouterSMS1800,
                         eriRouterEntContainerSMS1800Power=eriRouterEntContainerSMS1800Power,
                         eriRouterEntPortSMSAIMT1=eriRouterEntPortSMSAIMT1, eriRouterSmartEdge800=eriRouterSmartEdge800,
                         eriRouterEntFanSE400=eriRouterEntFanSE400,
                         eriRouterEntModuleSE4PortOC48=eriRouterEntModuleSE4PortOC48,
                         eriRouterEntContainerSPSC1PowerModule=eriRouterEntContainerSPSC1PowerModule,
                         eriRouterEntPortSECHOC3=eriRouterEntPortSECHOC3,
                         eriRouterEntPortSE100AIMOC3=eriRouterEntPortSE100AIMOC3,
                         eriRouterEntPortSSR1GE=eriRouterEntPortSSR1GE,
                         eriRouterEntModuleSMSAIMOC12=eriRouterEntModuleSMSAIMOC12,
                         eriRouterEntFanSE800=eriRouterEntFanSE800,
                         eriRouterEntPortSECHOC12DS1=eriRouterEntPortSECHOC12DS1,
                         eriRouterEntBackplaneSM480Data=eriRouterEntBackplaneSM480Data,
                         eriRouterEntDiskSSE=eriRouterEntDiskSSE, eriRouterEntModuleUnknown=eriRouterEntModuleUnknown,
                         eriRouterEntModuleSMGIGETM=eriRouterEntModuleSMGIGETM,
                         eriRouterEntPortSMCHOC3OC12=eriRouterEntPortSMCHOC3OC12,
                         eriRouterSmartEdge100=eriRouterSmartEdge100,
                         eriRouterEntPowerSupplySMS500DC=eriRouterEntPowerSupplySMS500DC,
                         eriRouterEntModuleSEAIMDS3=eriRouterEntModuleSEAIMDS3,
                         eriRouterEntPortSMSAIMOC12=eriRouterEntPortSMSAIMOC12,
                         eriRouterEntModuleSECHDS3=eriRouterEntModuleSECHDS3,
                         eriRouterEntContainerSM240Data=eriRouterEntContainerSM240Data,
                         eriRouterEntPortSE100GEFXIM=eriRouterEntPortSE100GEFXIM,
                         eriRouterSmartEdge600=eriRouterSmartEdge600, eriRouterEntPortSECHDS3=eriRouterEntPortSECHDS3,
                         eriRouterEntPortSEEIM=eriRouterEntPortSEEIM, eriRouterEntChassisSE800=eriRouterEntChassisSE800,
                         eriRouterEntPortSE10GIGETM=eriRouterEntPortSE10GIGETM,
                         eriRouterEntPortSE100FXIM=eriRouterEntPortSE100FXIM,
                         eriRouterEntChassisSM480=eriRouterEntChassisSM480,
                         eriRouterEntModuleSMSPIME1=eriRouterEntModuleSMSPIME1,
                         eriRouterEntityTypeDisk=eriRouterEntityTypeDisk,
                         eriRouterEntContainerSSR8010Data=eriRouterEntContainerSSR8010Data,
                         eriRouterSMS500=eriRouterSMS500, eriRouterEntPortSEPOSOC192=eriRouterEntPortSEPOSOC192,
                         eriRouterEntModuleSE8PortOC3=eriRouterEntModuleSE8PortOC3,
                         eriRouterEntModuleSEPOSOC12=eriRouterEntModuleSEPOSOC12,
                         eriRouterEntPortSM10GIGETM=eriRouterEntPortSM10GIGETM, eriRouterProductMIB=eriRouterProductMIB,
                         eriRouterEntBackplaneSMS1800Data=eriRouterEntBackplaneSMS1800Data,
                         eriRouterEntPortSMCHOC3=eriRouterEntPortSMCHOC3,
                         eriRouterEntBackplaneSP415Data=eriRouterEntBackplaneSP415Data,
                         eriRouterEntContainerSMS1000Power=eriRouterEntContainerSMS1000Power,
                         eriRouterEntityTypeOther=eriRouterEntityTypeOther,
                         eriRouterEntFanTraySPSC1=eriRouterEntFanTraySPSC1,
                         eriRouterEntPowerModuleSPSC1DC=eriRouterEntPowerModuleSPSC1DC,
                         eriRouterEntModuleSMSPOSOC3=eriRouterEntModuleSMSPOSOC3, eriRouterSM240=eriRouterSM240,
                         eriRouterEntModuleSPSC120and2Port1and10GE=eriRouterEntModuleSPSC120and2Port1and10GE,
                         eriRouterEntModuleSPSC116Port1GE=eriRouterEntModuleSPSC116Port1GE,
                         eriRouterEntModuleSSR20Port1GEor10GE=eriRouterEntModuleSSR20Port1GEor10GE,
                         eriRouterEntBackplaneSE1200HData=eriRouterEntBackplaneSE1200HData,
                         eriRouterEntContainerSSR8010FanTray=eriRouterEntContainerSSR8010FanTray,
                         eriRouterEntPortSEAIMOC3=eriRouterEntPortSEAIMOC3,
                         eriRouterEntPortSMSCE1MGMT=eriRouterEntPortSMSCE1MGMT,
                         eriRouterEntPortSE100EIM=eriRouterEntPortSE100EIM,
                         eriRouterEntModuleSECHOC12DS1=eriRouterEntModuleSECHOC12DS1,
                         eriRouterEntPortSEAIMDS3=eriRouterEntPortSEAIMDS3,
                         eriRouterEntChassisSSR8004=eriRouterEntChassisSSR8004,
                         eriRouterEntChassisSE400=eriRouterEntChassisSE400,
                         eriRouterEntSensorAlarmSM240=eriRouterEntSensorAlarmSM240,
                         eriRouterEntPowerSupplySMS1000DC=eriRouterEntPowerSupplySMS1000DC,
                         eriRouterEntModuleSEPOSOC192=eriRouterEntModuleSEPOSOC192,
                         eriRouterEntContainerSSR8020PowerModule=eriRouterEntContainerSSR8020PowerModule,
                         eriRouterEntModuleSE100EMIC=eriRouterEntModuleSE100EMIC,
                         eriRouterEntModuleSM4Port10GIGE=eriRouterEntModuleSM4Port10GIGE,
                         eriRouterEntPortSMSPOSOC3=eriRouterEntPortSMSPOSOC3,
                         eriRouterEntSensorAlarmSE600=eriRouterEntSensorAlarmSE600,
                         eriRouterEntityTypeChassis=eriRouterEntityTypeChassis,
                         eriRouterEntModuleSE100AIMOC3MIC=eriRouterEntModuleSE100AIMOC3MIC,
                         eriRouterEntModuleSM1Port10GEOC192=eriRouterEntModuleSM1Port10GEOC192,
                         eriRouterEntContainerSSR8020FanTray=eriRouterEntContainerSSR8020FanTray,
                         eriRouterEntSensorAlarmSE400=eriRouterEntSensorAlarmSE400, eriRouterSP420=eriRouterSP420,
                         eriRouterEntModuleSE4Port10GIGE=eriRouterEntModuleSE4Port10GIGE,
                         eriRouterEntModuleSSC2=eriRouterEntModuleSSC2,
                         eriRouterEntChassisSE1200=eriRouterEntChassisSE1200,
                         eriRouterEntPowerModuleSPSC1AC=eriRouterEntPowerModuleSPSC1AC,
                         eriRouterEntModuleSE100GERJMIC=eriRouterEntModuleSE100GERJMIC,
                         eriRouterEntPortSMSEIM=eriRouterEntPortSMSEIM,
                         eriRouterEntPortSE10GIGEIM=eriRouterEntPortSE10GIGEIM,
                         eriRouterEntBackplaneSMS500Power=eriRouterEntBackplaneSMS500Power,
                         eriRouterEntPortSPSC1AlarmOut=eriRouterEntPortSPSC1AlarmOut,
                         eriRouterEntModuleSEASE=eriRouterEntModuleSEASE,
                         eriRouterEntPortSEAIMOC12E=eriRouterEntPortSEAIMOC12E,
                         eriRouterEntModuleSMSFABRIC=eriRouterEntModuleSMSFABRIC,
                         eriRouterEntDiskUnknown=eriRouterEntDiskUnknown,
                         eriRouterEntModuleSSR2Port40GEor100GE=eriRouterEntModuleSSR2Port40GEor100GE,
                         eriRouterEntPowerSupplySMS500AC=eriRouterEntPowerSupplySMS500AC, eriRouterSM480=eriRouterSM480,
                         eriRouterEntModuleSEAtm2xOC12=eriRouterEntModuleSEAtm2xOC12,
                         eriRouterEntBackplaneSMS1000Data=eriRouterEntBackplaneSMS1000Data,
                         eriRouterEntModuleSMSPIMDS1=eriRouterEntModuleSMSPIMDS1,
                         eriRouterEntModuleSMSFE2=eriRouterEntModuleSMSFE2,
                         eriRouterEntPortSEPOSOC48=eriRouterEntPortSEPOSOC48,
                         eriRouterEntPortSSR40GE=eriRouterEntPortSSR40GE,
                         eriRouterEntContainerSSR8004PowerModule=eriRouterEntContainerSSR8004PowerModule,
                         eriRouterEntPortSE100XCMGMT=eriRouterEntPortSE100XCMGMT,
                         eriRouterEntModuleSMSAIMOC3=eriRouterEntModuleSMSAIMOC3,
                         eriRouterEntContainerSM480Data=eriRouterEntContainerSM480Data,
                         eriRouterEntPowerSupplyUnknown=eriRouterEntPowerSupplyUnknown,
                         eriRouterEntityTypeMemory=eriRouterEntityTypeMemory,
                         eriRouterEntContainerSMS10000IO=eriRouterEntContainerSMS10000IO,
                         eriRouterEntModuleSSR20Port1GEor4Port10GE=eriRouterEntModuleSSR20Port1GEor4Port10GE,
                         eriRouterEntityTypeBackplane=eriRouterEntityTypeBackplane,
                         eriRouterSmartEdge400=eriRouterSmartEdge400, eriRouterEntPortSEGIGEIM=eriRouterEntPortSEGIGEIM,
                         eriRouterEntModuleSMSFE3=eriRouterEntModuleSMSFE3,
                         eriRouterEntBackplaneSMS500Data=eriRouterEntBackplaneSMS500Data,
                         eriRouterEntModuleSSC1=eriRouterEntModuleSSC1,
                         eriRouterEntModuleSE10GIGETM=eriRouterEntModuleSE10GIGETM,
                         eriRouterEntContainerSMS500Data=eriRouterEntContainerSMS500Data,
                         eriRouterEntModuleSMSGIGEIM=eriRouterEntModuleSMSGIGEIM,
                         eriRouterEntContainerSSR8004Data=eriRouterEntContainerSSR8004Data,
                         eriRouterEntModuleSEEIM=eriRouterEntModuleSEEIM,
                         eriRouterEntityTypeUnknown=eriRouterEntityTypeUnknown,
                         eriRouterEntModuleSEPOSOC3=eriRouterEntModuleSEPOSOC3,
                         eriRouterEntBackplaneSSR8010Data=eriRouterEntBackplaneSSR8010Data,
                         eriRouterEntPortSMGIGEIM=eriRouterEntPortSMGIGEIM,
                         eriRouterEntChassisSSR8010=eriRouterEntChassisSSR8010,
                         eriRouterEntPortSECHOC12DS3=eriRouterEntPortSECHOC12DS3, eriRouterSSR8010=eriRouterSSR8010,
                         eriRouterEntModuleSMSCE1=eriRouterEntModuleSMSCE1,
                         eriRouterEntModuleSSR20PortOC3orOC12orOC48orOC192=eriRouterEntModuleSSR20PortOC3orOC12orOC48orOC192,
                         eriRouterEntModuleSECHOC12DS3=eriRouterEntModuleSECHOC12DS3,
                         eriRouterEntContainerSPSC1Data=eriRouterEntContainerSPSC1Data,
                         eriRouterEntModuleSMSCM=eriRouterEntModuleSMSCM, eriRouterEntPortSMEIM=eriRouterEntPortSMEIM,
                         eriRouterEntModuleSEXC=eriRouterEntModuleSEXC,
                         eriRouterEntModuleSECHSTM1E1=eriRouterEntModuleSECHSTM1E1,
                         eriRouterEntPowerSupplySMS1800AC=eriRouterEntPowerSupplySMS1800AC,
                         eriRouterEntContainerSMS1800Data=eriRouterEntContainerSMS1800Data,
                         eriRouterEntModuleSMSAIME1=eriRouterEntModuleSMSAIME1,
                         eriRouterEntPortSMSAIMOC3=eriRouterEntPortSMSAIMOC3,
                         eriRouterEntPortSMSPIME1=eriRouterEntPortSMSPIME1,
                         eriRouterEntContainerSSR8004FanTray=eriRouterEntContainerSSR8004FanTray,
                         eriRouterEntPowerModuleSSR=eriRouterEntPowerModuleSSR,
                         eriRouterEntCpuOcteon=eriRouterEntCpuOcteon,
                         eriRouterEntPortSMSCE3MGMT=eriRouterEntPortSMSCE3MGMT,
                         eriRouterEntModuleSMSPIMDS3=eriRouterEntModuleSMSPIMDS3,
                         eriRouterEntModuleSEFE60GE2=eriRouterEntModuleSEFE60GE2,
                         eriRouterIposRefPizza=eriRouterIposRefPizza,
                         eriRouterEntModuleSE5PortGIGE=eriRouterEntModuleSE5PortGIGE,
                         eriRouterEntContainerSE100Data=eriRouterEntContainerSE100Data,
                         eriRouterEntityTypeCPU=eriRouterEntityTypeCPU,
                         eriRouterEntChassisSMS10000=eriRouterEntChassisSMS10000,
                         eriRouterEntModuleSMSCE2=eriRouterEntModuleSMSCE2,
                         eriRouterEntModuleSSRSW=eriRouterEntModuleSSRSW,
                         eriRouterEntPortSEPOSOC3=eriRouterEntPortSEPOSOC3,
                         eriRouterEntModuleSEAIMOC12E=eriRouterEntModuleSEAIMOC12E,
                         eriRouterEntContainerSMS10000Timing=eriRouterEntContainerSMS10000Timing,
                         eriRouterEntModuleSM10PortGIGEDDR2=eriRouterEntModuleSM10PortGIGEDDR2,
                         eriRouterEntModuleSE10PortGIGEDDR2=eriRouterEntModuleSE10PortGIGEDDR2,
                         eriRouterEntPortSPSC11GE=eriRouterEntPortSPSC11GE,
                         eriRouterEntModuleSM10GIGETM=eriRouterEntModuleSM10GIGETM,
                         eriRouterEntModuleSESSE=eriRouterEntModuleSESSE,
                         eriRouterEntModuleSE10GIGEIM=eriRouterEntModuleSE10GIGEIM,
                         eriRouterEntPortSMSPIME3=eriRouterEntPortSMSPIME3,
                         eriRouterEntFanTraySSR=eriRouterEntFanTraySSR,
                         eriRouterEntModuleSE100GEFXMIC=eriRouterEntModuleSE100GEFXMIC,
                         eriRouterEntPortSMGIGETM=eriRouterEntPortSMGIGETM,
                         eriRouterEntPortSMSPIMDS3=eriRouterEntPortSMSPIMDS3,
                         eriRouterEntModuleSMSPIME3=eriRouterEntModuleSMSPIME3,
                         eriRouterEntPortSE100GERJIM=eriRouterEntPortSE100GERJIM,
                         eriRouterEntBackplaneSE1200Data=eriRouterEntBackplaneSE1200Data,
                         eriRouterEntPortSPSC110GE=eriRouterEntPortSPSC110GE,
                         eriRouterEntChassisSMS500=eriRouterEntChassisSMS500,
                         eriRouterEntPortSECHOC3OC12=eriRouterEntPortSECHOC3OC12,
                         eriRouterEntBackplaneSSR8020Data=eriRouterEntBackplaneSSR8020Data)
mibBuilder.exportSymbols("ERICSSON-ROUTER-PRODUCT-MIB", eriRouterEntPortSSR100GE=eriRouterEntPortSSR100GE,
                         eriRouterEntBackplaneSE600Data=eriRouterEntBackplaneSE600Data,
                         eriRouterSSR8801=eriRouterSSR8801,
                         eriRouterEntContainerSMS10000SMCM=eriRouterEntContainerSMS10000SMCM,
                         PYSNMP_MODULE_ID=eriRouterProductMIB, eriRouterEntPortSMSPIMCDS3=eriRouterEntPortSMSPIMCDS3,
                         eriRouterEntChassisSMS1000=eriRouterEntChassisSMS1000, eriRouterSSR8004=eriRouterSSR8004,
                         eriRouterEntContainerSMS500Power=eriRouterEntContainerSMS500Power,
                         eriRouterEntityTypePort=eriRouterEntityTypePort,
                         eriRouterEntModuleSE1Port10GEOC192=eriRouterEntModuleSE1Port10GEOC192,
                         eriRouterEntPortSSR20POSOCorOC12orOC48orOC192=eriRouterEntPortSSR20POSOCorOC12orOC48orOC192,
                         eriRouterSSR8020=eriRouterSSR8020, eriRouterEntModuleSE100XC=eriRouterEntModuleSE100XC,
                         eriRouterSP415=eriRouterSP415, eriRouterEntModuleSMSAIMT1=eriRouterEntModuleSMSAIMT1,
                         eriRouterEntModuleSSRRPSW=eriRouterEntModuleSSRRPSW,
                         eriRouterEntChassisSSR8020=eriRouterEntChassisSSR8020,
                         eriRouterEntContainerSE1200HData=eriRouterEntContainerSE1200HData,
                         eriRouterEntContainerSE600Data=eriRouterEntContainerSE600Data,
                         eriRouterEntModuleSMFE60GE2=eriRouterEntModuleSMFE60GE2,
                         eriRouterEntPortSEXCMGMT=eriRouterEntPortSEXCMGMT,
                         eriRouterEntPortSSR10GE=eriRouterEntPortSSR10GE,
                         eriRouterEntChassisSE600=eriRouterEntChassisSE600,
                         eriRouterEntPortSMRPMGMT=eriRouterEntPortSMRPMGMT,
                         eriRouterEntBackplaneSMS10000Midplane=eriRouterEntBackplaneSMS10000Midplane,
                         eriRouterEntPortSEXC3MGMT=eriRouterEntPortSEXC3MGMT,
                         eriRouterEntModuleSPSC11Port10GE=eriRouterEntModuleSPSC11Port10GE,
                         eriRouterEntModuleSEDS3=eriRouterEntModuleSEDS3,
                         eriRouterEntModuleSSR40Port1GE=eriRouterEntModuleSSR40Port1GE,
                         eriRouterEntModuleSPSC1SC=eriRouterEntModuleSPSC1SC,
                         eriRouterEntModuleSEASE2=eriRouterEntModuleSEASE2,
                         eriRouterEntPortSMSGIGEIM=eriRouterEntPortSMSGIGEIM, eriRouterEntFanSM240=eriRouterEntFanSM240,
                         eriRouterEntModuleSE8OR2PORTCHOC3OC12=eriRouterEntModuleSE8OR2PORTCHOC3OC12,
                         eriRouterEntBackplaneSE100Data=eriRouterEntBackplaneSE100Data,
                         eriRouterEntModuleSSR10Port10GE=eriRouterEntModuleSSR10Port10GE,
                         eriRouterEntModuleSE20PortGIGE=eriRouterEntModuleSE20PortGIGE,
                         eriRouterEntModuleSMSTIMING=eriRouterEntModuleSMSTIMING,
                         eriRouterEntModuleSEGIGETM=eriRouterEntModuleSEGIGETM,
                         eriRouterEntModuleSMSPOSOC12=eriRouterEntModuleSMSPOSOC12,
                         eriRouterEntModuleSEE3=eriRouterEntModuleSEE3,
                         eriRouterEntModuleSEGIGEIM=eriRouterEntModuleSEGIGEIM,
                         eriRouterEntPortSEDS3=eriRouterEntPortSEDS3, eriRouterEntFanSE1200H=eriRouterEntFanSE1200H,
                         eriRouterEntChassisSMS1800=eriRouterEntChassisSMS1800,
                         eriRouterEntChassisSP415=eriRouterEntChassisSP415)
