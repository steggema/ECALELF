import FWCore.ParameterSet.Config as cms
# Legacy re-reco 2016 with fixed high eta region of ECAL ICs
from CondCore.DBCommon.CondDBSetup_cfi import *

RerecoGlobalTag = cms.ESSource("PoolDBESSource",
                               CondDBSetup,
                               connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
                               globaltag = cms.string('101X_dataRun2_Prompt_v11'),

                               toGet = cms.VPSet(
        cms.PSet(record = cms.string("EcalPedestalsRcd"),
                 tag = cms.string("EcalPedestals_timestamp_2018"),
                 connect = cms.string("sqlite_file:/eos/cms/store/group/dpg_ecal/comm_ecal/pedestals_gainratio/EcalPedestals_timestamp_2018_25July2018_collisions_blue_laser.db")
                 ),
        cms.PSet(record = cms.string("EcalPulseShapesRcd"),
                 tag = cms.string("EcalPulseShapes_July2018_rereco_v1"),
                 connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS")
                 ),
                               )
)

