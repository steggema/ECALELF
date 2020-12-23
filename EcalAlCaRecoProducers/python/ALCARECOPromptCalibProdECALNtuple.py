
import os, sys, imp, re
import copy

import FWCore.ParameterSet.Config as cms
from Calibration.EcalAlCaRecoProducers.customRereco import EcalRecal 

from RecoLocalCalo.Configuartion.ecalLocalRecoSequence_cff import ecalLocalRecoSequence




# ### setup any defaults you want
# output="alcaSkimALCARAW.root"
# secondaryOutput="ntuple.root"

# if not doTreeOnly:
#     # import of ALCARECO sequences
#     process.load('Calibration.EcalAlCaRecoProducers.ALCARECOEcalCalIsolElectron_cff') # reduction of recHits
#     process.load('Calibration.EcalAlCaRecoProducers.ALCARECOEcalCalIsolElectron_Output_cff')
#     process.load('Calibration.EcalAlCaRecoProducers.ALCARECOEcalUncalIsolElectron_cff') # reduction of recHits ==> gives the UseDB warning
#     process.load('Calibration.EcalAlCaRecoProducers.ALCARECOEcalUncalIsolElectron_Output_cff')
#     # this module provides:
#     # process.seqALCARECOEcalRecalElectron 
#     process.load('Calibration.EcalAlCaRecoProducers.ALCARECOEcalRecalIsolElectron_cff')
#     process.load('Calibration.EcalAlCaRecoProducers.ALCARECOEcalRecalIsolElectron_Output_cff')

#     #process.load('RecoEgamma.ElectronIdentification.egmGsfElectronIDs_cff')
#     from RecoLocalCalo.EcalRecProducers.ecalLocalCustom import *
#     #from PhysicsTools.SelectorUtils.tools.vid_id_tools import *

#     process.load("Calibration.EcalAlCaRecoProducers.PUDumper_cfi")

# # Tree production
# process.load('Calibration.ZNtupleDumper.ntupledumper_cff')
# process.load("RecoLuminosity.LumiProducer.bunchSpacingProducer_cfi")

from Calibration.ZNtupleDumper.elenewenergiesproduer_cfi import eleNewEnergiesProducer
from RecoEcal.EgammaClusterProducer.particleFlowSuperClusterEcal_cfi import particleFlowSuperClusterECAL

if usenewSCregressionFromSam:
    eleNewEnergiesProducer = eleNewEnergiesProducer.clone()
     # FIXME: It's v2 for 2016UL and 2018UL in the E/g code, but seems inconsistent?
    eleNewEnergiesProducer.scEnergyCorrectorSemiParm.regressionKeyEB = cms.string('pfscecal_EBCorrection_offline_v3')
    eleNewEnergiesProducer.scEnergyCorrectorSemiParm.regressionKeyEE = cms.string('pfscecal_EECorrection_offline_v3')
    eleNewEnergiesProducer.scEnergyCorrectorSemiParm.uncertaintyKeyEB = cms.string('pfscecal_EBUncertainty_offline_v3')
    eleNewEnergiesProducer.scEnergyCorrectorSemiParm.uncertaintyKeyEE = cms.string('pfscecal_EEUncertainty_offline_v3')
    eleNewEnergiesProducer.scEnergyCorrectorSemiParm.isHLT = cms.bool(False)
    eleNewEnergiesProducer.scEnergyCorrectorSemiParm.applySigmaIetaIphiBug  = cms.bool(False)

    particleFlowSuperClusterECAL.regressionConfig = cms.PSet(
        isHLT = cms.bool(False),
        applySigmaIetaIphiBug = cms.bool(False),
        ecalRecHitsEB = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
        ecalRecHitsEE = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
        regressionKeyEB = cms.string('pfscecal_EBCorrection_offline_v3'),
        regressionKeyEE = cms.string('pfscecal_EECorrection_offline_v3'),
        uncertaintyKeyEB = cms.string('pfscecal_EBUncertainty_offline_v3'),
        uncertaintyKeyEE = cms.string('pfscecal_EEUncertainty_offline_v3'),
        vertexCollection = cms.InputTag("offlinePrimaryVertices")
    )

from PhysicsTools.SelectorUtils.tools.vid_id_tools import setupAllVIDIdsInModule

# define which IDs we want to produce
my_id_modules = [
		# 'RecoEgamma.ElectronIdentification.Identification.cutBasedElectronHLTPreselecition_Summer16_V1_cff',
		# 'RecoEgamma.ElectronIdentification.Identification.cutBasedElectronID_Summer16_80X_V1_cff',
		'RecoEgamma.ElectronIdentification.Identification.cutBasedElectronID_Fall17_94X_V1_cff',
		]

#add them to the VID producer
for id_mod in my_id_modules:
	setupAllVIDIdsInModule(process, id_mod, setupVIDElectronSelection)


# ntuple
# added by Shervin for ES recHits (saved as in AOD): large window 15x3 (strip x row)
process.load('RecoEcal.EgammaClusterProducers.interestingDetIdCollectionProducer_cfi')
from RecoEcal.EgammaClusterProducers.interestingDetIdCollectionProducer_cfi import interestingDetIdCollectionProducer


myEleCollection =  cms.InputTag("gedGsfElectrons")

recalibElectronSrc = cms.InputTag("electronRecalibSCAssociator")

MinEleNumberFilter.src = myEleCollection


pfIsoEgamma = cms.Sequence()

process.load('Calibration.EcalAlCaRecoProducers.WZElectronSkims_cff')

process.load('DPGAnalysis.Skims.ZmmgSkim_cff')

process.MinMuonNumberFilter = cms.EDFilter("CandViewCountFilter",
                                          src = cms.InputTag("muons"),
                                          minNumber = cms.uint32(2))
process.MinPhoNumberFilter = cms.EDFilter("CandViewCountFilter",
                                          src = cms.InputTag("gedPhotons"),
                                          minNumber = cms.uint32(1))
process.filterSeq = cms.Sequence()
if (ZmmgSkim==True):
    process.filterSeq = cms.Sequence(process.MinMuonNumberFilter * process.MinPhoNumberFilter)

if (HLTFilter):
    from HLTrigger.HLTfilters.hltHighLevel_cfi import *
    process.ZEEHltFilter = copy.deepcopy(hltHighLevel)
    process.ZEEHltFilter.throw = cms.bool(False)
    process.ZEEHltFilter.HLTPaths = [ "HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_*"]
    process.filterSeq *= process.ZEEHltFilter

from HLTrigger.HLTfilters.hltHighLevel_cfi import *
process.NtupleFilter = copy.deepcopy(hltHighLevel)
process.NtupleFilter.throw = cms.bool(False)
process.NtupleFilter.HLTPaths = [ 'pathALCARECOEcalUncalZElectron',   'pathALCARECOEcalUncalWElectron',
                                  'pathALCARECOEcalCalZElectron',     'pathALCARECOEcalCalWElectron',
                                  'pathALCARECOEcalUncalZSCElectron', 'pathALCARECOEcalCalZSCElectron',
                                  'pathALCARECOEcalUncalSingleElectron', 'pathALCARECOEcalCalSingleElectron', ## in case of no skim
                                 ]


process.NtupleFilter.TriggerResultsTag = cms.InputTag("TriggerResults","","RECO")


process.NtupleFilterSeq = cms.Sequence()
if(ZSkim) and not doTreeOnly:
    process.NtupleFilterSeq = cms.Sequence(process.WZFilter)
  # process.NtupleFilterSeq= cms.Sequence(process.NtupleFilter)
    process.NtupleFilter.HLTPaths = [ 'pathALCARECOEcalCalZElectron', 'pathALCARECOEcalUncalZElectron',
                                      'pathALCARECOEcalCalZSCElectron', 'pathALCARECOEcalUncalZSCElectron',
                                      ]
elif(WSkim):
    process.NtupleFilterSeq = cms.Sequence(process.WZFilter)
    #    process.NtupleFilterSeq= cms.Sequence(process.NtupleFilter)
    process.NtupleFilter.HLTPaths = [ 'pathALCARECOEcalCalWElectron', 'pathALCARECOEcalUncalWElectron' ]
elif(ZmmgSkim):
    process.NtupleFilterSeq = cms.Sequence(process.ZmmgSkimSeq)
    process.NtupleFilter.HLTPaths = [ 'pathALCARECOEcalCalZmmgPhoton', 'pathALCARECOEcalUncalZmmgPhoton' ]

elif(options.skim=="no" or options.skim=="NO" or options.skim=="none" or options.skim=="NONE"):
    process.NtupleFilterSeq = cms.Sequence()
    process.NtupleFilter.HLTPaths = []


if(options.skim=="partGun"):
    process.zNtupleDumper.isPartGun = cms.bool(True)

###############################
# ECAL Recalibration
###############################
#============================== TO BE CHECKED FOR PRESHOWER
process.load("RecoEcal.EgammaClusterProducers.reducedRecHitsSequence_cff")
#process.reducedEcalRecHitsES.scEtThreshold = cms.double(0.)

#process.reducedEcalRecHitsES.EcalRecHitCollectionES = cms.InputTag('ecalPreshowerRecHit','EcalRecHitsES')
#process.reducedEcalRecHitsES.noFlag = cms.bool(True)
#process.reducedEcalRecHitsES.OutputLabel_ES = cms.string('alCaRecHitsES')

#==============================

        
try:
    EcalTrivialConditionRetriever
except NameError:
    #print "well, it WASN'T defined after all!"
    process.trivialCond = cms.Sequence()
else:
    print "** TrivialConditionRetriver defined"
    process.trivialCond = cms.Sequence( EcalTrivialConditionRetriever )

if not doTreeOnly:
    process.alcarerecoSeq=cms.Sequence( process.trivialCond * process.seqALCARECOEcalRecalElectron) # * process.reducedEcalRecHitsES)

    process.rhoFastJetSeq = cms.Sequence()

    if (options.skim=="ZmmgSkim"):
        process.patSequence=cms.Sequence( (process.muonSelectionProducers * process.phoSelectionProducers) * process.patMuons * process.patPhotons )
        process.patSequenceMC=cms.Sequence( process.muonMatch * process.photonMatch * (process.muonSelectionProducers * process.phoSelectionProducers ) * process.patMuons * process.patPhotons )

#process.egmGsfElectronIDs.physicsObjectSrc = cms.InputTag("patElectrons") #myEleCollection

if(options.type!="MINIAODNTUPLE"):
    if(MC):
        process.prePatSequence *= process.electronMatch
        process.alCaIsolatedElectrons.uncalibRecHitCollectionEB = cms.InputTag("")
        process.alCaIsolatedElectrons.uncalibRecHitCollectionEE = cms.InputTag("")
        process.alCaIsolatedElectrons.esRecHitsLabel = cms.InputTag("reducedEcalRecHitsES")

    process.ntupleSeq = cms.Sequence(process.jsonFilter * process.patSequence)
else:
    #process.load('PhysicsTools.PatAlgos.slimming.MiniAODfromMiniAOD_cff')
    process.ntupleSeq = cms.Sequence(process.jsonFilter  * process.patSequence)

    
if(options.doTree==0):
    process.zNtupleDumper.doStandardTree = cms.bool(False)
if(options.doEleIDTree>0):
    process.zNtupleDumper.doEleIDTree=cms.bool(True)
if(options.doExtraCalibTree>0):
    process.zNtupleDumper.doExtraCalibTree=cms.bool(True)
if(options.doExtraStudyTree>0):
    process.zNtupleDumper.doExtraStudyTree=cms.bool(True)
if(options.doTrackTree>0):
    process.zNtupleDumper.doTrackTree=cms.bool(True)


############################################################
# OUTPUT MODULES
##############################
fileName = cms.untracked.string(options.output)

if not doTreeOnly:
    process.outputALCARAW = cms.OutputModule("PoolOutputModule",
                                            # after 5 GB split the file
                                            maxSize = cms.untracked.int32(5120000),
                                            outputCommands = process.OutALCARECOEcalUncalElectron.outputCommands,
                                            #fileName = fileName,
                                            fileName = cms.untracked.string('alcaraw.root'),
                                            SelectEvents = process.OutALCARECOEcalUncalElectron.SelectEvents,
                                            dataset = cms.untracked.PSet(
                                                filterName = cms.untracked.string(''),
                                                dataTier = cms.untracked.string('ALCARECO')
                                            )
                                        )

    process.outputALCARECO = cms.OutputModule("PoolOutputModule",
                                            # after 5 GB split the file
                                            maxSize = cms.untracked.int32(5120000),
                                            outputCommands = process.OutALCARECOEcalCalElectron.outputCommands,
                                            fileName = cms.untracked.string('alcareco.root'),
                                            SelectEvents = process.OutALCARECOEcalCalElectron.SelectEvents,
                                            dataset = cms.untracked.PSet(
                                                filterName = cms.untracked.string(''),
                                                dataTier = cms.untracked.string('ALCARECO')
                                            )
                                        )

process.zNtupleDumper.SelectEvents = process.NtupleFilter.HLTPaths

if not doTreeOnly:
    process.outputALCARERECO = cms.OutputModule("PoolOutputModule",
                                                # after 5 GB split the file
                                                maxSize = cms.untracked.int32(5120000),
                                                outputCommands = process.OutALCARECOEcalCalElectron.outputCommands,
                                                fileName = cms.untracked.string('EcalRecalElectron.root'),
                                                SelectEvents = cms.untracked.PSet(
                                                    SelectEvents = cms.vstring('pathALCARERECOEcalCalElectron')
                                                ),
                                                dataset = cms.untracked.PSet(
                                                    filterName = cms.untracked.string(''),
                                                    dataTier = cms.untracked.string('ALCARECO')
                                                )
                                            )

    process.outputRECO = cms.OutputModule("PoolOutputModule",
                                        # after 5 GB split the file
                                        maxSize = cms.untracked.int32(5120000),
                                        outputCommands = cms.untracked.vstring('keep *'),
                                        fileName = cms.untracked.string('RECO.root'),
    #                                      SelectEvents = process.OutALCARECOEcalCalElectron.SelectEvents,
                                        dataset = cms.untracked.PSet(
                                            filterName = cms.untracked.string(''),
                                            dataTier = cms.untracked.string('RECO')
                                        )
                                    )

# ALCARAW
if not doTreeOnly:
    process.pathALCARECOEcalUncalSingleElectron = cms.Path(process.filterSeq *
                                                        process.seqALCARECOEcalUncalElectron 
                                                        )
    process.pathALCARECOEcalUncalZElectron = cms.Path(process.filterSeq * process.preFilterSeq *
                                                    process.seqALCARECOEcalUncalZElectron )
    process.pathALCARECOEcalUncalZSCElectron = cms.Path(process.filterSeq * process.preFilterSeq *
                                                        ~process.ZeeFilter * process.ZSCFilter *
                                                            process.seqALCARECOEcalUncalZSCElectron 
                                                        )
    process.pathALCARECOEcalUncalWElectron = cms.Path(process.filterSeq * process.preFilterSeq *
                                                    ~process.ZeeFilter * ~process.ZSCFilter * process.WenuFilter *
                                                    process.seqALCARECOEcalUncalWElectron 
                                                    )
    process.pathALCARECOEcalUncalZmmgPhoton = cms.Path(                                                        process.filterSeq * process.FilterMuSeq * process.ZmmgSkimSeq * 
                                                        ~process.ZeeFilter * ~process.ZSCFilter * ~process.WenuFilter *
                                                        process.seqALCARECOEcalUncalElectron ) #* process.hltReporter)


    # ALCARERECO
    process.pathALCARERECOEcalCalElectron = cms.Path(process.alcarerecoSeq)

    if(doAnyTree):
        process.pathALCARERECOEcalCalElectron+=cms.Sequence(  process.ntupleSeq) # this cannot be done because the json will prevent to save the alcareco files

    # ALCARECO
    process.pathALCARECOEcalCalSingleElectron = cms.Path(process.filterSeq *
                                                        process.pfIsoEgamma *
                                                        process.ALCARECOEcalCalElectronSeq)
    process.pathALCARECOEcalCalZElectron = cms.Path(process.filterSeq * 
                                                    process.ZeeSkimFilterSeq *                                                 
                                                    process.pfIsoEgamma *
                                                    process.ALCARECOEcalCalElectronSeq)
    process.pathALCARECOEcalCalWElectron = cms.Path(process.filterSeq *
                                                    process.WenuSkimFilterSeq *
                                                    process.pfIsoEgamma *
                                                    process.ALCARECOEcalCalElectronSeq)
    process.pathALCARECOEcalCalZSCElectron = cms.Path(process.filterSeq *
                                                    process.ZSCSkimFilterSeq *
    #                                                   process.ZSCHltFilter *
                                                    process.pfIsoEgamma *
                                                    process.ALCARECOEcalCalElectronSeq ) #* process.hltReporter)
    process.pathALCARECOEcalCalZmmgPhoton = cms.Path(process.filterSeq * process.FilterMuSeq *  
                                                    process.ZmmgSkimSeq *
                                                    ~process.ZeeFilter * ~process.ZSCFilter * ~process.WenuFilter *
                                                    process.pfIsoEgamma *
                                                    process.seqALCARECOEcalCalPhoton ) #* process.hltReporter)

if (options.skim=="ZmmgSkim"):
    process.NtuplePath = cms.Path(process.filterSeq * process.FilterMuSeq *  process.NtupleFilterSeq 
                                  #                              * process.pfIsoEgamma 
                                  #                              * process.ALCARECOEcalCalElectronSeq 
                               * process.ntupleSeq)
else:
    process.NtuplePath = cms.Path(process.filterSeq * process.preFilterSeq *  process.NtupleFilterSeq 
                            #    * process.ecalMultiFitUncalibRecHit
                               * process.ntupleSeq)
process.NtupleEndPath = cms.EndPath( process.zNtupleDumper)
if options.outputAll:
	outputAllFilename = "outputAll.root"
	process.output = cms.OutputModule("PoolOutputModule", fileName = cms.untracked.string(outputAllFilename))
	process.NtupleEndPath *= process.output


if(not doTreeOnly):
    process.ALCARECOoutput_step = cms.EndPath(process.outputALCARECO )
    if(options.type=="ALCARERECO"):
        process.ALCARERECOoutput_step = cms.EndPath(process.outputALCARERECO)

    if(options.type=="ALCARAW"):
        process.ALCARAWoutput_step = cms.EndPath(process.outputALCARAW)
            

############################################################
# Schedule definition
##############################
if not doTreeOnly:
    if(options.skim=='WSkim'):
        process.outputALCARAW.SelectEvents = cms.untracked.PSet(
            SelectEvents = cms.vstring('pathALCARECOEcalUncalWElectron')
            )
        process.outputALCARECO.SelectEvents = cms.untracked.PSet(
            SelectEvents = cms.vstring('pathALCARECOEcalCalWElectron')
            )
    elif(options.skim=='ZSkim'):
        process.outputALCARAW.SelectEvents = cms.untracked.PSet(
            SelectEvents = cms.vstring('pathALCARECOEcalUncalZElectron', 'pathALCARECOEcalUncalZSCElectron')
            )
        process.outputALCARECO.SelectEvents = cms.untracked.PSet(
            SelectEvents = cms.vstring('pathALCARECOEcalCalZElectron', 'pathALCARECOEcalCalZSCElectron')
            )
    elif(options.skim=='ZmmgSkim'):
        process.outputALCARAW.SelectEvents = cms.untracked.PSet(
            SelectEvents = cms.vstring('pathALCARECOEcalUncalZmmgPhoton')
            )
        process.outputALCARECO.SelectEvents = cms.untracked.PSet(
            SelectEvents = cms.vstring('pathALCARECOEcalCalZmmgPhoton')
            )
    else:
        #if(options.skim=="" or options.skim=="none" or options.skim=="no" or options.skim=="partGun"):
        process.outputALCARAW.SelectEvents = cms.untracked.PSet(
            SelectEvents = cms.vstring('pathALCARECOEcalUncalSingleElectron')
            )
        process.outputALCARECO.SelectEvents = cms.untracked.PSet(
            SelectEvents = cms.vstring('pathALCARECOEcalCalSingleElectron')
            )

if(options.type=='ALCARAW'):
    process.schedule = cms.Schedule(
        #process.raw2digi_step,process.L1Reco_step,
        #process.reconstruction_step,process.endjob_step, 
        process.pathALCARECOEcalUncalZElectron, process.pathALCARECOEcalUncalWElectron,
        process.pathALCARECOEcalUncalZSCElectron,
        process.pathALCARECOEcalUncalZmmgPhoton,
        process.ALCARAWoutput_step,
        process.pathALCARECOEcalCalZElectron,  process.pathALCARECOEcalCalWElectron,
        process.pathALCARECOEcalCalZSCElectron,
        process.pathALCARECOEcalCalZmmgPhoton,
        process.ALCARECOoutput_step, process.NtuplePath
    ) # fix the output modules
    

elif(options.type=='ALCARERECO'):
    if(doTreeOnly):
        process.NtuplePath = cms.Path(process.ntupleSeq * process.zNtupleDumper)
        process.schedule = cms.Schedule(process.NtuplePath) #, process.NtupleEndPath)
    else:
        if(doAnyTree):
            process.pathALCARERECOEcalCalElectron += process.zNtupleDumper
        process.schedule = cms.Schedule(process.pathALCARERECOEcalCalElectron, process.ALCARERECOoutput_step)
elif(options.type=='ALCARECO' or options.type=='ALCARECOSIM'):
    if(doTreeOnly):
        process.NtuplePath = cms.Path(process.bunchSpacingProducer*process.ecalLocalRecoSequence*process.ntupleSeq)
        process.schedule = cms.Schedule(process.NtuplePath, process.NtupleEndPath)
        process.zNtupleDumper.WZSkimResultsCollection = cms.InputTag('TriggerResults::ALCARECO')
        process.patElectrons.reducedBarrelRecHitCollection = cms.InputTag("ecalRecHit","EcalRecHitsEB")
        process.patElectrons.reducedEndcapRecHitCollection = cms.InputTag("ecalRecHit","EcalRecHitsEE")
    else:
        if(doAnyTree==False):
            process.schedule = cms.Schedule(process.pathALCARECOEcalCalZElectron,  process.pathALCARECOEcalCalWElectron,
                                            process.pathALCARECOEcalCalZSCElectron, #process.pathALCARECOEcalCalZmmgPhoton,
                                            process.ALCARECOoutput_step
                                            ) # fix the output modules
        else:
            process.schedule = cms.Schedule(process.pathALCARECOEcalCalZElectron,  process.pathALCARECOEcalCalWElectron,
                                            process.pathALCARECOEcalCalZSCElectron, #process.pathALCARECOEcalCalZmmgPhoton,
                                            #process.ALCARECOoutput_step,
                                            process.NtuplePath, process.NtupleEndPath
                                            ) # fix the output modules
        if(options.skim=="" or options.skim=="ZHLTSkim" or options.skim=="partGun"):
            process.schedule += cms.Schedule(process.pathALCARECOEcalCalSingleElectron)
elif(options.type=='SKIMEFFTEST'):
    process.schedule = cms.Schedule(process.pathWElectronSkimGen, process.pathZSCElectronSkimGen, process.pathZElectronSkimGen,
                                    process.pathWElectronSkim, process.pathZSCElectronSkim, process.pathZElectronSkim,
                                    process.pathWElectronGen, process.pathZSCElectronGen, process.pathZElectronGen,
                                    )
elif(options.type=='MINIAODNTUPLE'):
    process.schedule = cms.Schedule(process.NtuplePath, process.NtupleEndPath)

process.zNtupleDumper.foutName=options.secondaryOutput


############################################################
# Setting collection names
##############################
process.selectedECALElectrons.src = myEleCollection
process.PassingVetoId.src = myEleCollection

process.patElectrons.userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
)

process.electronMatch.src = myEleCollection
if (options.skim=="ZmmgSkim"):
    process.alCaIsolatedElectrons.photonLabel = cms.InputTag("gedPhotons")

if not doTreeOnly:
    process.alcaElectronTracksReducer.electronLabel = myEleCollection

rechitsEB = cms.InputTag("alCaIsolatedElectrons", "alcaBarrelHits")
rechitsEE = cms.InputTag("alCaIsolatedElectrons", "alcaEndcapHits")
rechitsES = cms.InputTag("alCaIsolatedElectrons", "alcaPreshowerHits")

process.eleNewEnergiesProducer.recHitCollectionEB = rechitsEB
process.eleNewEnergiesProducer.recHitCollectionEE = rechitsEE

for ps in process.egmGsfElectronIDs.physicsObjectIDs:
    for cutflow in ps.idDefinition.cutFlow:
        if(cutflow.cutName == cms.string('GsfEleCalPFClusterIsoCut') or 
            cutflow.cutName == cms.string('GsfEleCalPFClusterIsoCut') or
            cutflow.cutName == cms.string('GsfEleEffAreaPFIsoCut')
            ):
            cutflow.rho = cms.InputTag("fixedGridRhoFastjetAll:rho")
    

if(options.type=="ALCARERECO"):
    process = EcalRecal(process)
    process.electronMVAValueMapProducer.src = recalibElectronSrc   #####Commented for now SJ

    process.patElectrons.electronSource                = recalibElectronSrc
    process.alCaIsolatedElectrons.esRecHitsLabel = cms.InputTag("ecalPreshowerRecHit","EcalRecHitsES")

    process.outputALCARECO.outputCommands += process.OutALCARECOEcalRecalElectron.outputCommands
    process.outputALCARECO.fileName=cms.untracked.string('EcalRecalElectron.root')
    process.zNtupleDumper.WZSkimResultsCollection = cms.InputTag('TriggerResults::RECO') ## how and why and where is it used?

    for ps in process.egmGsfElectronIDs.physicsObjectIDs:
        for cutflow in ps.idDefinition.cutFlow:
            if(cutflow.cutName == cms.string('GsfEleCalPFClusterIsoCut') or 
               cutflow.cutName == cms.string('GsfEleCalPFClusterIsoCut') or
               cutflow.cutName == cms.string('GsfEleEffAreaPFIsoCut')
               ):
                # cutflow.rho = cms.InputTag("kt6PFJetsForRhoCorrection:rho")
                cutflow.rho = cms.InputTag("fixedGridRhoFastjetAll")
                

    # auto defined by the bunchSpacingProducer
    process.ecalMultiFitUncalibRecHit.algoPSet.useLumiInfoRunHeader = cms.bool(True)

    process.alCaIsolatedElectrons.uncalibRecHitCollectionEB = process.ecalRecHit.EBuncalibRecHitCollection
    process.alCaIsolatedElectrons.uncalibRecHitCollectionEE = process.ecalRecHit.EEuncalibRecHitCollection

    process.zNtupleDumper.uncalibRecHitCollectionEB = cms.InputTag("alCaIsolatedElectrons", process.alCaIsolatedElectrons.alcaBarrelUncalibHitCollection.value())
    process.zNtupleDumper.uncalibRecHitCollectionEE = cms.InputTag("alCaIsolatedElectrons", process.alCaIsolatedElectrons.alcaEndcapUncalibHitCollection.value())
    process.zNtupleDumper.recHitCollectionES = cms.InputTag('alCaIsolatedElectrons', 'alcaPreshowerHits')
    process.slimmedECALELFElectrons.reducedBarrelRecHitCollection = process.eleNewEnergiesProducer.recHitCollectionEB
    process.slimmedECALELFElectrons.reducedEndcapRecHitCollection = process.eleNewEnergiesProducer.recHitCollectionEE

    process.patElectrons.reducedBarrelRecHitCollection = process.eleNewEnergiesProducer.recHitCollectionEB
    process.patElectrons.reducedEndcapRecHitCollection = process.eleNewEnergiesProducer.recHitCollectionEE

for modifier in process.slimmedECALELFElectrons.modifierConfig.modifications:
    modifier.ecalRecHitsEB = process.slimmedECALELFElectrons.reducedBarrelRecHitCollection
    modifier.ecalRecHitsEE = process.slimmedECALELFElectrons.reducedEndcapRecHitCollection

if(options.type=="ALCARECOSIM"):
    process.zNtupleDumper.recHitCollectionES = cms.InputTag("reducedEcalRecHitsES")

############################
## Dump the output Python ##
############################

processDumpFile = open('processDump.py', 'w')
print >> processDumpFile, process.dumpPython()

