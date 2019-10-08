import FWCore.ParameterSet.Config as cms
from CondCore.DBCommon.CondDBSetup_cfi import *

RerecoGlobalTag = cms.ESSource("PoolDBESSource",
                               CondDBSetup,
                               connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
                               globaltag = cms.string('103X_dataRun2_v6'),


                               toGet = cms.VPSet(
        
        
                                   cms.PSet(record = cms.string("EcalIntercalibConstantsRcd"),
                                            tag = cms.string("EcalIntercalibConstants_Run2016_run297056_eopPNEB_v1"),
                                            connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS")
                                        ),
                                   cms.PSet(record = cms.string("EcalPedestalsRcd"),
                                         tag = cms.string("EcalPedestals_timestamp_UltraLegacy_2016_v1"),
                                         connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS")
                                     ),
                                   cms.PSet(record = cms.string("EcalPulseShapesRcd"),
                                            tag = cms.string("EcalPulseShapes_Ultimate2016_calib"),
                                            connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS")
                                        ),
                                   
                                   cms.PSet(record = cms.string("EcalLaserAPDPNRatiosRcd"),
                                            tag = cms.string("EcalLaserAPDPNRatios_rereco2016_v2"),
                                            connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS")
                                        ),
                                   
                                   cms.PSet(record = cms.string("EcalLaserAlphasRcd"),
                                            tag = cms.string("EcalLaserAlphas_EB152-150_EE_UL2016"),
                                            connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS")
                                        ),
                                   
                                   cms.PSet(record = cms.string("EcalPFRecHitThresholdsRcd"),
                                            tag = cms.string("EcalPFRecHitThresholds_UL_2016_byxt_mixed"),
                                            connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS")
                                        ),
                                   
                                   cms.PSet(record = cms.string("GBRDWrapperRcd"),
                                            label = cms.untracked.string("pfscecal_EBCorrection_offline_v2"),
                                            tag = cms.string("pfscecal_EBCorrection_offline_v2_2016ULV1"),
                                            connect = cms.string("frontier://FrontierPrep/CMS_CONDITIONS")
                                        ),
                                   
                                cms.PSet(record = cms.string("GBRDWrapperRcd"),
                                         label = cms.untracked.string("pfscecal_EECorrection_offline_v2"),
                                         tag = cms.string("pfscecal_EECorrection_offline_v2_2016ULV1"),
                                         connect = cms.string("frontier://FrontierPrep/CMS_CONDITIONS")
                                     ),

                                cms.PSet(record = cms.string("GBRDWrapperRcd"),
                                         label = cms.untracked.string("pfscecal_EBUncertainty_offline_v2"),
                                         tag = cms.string("pfscecal_EBUncertainty_offline_v2_2016ULV1"),
                                         connect = cms.string("frontier://FrontierPrep/CMS_CONDITIONS")
                                     ),
                                   
                                   cms.PSet(record = cms.string("GBRDWrapperRcd"),
                                            label = cms.untracked.string("pfscecal_EEUncertainty_offline_v2"),
                                            tag = cms.string("pfscecal_EEUncertainty_offline_v2_2016ULV1"),
                                            connect = cms.string("frontier://FrontierPrep/CMS_CONDITIONS")
                                        ),
                                   

                               )
                               
                               
)




