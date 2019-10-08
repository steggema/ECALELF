import FWCore.ParameterSet.Config as cms

from CondCore.DBCommon.CondDBSetup_cfi import *

RerecoGlobalTag = cms.ESSource("PoolDBESSource",
                               CondDBSetup,
                               connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
                               globaltag = cms.string('94X_dataRun2_ReReco_EOY17_v2'),
                               toGet = cms.VPSet(
        				cms.PSet(record = cms.string("EcalIntercalibConstantsRcd"),
                 			tag = cms.string("EcalIntercalibConstants_Run2017BCDEF_eopPNEB_etaScalePNEE_combICCorrections_v2"),
                 			connect = cms.string("sqlite_file:/eos/cms/store/group/dpg_ecal/alca_ecalcalib/IC_tags/Cal_Feb2018/EcalIntercalibConstants_Run2017BCDEF_eopPNEB_etaScalePNEE_combICCorrections_v2.db")
                 				)
        				),

                              )
