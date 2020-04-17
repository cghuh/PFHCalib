import FWCore.ParameterSet.Config as cms

process = cms.Process("PFHadCalib")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.load("SimGeneral.HepPDTESSource.pythiapdt_cfi")

#process.load("PFHadHLT.hlt83X_JME_PFHadCal")

#from PFHCalib.PFHadHLT.dump_hlt_SinglePion import *
#from PFHCalib.PFHadHLT.step3_TrackingV2_11_0_0 import *
from JMETriggerAnalysis.NTuplizers.hltPhase2_TRKv02_cfg import *
from JMETriggerAnalysis.NTuplizers.tmp import *
#from PFHCalib.PFHadHLT.hltPhase2_TRKv02_cfg import *

#process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(10))

process.source = cms.Source("PoolSource",
 # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(
			#'root://cms-xrd-global.cern.ch//store/mc/Phase2HLTTDRWinter20DIGI/SinglePion_PT0to200/GEN-SIM-DIGI-RAW/NoPU_110X_mcRun4_realistic_v3-v2/50000/92FA6934-111A-F146-AD22-D50BA1BD7519.root'
			#'root://cms-xrd-global.cern.ch//store/mc/Phase2HLTTDRWinter20DIGI/SinglePion_PT0to200/GEN-SIM-DIGI-RAW/NoPU_110X_mcRun4_realistic_v3-v2/50000/75A710FD-7A17-8B48-942F-5DA2C69201DA.root'
			#'root://cms-xrd-global.cern.ch//store/mc/Phase2HLTTDRWinter20DIGI/SinglePion_PT0to200/GEN-SIM-DIGI-RAW/NoPU_110X_mcRun4_realistic_v3-v2/50000/DD6CC8FB-0F46-294B-BB27-7718226B5258.root'
			#'root://cms-xrd-global.cern.ch//store/mc/Phase2HLTTDRWinter20DIGI/SinglePion_PT0to200/GEN-SIM-DIGI-RAW/NoPU_110X_mcRun4_realistic_v3-v2/50000/A41942EF-6E1C-BD4B-A092-40E46C4531C6.root'
			#'root://cms-xrd-global.cern.ch//store/mc/Phase2HLTTDRWinter20DIGI/SinglePion_PT0to200/GEN-SIM-DIGI-RAW/NoPU_110X_mcRun4_realistic_v3-v2/50000/D13D0D95-AE8C-194D-AB2C-90E25417CDA3.root'
			#'root://cms-xrd-global.cern.ch//store/mc/Phase2HLTTDRWinter20DIGI/SinglePion_PT0to200/GEN-SIM-DIGI-RAW/NoPU_110X_mcRun4_realistic_v3-v2/50000/E3B81E3A-9B35-A54B-A6E0-2A4D41CD83A5.root'
			#'root://cms-xrd-global.cern.ch//store/mc/Phase2HLTTDRWinter20DIGI/SinglePion_PT0to200/GEN-SIM-DIGI-RAW/NoPU_110X_mcRun4_realistic_v3-v2/50000/0248A46E-D4D8-514D-A6F9-699E32BDF4B6.root'
      #'file:/afs/cern.ch/work/c/chuh/PFHadCalibration/CMSSW_11_1_0_pre3/src/PFHCalib/PFHadHLT/python/0248A46E-D4D8-514D-A6F9-699E32BDF4B6.root' #single pion
      #'file:/afs/cern.ch/work/c/chuh/PFHadCalibration/CMSSW_11_1_0_pre3/src/PFHCalib/PFHadHLT/python/47425336-6A25-5F47-ADD2-DCB8DDCADA3B.root' #multi pion
      'file:/afs/cern.ch/work/c/chuh/PFHadCalibration/CMSSW_11_1_0_pre3/src/PFHCalib/PFHadHLT/python/33B1D528-C050-F349-91FF-B29E9E111BC9.root' #multi pion
    )
)

process.pfhadhlt = cms.EDAnalyzer('PFHadHLT',
    #src = cms.InputTag("prunedGenParticles"),
    #maxEventsToPrint = cms.untracked.int32(1)
		   #genEvnTag = cms.InputTag("generator"),
		   genParTag        = cms.InputTag("genParticles"),
                   HLTPFCandidates  = cms.InputTag("particleFlowTmp"),
                   #PFSimParticles   = cms.InputTag("simPFProducer"),
                   #HLTPFCandidates  = cms.InputTag("hltParticleFlow","","TEST"),
                   PFSimParticles   = cms.InputTag("particleFlowSimParticle"),

                   ptMin = cms.double(0.01),                     # Minimum pt
                   pMin = cms.double(0.01),                      # Minimum p
                   nPixMin = cms.int32(2),                     # Nb of pixel hits for pion
						 #nPixMin = cms.int32(0),          # Nb of pixel hits for neutron

                   nHitMin = cms.vint32(8, 8, 8, 8),          # Nb of track hits for pion
						 #nHitMin = cms.vint32(0,0,0,0),       # Nb of track hits for neutron

		   nEtaMin = cms.vdouble(1.4, 1.6, 2.0, 2.5),  # in these eta ranges
                   hcalMin = cms.double(0.0),                   # Minimum hcal energy
                   ecalMax = cms.double(1e12),                  # Maximum ecal energy 
                   rootOutputFile = cms.string('PFHadCalibration.root')
)

process.printGenParticleList = cms.EDAnalyzer("ParticleListDrawer",
  maxEventsToPrint = cms.untracked.int32(10),
  printVertex = cms.untracked.bool(False),
  printOnlyHardInteraction = cms.untracked.bool(False), # Print only status=3 particles. This will not work for Pythia8, which does not have any such particles.
  src = cms.InputTag("genParticles")
)


#process.reconstruction += process.simPFProducer
process.reconstruction += process.particleFlowSimParticle

#process.p = cms.Path(process.pfhadhlt)

#process.AOutput = cms.EndPath( process.hltPreAOutput + process.pfhadhlt + process.printGenParticleList)
#process.AOutput = cms.EndPath( process.hltPreAOutput + process.pfhadhlt)
#process.AOutput = cms.EndPath( process.printGenParticleList)
process.AOutput = cms.EndPath( process.pfhadhlt )
process.schedule.extend([process.AOutput])
