import FWCore.ParameterSet.Config as cms

from CondCore.DBCommon.CondDBSetup_cfi import *

RerecoGlobalTag = cms.ESSource("PoolDBESSource",
                               CondDBSetup,
                               connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
                               globaltag = cms.string('101X_dataRun2_Prompt_v10'),
                               toGet = cms.VPSet(
        cms.PSet(record = cms.string("ESIntercalibConstantsRcd"),
                 tag = cms.string("ESIntercalibConstants_LG_Run2018A_316766"),
                 connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS")
                 )
        )
                               )

