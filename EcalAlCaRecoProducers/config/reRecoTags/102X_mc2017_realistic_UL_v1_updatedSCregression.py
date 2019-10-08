import FWCore.ParameterSet.Config as cms
# Legacy re-reco 2016 with fixed high eta region of ECAL ICs
from CondCore.DBCommon.CondDBSetup_cfi import *

RerecoGlobalTag = cms.ESSource("PoolDBESSource",
                               CondDBSetup,
                               connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
                               globaltag = cms.string('102X_mc2017_realistic_UL_v1'),

                               toGet = cms.VPSet(
        cms.PSet(record = cms.string("GBRDWrapperRcd"),
                 tag = cms.string("pfscecal_EBCorrection_offline_v2"),
                 label = cms.untracked.string("pfscecal_EBCorrection_offline_v2"),
                 connect = cms.string("sqlite_file:/afs/cern.ch/work/e/ecalmon/cmssw/CMSSW_10_3_2/src/Calibration/EcalAlCaRecoProducers/newSCRegression/pfscecal_EBCorrection_offline_v2.db")
                 ),
        
        cms.PSet(record = cms.string("GBRDWrapperRcd"),
                 tag = cms.string("pfscecal_EBUncertainty_offline_v2"),
                 label = cms.untracked.string("pfscecal_EBUncertainty_offline_v2"),
                 connect = cms.string("sqlite_file:/afs/cern.ch/work/e/ecalmon/cmssw/CMSSW_10_3_2/src/Calibration/EcalAlCaRecoProducers/newSCRegression/pfscecal_EBUncertainty_offline_v2.db")
                 ),
        
        cms.PSet(record = cms.string("GBRDWrapperRcd"),
                 tag = cms.string("pfscecal_EECorrection_offline_v2"),
                 label = cms.untracked.string("pfscecal_EECorrection_offline_v2"),
                 connect = cms.string("sqlite_file:/afs/cern.ch/work/e/ecalmon/cmssw/CMSSW_10_3_2/src/Calibration/EcalAlCaRecoProducers/newSCRegression/pfscecal_EECorrection_offline_v2.db")
                 ),

        cms.PSet(record = cms.string("GBRDWrapperRcd"),
                 tag = cms.string("pfscecal_EEUncertainty_offline_v2"),
                 label = cms.untracked.string("pfscecal_EEUncertainty_offline_v2"),
                 connect = cms.string("sqlite_file:/afs/cern.ch/work/e/ecalmon/cmssw/CMSSW_10_3_2/src/Calibration/EcalAlCaRecoProducers/newSCRegression/pfscecal_EEUncertainty_offline_v2.db")
                 ),
)
                               )


