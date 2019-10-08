import FWCore.ParameterSet.Config as cms
# Legacy re-reco 2016 with fixed high eta region of ECAL ICs
from CondCore.DBCommon.CondDBSetup_cfi import *

RerecoGlobalTag = cms.ESSource("PoolDBESSource",
                               CondDBSetup,
                               connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
                               globaltag = cms.string('103X_dataRun2_v6'),

                               toGet = cms.VPSet(


        cms.PSet(record = cms.string("EcalIntercalibConstantsRcd"),
                 tag = cms.string("EcalIntercalibConstants_UL2017_Intermediate_v1"),
                 connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS"),
                 ),
        cms.PSet(record = cms.string("EcalPedestalsRcd"),
                 tag = cms.string("EcalPedestals_timestamp_UltraLegacy_2017_v1"),
                 connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS")
                 ),
        cms.PSet(record = cms.string("EcalPulseShapesRcd"),
                 tag = cms.string("EcalPulseShapes_UltraLegacy2017_calib"),
                 connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS")
                 ),

        cms.PSet(record = cms.string("EcalLaserAPDPNRatiosRcd"),
                 tag = cms.string("EcalLaserAPDPNRatios_rereco2017_v3"),
                 connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS")
                 ),

        cms.PSet(record = cms.string("EcalLaserAlphasRcd"),
                 tag = cms.string("EcalLaserAlphas_EB152-150_EE116_107_SICoptimized17"),
                 connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS")
                 ),

        cms.PSet(record = cms.string("EcalPFRecHitThresholdsRcd"),
                 tag = cms.string("EcalPFRecHitThresholds_UL_2017_mc_v2_mixedsigmas"),
                 connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS")
                 ),


        cms.PSet(record = cms.string("EcalChannelStatusRcd"),
                 tag = cms.string("EcalChannelStatus_v13_offline"),
                 connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS")
                 ),

        cms.PSet(record = cms.string("GBRDWrapperRcd"),
                 tag = cms.string("pfscecal_EBCorrection_offline_v2"),
                 label = cms.untracked.string("pfscecal_EBCorrection_offline_v2"),
                 connect = cms.string("sqlite_file:/afs/cern.ch/work/e/ecalmon/cmssw/CMSSW_10_3_2/src/Calibration/EcalAlCaRecoProducers/newSCRegression/v1/pfscecal_EBCorrection_offline_v2.db")
                 ),

        cms.PSet(record = cms.string("GBRDWrapperRcd"),
                 tag = cms.string("pfscecal_EBUncertainty_offline_v2"),
                 label = cms.untracked.string("pfscecal_EBUncertainty_offline_v2"),
                 connect = cms.string("sqlite_file:/afs/cern.ch/work/e/ecalmon/cmssw/CMSSW_10_3_2/src/Calibration/EcalAlCaRecoProducers/newSCRegression/v1/pfscecal_EBUncertainty_offline_v2.db")
                 ),

        cms.PSet(record = cms.string("GBRDWrapperRcd"),
                 tag = cms.string("pfscecal_EECorrection_offline_v2"),
                 label = cms.untracked.string("pfscecal_EECorrection_offline_v2"),
                 connect = cms.string("sqlite_file:/afs/cern.ch/work/e/ecalmon/cmssw/CMSSW_10_3_2/src/Calibration/EcalAlCaRecoProducers/newSCRegression/v1/pfscecal_EECorrection_offline_v2.db")
                 ),

        cms.PSet(record = cms.string("GBRDWrapperRcd"),
                 tag = cms.string("pfscecal_EEUncertainty_offline_v2"),
                 label = cms.untracked.string("pfscecal_EEUncertainty_offline_v2"),
                 connect = cms.string("sqlite_file:/afs/cern.ch/work/e/ecalmon/cmssw/CMSSW_10_3_2/src/Calibration/EcalAlCaRecoProducers/newSCRegression/v1/pfscecal_EEUncertainty_offline_v2.db")
                 ),

        )
)

