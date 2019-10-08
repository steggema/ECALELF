import FWCore.ParameterSet.Config as cms
from CondCore.DBCommon.CondDBSetup_cfi import *

RerecoGlobalTag = cms.ESSource("PoolDBESSource",
                               CondDBSetup,
                               connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
                               globaltag = cms.string('103X_upgrade2018_realistic_v9'),


                               toGet = cms.VPSet(
        
        
        cms.PSet(record = cms.string("EcalADCToGeVConstantRcd"),
                 tag = cms.string("EcalADCToGeVConstant_UL_2018_v1_mc"),
                 connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS")
                 ),

        cms.PSet(record = cms.string("EcalChannelStatusRcd"),
                 tag = cms.string("EcalChannelStatus_UL_2018_v2_mc"),
                 connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS")
                 ),

        cms.PSet(record = cms.string("EcalIntercalibConstantsMCRcd"),
                 tag = cms.string("EcalIntercalibConstants_MC_Digi_2018"),
                 connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS")
                 ),

        cms.PSet(record = cms.string("EcalIntercalibConstantsRcd"),
                 tag = cms.string("EcalIntercalibConstants_MC_Reco_2018"),
                 connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS")
                 ),

        cms.PSet(record = cms.string("EcalPedestalsRcd"),
                 tag = cms.string("EcalPedestals_UL_2018_mc"),
                 connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS")
                 ),

        cms.PSet(record = cms.string("EcalLaserAPDPNRatiosRcd"),
                 tag = cms.string("EcalLaserAPDPNRatios_UL_2018_mc_3sigma_v2"),
                 connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS")
                 ),

        cms.PSet(record = cms.string("EcalPFRecHitThresholdsRcd"),
                 tag = cms.string("EcalPFRecHitThresholds_UL_2018_2e3sig"),
                 connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS")
                 ),

        cms.PSet(record = cms.string("EcalTPGLinearizationConstRcd"),
                 tag = cms.string("EcalTPGLinearizationConst_UL_2018_mc"),
                 connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS")
                 ),

        cms.PSet(record = cms.string("EcalTPGPedestalsRcd"),
                 tag = cms.string("EcalTPGPedestals_UL_2018_mc"),
                 connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS")
                 ),

        cms.PSet(record = cms.string("ESIntercalibConstantsRcd"),
                 tag = cms.string("ESIntercalibConstants_LG_UL_2018_mc"),
                 connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS")
                 ),

        cms.PSet(record = cms.string("ESPedestalsRcd"),
                 tag = cms.string("ESPedestals_LG_UL_2018_mc"),
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



