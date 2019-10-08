import FWCore.ParameterSet.Config as cms

from CondCore.DBCommon.CondDBSetup_cfi import *

RerecoGlobalTag = cms.ESSource("PoolDBESSource",
                               CondDBSetup,
                               connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
                               globaltag = cms.string('101X_dataRun2_Prompt_v9'),
                               toGet = cms.VPSet(
        cms.PSet(record = cms.string("EcalPedestalsRcd"),
                 #tag = cms.string("EcalPedestals_timestamp_10May2018_collisions_blue_laser"),
                 tag = cms.string("EcalPedestals_timestamp_2018"),
                 connect = cms.string("sqlite_file:/eos/cms/store/group/dpg_ecal/comm_ecal/pedestals_gainratio/EcalPedestals_timestamp_10May2018_collisions_blue_laser.db")
                 ),
        cms.PSet(record = cms.string("EcalLaserAlphasRcd"),
                 tag = cms.string("EcalLaserAlphas_EB152-150_EEbyring"),
                 connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS")
                 ),
        
        ),
                               
                               )
