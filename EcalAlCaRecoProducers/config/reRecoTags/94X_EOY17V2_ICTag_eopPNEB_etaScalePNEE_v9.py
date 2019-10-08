import FWCore.ParameterSet.Config as cms

from CondCore.DBCommon.CondDBSetup_cfi import *

RerecoGlobalTag = cms.ESSource("PoolDBESSource",
                               CondDBSetup,
                               connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
                               globaltag = cms.string('94X_dataRun2_ReReco_EOY17_v2'),
                               toGet = cms.VPSet(
        				cms.PSet(record = cms.string("EcalIntercalibConstantsRcd"),
                 			tag = cms.string("EcalIntercalibConstants_eopPNEB_etaScalePNEE_v9"),
                 			connect = cms.string("sqlite_file:/afs/cern.ch/work/b/bmarzocc/public/EcalIntercalibConstants_eopPNEB_etaScalePNEE_v9.db")
                 				)
        				),

                              )
