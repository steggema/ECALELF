import FWCore.ParameterSet.Config as cms
from CondCore.DBCommon.CondDBSetup_cfi import *

RerecoGlobalTag = cms.ESSource("PoolDBESSource",
                               CondDBSetup,
                               connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
                               globaltag = cms.string('102X_dataRun2_Sep2018Rereco_v1'),


                               toGet = cms.VPSet(
        
        
        cms.PSet(record = cms.string("EcalIntercalibConstantsRcd"),
                 tag = cms.string("EcalIntercalibConstants_UL_Run1_Run2_2018_v1"),
                 connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS")
                 ),
        cms.PSet(record = cms.string("EcalPedestalsRcd"),
                 tag = cms.string("EcalPedestals_timestamp_UL_Run1_Run2_2018_v1"),
                 connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS")
                 ),
        cms.PSet(record = cms.string("EcalPulseShapesRcd"),
                 tag = cms.string("EcalPulseShapes_UL_Run1_Run2_2018_v1"),
                 connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS")
                 ),
        
        cms.PSet(record = cms.string("EcalLaserAPDPNRatiosRcd"),
                 tag = cms.string("EcalLaserAPDPNRatios_UL_Run1_Run2_2018_v1"),
                 connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS")
                 ),

        cms.PSet(record = cms.string("EcalLaserAlphasRcd"),
                 tag = cms.string("EcalLaserAlphas_UL_Run1_Run2_2018_v1"),
                 connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS")
                 ),

        cms.PSet(record = cms.string("EcalPFRecHitThresholdsRcd"),
                 tag = cms.string("EcalPFRecHitThresholds_UL_Run1_Run2_2018_v1"),
                 connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS")
                 ),

        cms.PSet(record = cms.string("EcalChannelStatusRcd"),
                 tag = cms.string("EcalChannelStatus_v13_offline"),
                 connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS")
                 ),

        cms.PSet(record = cms.string("ESIntercalibConstantsRcd"),
                 tag = cms.string("ESIntercalibConstants_Run1_Run2_V14_offline"),
                 connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS")
                 ),

        cms.PSet(record = cms.string("ESEEIntercalibConstantsRcd"),
                 tag = cms.string("ESEEIntercalibConstants_V06_offline"),
                 connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS")
                 ),

        cms.PSet(record = cms.string("GBRDWrapperRcd"),
                 tag = cms.string("pfscecal_EBCorrection_offline_v2_2018UL"),
                 label = cms.untracked.string("pfscecal_EBCorrection_offline_v2"),
                 connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS")
                 ),

        cms.PSet(record = cms.string("GBRDWrapperRcd"),
                 tag = cms.string("pfscecal_EBUncertainty_offline_v2_2018UL"),
                 label = cms.untracked.string("pfscecal_EBUncertainty_offline_v2"),
                 connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS")
                 ),


        cms.PSet(record = cms.string("GBRDWrapperRcd"),
                 tag = cms.string("pfscecal_EECorrection_offline_v2_2018UL"),
                 label = cms.untracked.string("pfscecal_EECorrection_offline_v2"),
                 connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS")
                 ),


        cms.PSet(record = cms.string("GBRDWrapperRcd"),
                 tag = cms.string("pfscecal_EEUncertainty_offline_v2_2018UL"),
                 label = cms.untracked.string("pfscecal_EEUncertainty_offline_v2"),
                 connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS")
                 ),




        )
                               
                               
                               )



