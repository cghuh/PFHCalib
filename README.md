# PFHadronCalbration_HLT

How to use (examples)

## Recipe
    cmsrel CMSSW_11_1_0_pre6
    cd CMSSW_11_1_0_pre6/src/
    cmsenv
    follow this recipe for CMSSW_11_1_0_pre6 case : https://github.com/missirol/JMETriggerAnalysis/tree/e1c2765e2719678273afe4a6259bfa99dad51691#setup
    git clone https://github.com/cghuh/PFHCalib.git
    fix the FastSimulation/Event/src/KineParticleFilter.cc
        return vertex.Perp2() < vertexRMax2 && fabs(vertex.Z()) < vertexZMax;
        -> return true;
    scram b -j4
    cd PFHCalib/PFHadHLT/python
    cmsRun PFHadCalib_cfg.py
