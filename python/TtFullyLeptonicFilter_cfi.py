import FWCore.ParameterSet.Config as cms

from TopQuarkAnalysis.TopSkimming.TtDecayChannelFilter_cfi import ttDecayChannelFilter

## full-leptonic decay
ttFullLeptonicFilter = ttDecayChannelFilter.clone()
ttFullLeptonicFilter.allowedTopDecays.decayBranchA.electron = True
ttFullLeptonicFilter.allowedTopDecays.decayBranchA.muon     = True
ttFullLeptonicFilter.allowedTopDecays.decayBranchB.electron = True
ttFullLeptonicFilter.allowedTopDecays.decayBranchB.muon     = True
ttFullLeptonicFilter.allowedTopDecays.decayBranchA.tau      = True
ttFullLeptonicFilter.allowedTopDecays.decayBranchB.tau      = True

#more di-leptonic filters
ttFullLeptonicEEFilter = ttDecayChannelFilter.clone()
ttFullLeptonicEEFilter.allowedTopDecays.decayBranchA.electron = True
ttFullLeptonicEEFilter.allowedTopDecays.decayBranchB.electron = True

ttFullLeptonicMuMuFilter = ttDecayChannelFilter.clone()
ttFullLeptonicMuMuFilter.allowedTopDecays.decayBranchA.muon = True
ttFullLeptonicMuMuFilter.allowedTopDecays.decayBranchB.muon = True

ttFullLeptonicTauTauFilter = ttDecayChannelFilter.clone()
ttFullLeptonicTauTauFilter.allowedTopDecays.decayBranchA.tau = True
ttFullLeptonicTauTauFilter.allowedTopDecays.decayBranchB.tau = True
#mixed leptons
ttFullLeptonicETauFilter = ttDecayChannelFilter.clone()
ttFullLeptonicETauFilter.allowedTopDecays.decayBranchA.electron = True
ttFullLeptonicETauFilter.allowedTopDecays.decayBranchB.tau = True

ttFullLeptonicEMuFilter = ttDecayChannelFilter.clone()
ttFullLeptonicEMuFilter.allowedTopDecays.decayBranchA.electron = True
ttFullLeptonicEMuFilter.allowedTopDecays.decayBranchB.muon = True
#more di-leptonic filters
ttFullLeptonicMuTauFilter = ttDecayChannelFilter.clone()
ttFullLeptonicMuTauFilter.allowedTopDecays.decayBranchA.muon = True
ttFullLeptonicMuTauFilter.allowedTopDecays.decayBranchB.tau = True