import FWCore.ParameterSet.Config as cms

from TopQuarkAnalysis.TopSkimming.TtDecayChannelFilter_cfi import ttDecayChannelFilter

## semi-leptonic-tau decay
ttSemiLeptonicElectronFilter = ttDecayChannelFilter.clone()
ttSemiLeptonicElectronFilter.allowedTopDecays.decayBranchA.electron = True
## semi-leptonic-tau decay
ttSemiLeptonicMuonFilter = ttDecayChannelFilter.clone()
ttSemiLeptonicMuonFilter.allowedTopDecays.decayBranchA.muon = True
## semi-leptonic-tau decay
ttSemiLeptonicTauFilter = ttDecayChannelFilter.clone()
ttSemiLeptonicTauFilter.allowedTopDecays.decayBranchA.tau = True