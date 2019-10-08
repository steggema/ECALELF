import FWCore.ParameterSet.Config as cms

from CondCore.DBCommon.CondDBSetup_cfi import *

RerecoGlobalTag = cms.ESSource("PoolDBESSource",
                               CondDBSetup,
                               connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
                               globaltag = cms.string('94X_dataRun2_ReReco_EOY17_v2'),
                               toGet = cms.VPSet(
        				cms.PSet(record = cms.string("EcalIntercalibConstantsRcd"),
						 tag = cms.string("EcalIntercalibConstants_Run2017BCDE_eopPNEB_etaScalePNEE_zeeIC_v1"),
                 			         connect = cms.string("sqlite_file:/eos/cms/store/user/bmarzocc/EcalIntercalibConstants_Run2017BCDE_eopPNEB_etaScalePNEE_zeeIC_v1.db")
                 				)
        				),

                              )
