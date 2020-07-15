from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName   = 'MultiPion_PT0to200_PFHadCalib_2020'
config.General.transferLogs = False
config.General.workArea = 'MultiPion'

config.section_("JobType")
config.JobType.pluginName  = 'Analysis'
# Name of the CMSSW configuration file
config.JobType.psetName    = 'PFHadCalib_cfg.py'
config.JobType.outputFiles = ['PFHadCalibration.root']
#config.JobType.numCores = 4
#config.JobType.inputFiles    = ['/d3/scratch/cghuh3811/CMSSW_9_2_14/src/PFHCalib/PFHadHLT/python/HLT_BX25_Feb17_MC.db']
config.JobType.inputFiles    = ['/afs/cern.ch/work/m/missirol/public/phase2/JESC/PhaseIIFall17_V5b_MC.db']
config.JobType.allowUndistributedCMSSW = True
config.JobType.maxMemoryMB = 2500

config.section_("Data")
# This string determines the primary dataset of the newly-produced outputs.
# For instance, this dataset will be named /CrabTestSingleMu/something/USER
#config.Data.inputDataset = ''
config.Data.inputDataset = '/SinglePion_PT0to200/Run3Winter20DRMiniAOD-NoPU_110X_mcRun3_2021_realistic_v6-v3/GEN-SIM-RAW'
#config.Data.inputDataset = '/MultiPion_PT0to200/Phase2HLTTDRWinter20DIGI-NoPU_110X_mcRun4_realistic_v3-v2/GEN-SIM-DIGI-RAW'
#config.Data.inputDataset = '/SinglePion_PT0to200/Phase2HLTTDRWinter20DIGI-NoPU_110X_mcRun4_realistic_v3-v2/GEN-SIM-DIGI-RAW'
#config.Data.splitting = 'Automatic'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.totalUnits = 6429
config.Data.publication = False

#config.Data.outLFNDirBase = '/store/user/chuh/PFHadCalib_2020/MultiPionPT0_200'
config.Data.outLFNDirBase = '/store/user/chuh/PFHadCalib_2020/SinglePionPT0_200'
#config.Data.useParent = True
#config.Data.lumiMask = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/Cert_271036-284044_13TeV_PromptReco_Collisions16_JSON_NoL1T.txt'

# This string is used to construct the output dataset name
#config.Data.publishDataName = 'CRAB3-tutorial'

#config.Data.publication = True
#config.Data.publishDBS = 'phys03'
#config.Data.outputDatasetTag = 'SingleMuon_Run2016H_theNEWjec'

config.section_("Site")
#config.Site.whitelist = ['T2_KR_KNU']
config.Site.storageSite = 'T2_KR_KNU'
#config.Site.blacklist = ['T1_US_FNAL','T2_UK_London_Brunel']

