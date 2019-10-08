import FWCore.ParameterSet.Config as cms
# Legacy re-reco 2016 with fixed high eta region of ECAL ICs
from CondCore.DBCommon.CondDBSetup_cfi import *

RerecoGlobalTag = cms.ESSource("PoolDBESSource",
                               CondDBSetup,
                               connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
                               globaltag = cms.string('101X_dataRun2_Prompt_v10'),
                               )


