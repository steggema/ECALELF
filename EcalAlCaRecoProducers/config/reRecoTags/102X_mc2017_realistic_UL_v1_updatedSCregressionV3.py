import FWCore.ParameterSet.Config as cms
# Legacy re-reco 2016 with fixed high eta region of ECAL ICs
from CondCore.DBCommon.CondDBSetup_cfi import *

RerecoGlobalTag = cms.ESSource("PoolDBESSource",
                               CondDBSetup,
                               connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
                               globaltag = cms.string('102X_mc2017_realistic_UL_v1'),

                               toGet = cms.VPSet(

 
        cms.PSet(record = cms.string("GBRDWrapperRcd"),
                 tag = cms.string("pfscecal_EBCorrection_offline_v3_2017UL"),
                 label = cms.untracked.string("pfscecal_EBCorrection_offline_v3"),
                 connect = cms.string("sqlite_file:/eos/cms/store/group/phys_egamma/EgRegression/scReg_2017_UL_290419.db")
                 ),

        cms.PSet(record = cms.string("GBRDWrapperRcd"),
                 tag = cms.string("pfscecal_EBUncertainty_offline_v3_2017UL"),
                 label = cms.untracked.string("pfscecal_EBUncertainty_offline_v3"),
                 connect = cms.string("sqlite_file:/eos/cms/store/group/phys_egamma/EgRegression/scReg_2017_UL_290419.db")
                 ),

        cms.PSet(record = cms.string("GBRDWrapperRcd"),
                 tag = cms.string("pfscecal_EECorrection_offline_v3_2017UL"),
                 label = cms.untracked.string("pfscecal_EECorrection_offline_v3"),
                 connect = cms.string("sqlite_file:/eos/cms/store/group/phys_egamma/EgRegression/scReg_2017_UL_290419.db")
                 ),

        cms.PSet(record = cms.string("GBRDWrapperRcd"),
                 tag = cms.string("pfscecal_EEUncertainty_offline_v3_2017UL"),
                 label = cms.untracked.string("pfscecal_EEUncertainty_offline_v3"),
                 connect = cms.string("sqlite_file:/eos/cms/store/group/phys_egamma/EgRegression/scReg_2017_UL_290419.db")
                 )
        )
                              )



