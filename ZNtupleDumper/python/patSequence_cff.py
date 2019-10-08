import FWCore.ParameterSet.Config as cms
from TrackingTools.TransientTrack.TransientTrackBuilder_cfi import *
#from Configuration.StandardSequences.MagneticField_cff import *

#------------------------------ pattuple
from Calibration.ZNtupleDumper.elePat_cfi import *
from Calibration.ZNtupleDumper.muonPat_cfi import *
from Calibration.ZNtupleDumper.phoPat_cfi import *
#process.patElectrons.electronSource = cms.InputTag("gedGsfElectrons")
#process.patElectrons.addElectronID = cms.bool(False)
#process.patElectrons.addGenMatch = cms.bool(True)
patElectrons.addGenMatch = cms.bool(False)
#process.patElectrons.pvSrc = cms.InputTag("offlinePrimaryVerticesWithBS")
#print process.patElectrons.reducedBarrelRecHitCollection
    
#------------------------------ new energies
from Calibration.ZNtupleDumper.elenewenergiesproducer_cfi import *

#------------------------------ electronID producer
from Calibration.ZNtupleDumper.phoselectionproducers_cfi import *
from Calibration.ZNtupleDumper.muonselectionproducers_cfi import *

from RecoEgamma.ElectronIdentification.egmGsfElectronIDs_cff import *
egmGsfElectronIDs.physicsObjectSrc = cms.InputTag('patElectrons')


#============================== Adding new energies to patElectrons
# adding new float variables to the patElectron
# this variables are produced with a specific producer: eleNewEnergiesProducer
# the name of the userFloat is equal to the InputTag passed here
# to access the float:
# electron.userFloat("eleNewEnergiesProducer:energySCEleJoshEle")
# electron.userFloat("eleNewEnergiesProducer:energySCEleJoshEle:MVAntuplizer")

# patElectrons.userData.userFloats.src = [
#     cms.InputTag("eleNewEnergiesProducer", "energySCEleMust"),
#     cms.InputTag("eleNewEnergiesProducer", "energySCEleMustVar"),
#     ]


#============================== Adding electron ID to patElectrons
patElectrons.addElectronID=cms.bool(False)
patElectrons.electronIDSources =  cms.PSet()
patElectrons.userData = cms.PSet(
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

electronMatch.src=cms.InputTag('gedGsfElectrons')

#============================== Adding photon ID to patPhotons
patPhotons.addPhotonID=cms.bool(True)
patPhotons.photonIDSources =  cms.PSet(
    # configure many IDs as InputTag <someName> = <someTag> you
    # can comment out those you don't want to save some disk space
    fiducial = cms.InputTag("phoSelectionProducers", "fiducial"),
    loose       = cms.InputTag("phoSelectionProducers", "loose"),
    medium      = cms.InputTag("phoSelectionProducers", "medium"),
    tight      = cms.InputTag("phoSelectionProducers", "tight"),
    loose25nsRun2       = cms.InputTag("phoSelectionProducers", "loose25nsRun2"),
    medium25nsRun2      = cms.InputTag("phoSelectionProducers", "medium25nsRun2"),
    tight25nsRun2      = cms.InputTag("phoSelectionProducers", "tight25nsRun2"),
    )

photonMatch.src=cms.InputTag('gedPhotons')
muonMatch.src=cms.InputTag('muons')


#============================== Slimming electron (not really slimming if alcareco
from PhysicsTools.PatAlgos.slimming.slimmedElectrons_cfi import *
slimmedECALELFElectrons = slimmedElectrons.clone()
slimmedECALELFElectrons.src = cms.InputTag('patElectrons')
slimmedECALELFElectrons.linkToPackedPFCandidates = cms.bool(False)
modPSet =  cms.PSet( modifierName    = cms.string('EGExtraInfoModifierFromFloatValueMaps'),
                     electron_config = cms.PSet( 
        #                  electronSrc = cms.InputTag("slimmedECALELFElectrons","","@skipCurrentProcess"),
        electronSrc = slimmedECALELFElectrons.src,
        energySCEleMust = cms.InputTag("eleNewEnergiesProducer","energySCEleMust"),
        energySCEleMustVar = cms.InputTag("eleNewEnergiesProducer","energySCEleMustVar"),
        energySCElePho = cms.InputTag("eleNewEnergiesProducer","energySCElePho"),
        energySCElePhoVar = cms.InputTag("eleNewEnergiesProducer","energySCElePhoVar"),
        ),
                     photon_config   = cms.PSet( )
                     )

modPSetEleIDFloat =  cms.PSet( 
    modifierName = cms.string('EleIDModifierFromValueMaps'),
    electron_config = cms.PSet( 
        electronSrc = slimmedECALELFElectrons.src,
#        fiducial = cms.InputTag("eleSelectionProducers", "fiducial"),
        ),
    photon_config   = cms.PSet( )
    )

modPSetEleIDBool =  cms.PSet( 
    modifierName = cms.string('EleIDModifierFromBoolValueMaps'),
    electron_config = cms.PSet( 
        electronSrc = slimmedECALELFElectrons.src,
        veto25nsRun22016Moriond  = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-Summer16-80X-V1-veto"),
        loose25nsRun22016Moriond = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-Summer16-80X-V1-loose"),
        medium5nsRun22016Moriond = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-Summer16-80X-V1-medium"),
        tight25nsRun22016Moriond = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-Summer16-80X-V1-tight"),
        veto94XV1Run2017         = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-Fall17-94X-V1-veto"),
        loose94XV1Run2017        = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-Fall17-94X-V1-loose"),
        medium94XV1Run2017       = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-Fall17-94X-V1-medium"),
        tight94XV1Run2017        = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-Fall17-94X-V1-tight"),
        ),
    photon_config   = cms.PSet( )
    )

eleNewEnergiesProducer.recHitCollectionEB = cms.InputTag("alCaIsolatedElectrons", "alCaRecHitsEB")
eleNewEnergiesProducer.recHitCollectionEE = cms.InputTag("alCaIsolatedElectrons", "alCaRecHitsEE")
eleNewEnergiesProducer.recHitCollectionEB = cms.InputTag("alCaIsolatedElectrons", "alcaBarrelHits")
eleNewEnergiesProducer.recHitCollectionEE = cms.InputTag("alCaIsolatedElectrons", "alcaEndcapHits")

#eleRegressionEnergy.recHitCollectionEB = eleNewEnergiesProducer.recHitCollectionEB.value()
#eleRegressionEnergy.recHitCollectionEE = eleNewEnergiesProducer.recHitCollectionEE.value()
#patElectrons.reducedBarrelRecHitCollection = eleNewEnergiesProducer.recHitCollectionEB.value()
#patElectrons.reducedEndcapRecHitCollection = eleNewEnergiesProducer.recHitCollectionEE.value()

slimmedECALELFElectrons.reducedBarrelRecHitCollection = eleNewEnergiesProducer.recHitCollectionEB.value()
slimmedECALELFElectrons.reducedEndcapRecHitCollection = eleNewEnergiesProducer.recHitCollectionEE.value()

modPSetSlewRate = cms.PSet( 
	modifierName    = cms.string('EGSlewRateModifier'),
	ecalRecHitsEB  = slimmedECALELFElectrons.reducedBarrelRecHitCollection, #cms.InputTag("reducedEgamma", "reducedEBRecHits"),
	ecalRecHitsEE  = slimmedECALELFElectrons.reducedEndcapRecHitCollection, #cms.InputTag("reducedEgamma", "reducedEERecHits"),
	electron_config = cms.PSet( 
		electronSrc = slimmedECALELFElectrons.src,
        ),
	photon_config   = cms.PSet( )
)



slimmedECALELFElectrons.modifierConfig  = cms.PSet(
    modifications = cms.VPSet(
        modPSet,
        modPSetEleIDFloat,
        modPSetEleIDBool,
#        modPSetSlewRate
        )
    )

#process.trackerDrivenRemoverSeq: sequence to remove events with trackerDriven electrons
#process.eleSelectionProducers: produces value maps of floats that says if the electron passes the given selection
#process.eleNewEnergiesProducer: produces value maps of floats with the new calculated electron energy
#process.electronMatch: assosiation map of gsfelectron and genparticle
#process.patElectrons: producer of patElectron
#process.zNtupleDumper: dumper of flat tree for MVA energy training (Francesco Micheli)
EIsequence = cms.Sequence(egmGsfElectronIDSequence)
prePatSequence = cms.Sequence()
postPatSequence = cms.Sequence( eleNewEnergiesProducer * slimmedECALELFElectrons )
patTriggerMatchSeq = cms.Sequence( patTrigger * PatElectronTriggerMatchHLTEle_Ele20SC4Mass50v7 * PatElectronsTriggerMatch * patTriggerEvent ) 
patSequence=cms.Sequence( prePatSequence * patElectrons * EIsequence* postPatSequence)




