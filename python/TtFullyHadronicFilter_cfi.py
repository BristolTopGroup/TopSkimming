import FWCore.ParameterSet.Config as cms

from TopQuarkAnalysis.TopSkimming.TtDecayChannelFilter_cfi import ttDecayChannelFilter

## fully-hadronic decay
ttFullHadronicFilter = ttDecayChannelFilter.clone()
ttFullHadronicFilter.allowedTopDecays.decayBranchA.electron = False
ttFullHadronicFilter.allowedTopDecays.decayBranchA.muon     = False
ttFullHadronicFilter.allowedTopDecays.decayBranchA.tau      = False
ttFullHadronicFilter.allowedTopDecays.decayBranchB.electron = False
ttFullHadronicFilter.allowedTopDecays.decayBranchB.muon     = False
ttFullHadronicFilter.allowedTopDecays.decayBranchB.tau      = False