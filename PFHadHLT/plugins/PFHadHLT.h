// -*- C++ -*-
//
// Package:    PFHadCalib/PFHadHLT
// Class:      PFHadHLT
// 
/**\class PFHadHLT PFHadHLT.cc PFHadCalib/PFHadHLT/plugins/PFHadHLT.cc
 Description: [one line class summary]
 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Dr. Lee Sehwook
//         Created:  Thu, 26 Mar 2015 07:49:04 GMT
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/Math/interface/LorentzVector.h"
#include "DataFormats/Math/interface/Vector3D.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "DataFormats/HepMCCandidate/interface/GenParticleFwd.h"
#include "SimDataFormats/GeneratorProducts/interface/GenEventInfoProduct.h"

// needed for TFileService
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "CLHEP/Matrix/Vector.h"

/// needed for PFM
#include "DataFormats/ParticleFlowCandidate/interface/PFCandidate.h"
#include "DataFormats/ParticleFlowCandidate/interface/PFCandidateFwd.h"

/// 
#include "DataFormats/ParticleFlowReco/interface/PFSimParticle.h"
#include "DataFormats/ParticleFlowReco/interface/PFSimParticleFwd.h"

/// ROOT
#include "TTree.h"

//
//
// class declaration
//

using namespace std;
using namespace reco;

class PFHadHLT : public edm::EDAnalyzer {

   typedef std::vector<reco::GenParticle> GenParticleCollection;
   typedef std::vector<reco::PFSimParticle> PFSimParticleCollection;
   typedef std::vector<reco::PFCandidate> HltParticleFlow;
   typedef ROOT::Math::LorentzVector<ROOT::Math::PtEtaPhiE4D<double> > TLorentzVector;



   public:
      explicit PFHadHLT(const edm::ParameterSet&);
      ~PFHadHLT();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);


   private:
      virtual void beginJob() override;
      virtual void analyze(const edm::Event&, const edm::EventSetup&) override;
      virtual void endJob() override;

      //virtual void beginRun(edm::Run const&, edm::EventSetup const&) override;
      //virtual void endRun(edm::Run const&, edm::EventSetup const&) override;
      //virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;
      //virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;

      // ----------member data ---------------------------

      /// Input Tags
      //edm::InputTag hltpfcandTag;
      //edm::InputTag PFSimParticlesTag;

      edm::EDGetTokenT<reco::PFCandidateCollection> hltpfcandTag;
      edm::EDGetTokenT<reco::PFSimParticleCollection> PFSimParticlesTag;
      edm::EDGetTokenT<reco::GenParticleCollection> genParInfoTag;


      /// member functions
      void Book_trees();
      void Reset_variables();

      /// Min pt for charged hadrons
      double ptMin_;
          
      /// Min p for charged hadrons
      double pMin_;
      
      /// Min hcal raw energy for charged hadrons
      double hcalMin_;
                    
      /// Max ecal raw energy to define a MIP
      double ecalMax_;
                          
      /// Min number of pixel hits for charged hadrons
      int nPixMin_;
                                
      /// Min number of track hits for charged hadrons
      std::vector<int> nHitMin_;
      std::vector<double> nEtaMin_;
                                        
      // Number of tracks after cuts
      std::vector<unsigned int> nCh;
      std::vector<unsigned int> nEv;
     
      std::string outputfile_; 
      TFile *tf1;
      TTree *s;

      int charge_;
      float true_, p_, ecal_, hcal_, eta_, phi_, ho_;
      float gen_E_, gen_pt_, gen_eta_, gen_phi_;
      std::vector <float> pfcsID;
      std::vector <float> Eecal_;
      std::vector <float> Ehcal_;
      std::vector <float> dr_;
      //float TagPion_Pt, TagPion_Eta, TagPion_Phi, TagPion_E, TagPion_Charge;
      //float ProbePion_Pt, ProbePion_Eta, ProbePion_Phi, ProbePion_E, ProbePion_Charge;
      //float deltaR_pion;

      bool isCharged;
};
