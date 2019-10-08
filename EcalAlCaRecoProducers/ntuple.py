from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.workArea = 'prod_ntuples/ALCARERECO/PromptReco2017_103X/DoubleEG-Run2017B-ZSkim-Prompt-v2/298678-299329//pedNoise'
config.General.requestName = 'ALCARERECO'
config.General.transferOutputs = True
config.General.transferLogs = False

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'python/alcaSkimming.py'
config.JobType.outputFiles = ['ntuple.root','eleIDTree.root,eleIDTree.root,extraStudyTree.root,extraCalibTree.root']
config.JobType.pyCfgParams=['type=ALCARERECO','doTree=1','doExtraCalibTree=1','doExtraStudyTree=1','doEleIDTree=1','doTreeOnly=1','isCrab=1','skim=','tagFile=config/reRecoTags/PromptReco2017_103X.py','isPrivate=0','bunchSpacing=0', 'MC=1']

config.Data.inputDataset = '/DoubleEG/Run2017B-EcalUncalZElectron-PromptReco-v2/ALCARECO'
config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.publication = False
#config.Data.outputDatasetTag = 'outputdatasetTag'
#config.Site.storageSite = 'root://eoscms//eos/cms/store' #=> come si scrive su eos??
#config.Site.storageSite = 'srm-eoscms.cern.ch'
config.Site.storageSite = 'T2_CH_CERN'
#config.Site.storageSite = 'T2_IT_Rome'
config.Data.outLFNDirBase = 'group/dpg_ecal/alca_ecalcalib/ecalelf/ntuples/13TeV/ALCARERECO/2018/PromptReco2017_103X/DoubleEG-Run2017B-ZSkim-Prompt-v2/298678-299329/pedNoise/unmerged' 

