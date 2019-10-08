import FWCore.ParameterSet.Config as cms

from CondCore.DBCommon.CondDBSetup_cfi import *

RerecoGlobalTag = cms.ESSource("PoolDBESSource",
                               CondDBSetup,
                               connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
                               globaltag = cms.string('102X_dataRun2_Prompt_v1'),
                               toGet = cms.VPSet(
        cms.PSet(record = cms.string("ESIntercalibConstantsRcd"),
                 tag = cms.string("ESIntercalibConstants_HG_Run2018D1"),
                 connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS")
                 ),
        )
)
