import FWCore.ParameterSet.Config as cms
from CondCore.DBCommon.CondDBSetup_cfi import *

RerecoGlobalTag = cms.ESSource("PoolDBESSource",
                               CondDBSetup,
                               connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
                               globaltag = cms.string('102X_dataRun2_Sep2018Rereco_v1'),


                               toGet = cms.VPSet(
        
        
        cms.PSet(record = cms.string("EcalIntercalibConstantsRcd"),
                 tag = cms.string("EcalIntercalibConstants_Run2018ABCD_run297056_eopPNEB_Combination_withFinalReg_withEtaScale_v2"),
                 connect = cms.string("sqlite_file:/eos/cms/store/group/dpg_ecal/alca_ecalcalib/IC_tags/Cal_UL2018/EcalIntercalibConstants_Run2018ABCD_run297056_eopPNEB_Combination_withFinalReg_withEtaScale_v2.db")
                 ),
        cms.PSet(record = cms.string("EcalPedestalsRcd"),
                 tag = cms.string("EcalPedestals_timestamp_2018_18January2019_collisions_blue_laser"),
                 connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS")
                 ),
        cms.PSet(record = cms.string("EcalPulseShapesRcd"),
                 tag = cms.string("EcalPulseShapes_UltraLegacy2018_calib"),
                 connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS")
                 ),
        
        cms.PSet(record = cms.string("EcalLaserAPDPNRatiosRcd"),
                 tag = cms.string("EcalLaserAPDPNRatios_rereco2018_v3"),
                 connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS")
                 ),

        cms.PSet(record = cms.string("EcalLaserAlphasRcd"),
                 tag = cms.string("EcalLaserAlphas_EB152-150_EEoptimized18"),
                 connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS")
                 ),

        cms.PSet(record = cms.string("EcalPFRecHitThresholdsRcd"),
                 tag = cms.string("EcalPFRecHitThresholds_UL_2018_2e3sig"),
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



