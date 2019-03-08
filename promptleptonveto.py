import ROOT
import numpy as np
import root_numpy as rnp


ROOT.gROOT.SetBatch(1)
ROOT.gStyle.SetOptStat(0)
f = ROOT.TFile("/eos/atlas/atlascerngroupdisk/phys-higgs/HSG3/R21/PAOD_V19/EMTopoJets/2LDF/data/data1516/group.phys-higgs.data15_13TeV.HWW_VeryLooseLH.merge.PAOD_2L.V19.0_FakeWJets_PAOD_2LDF/group.phys-higgs.00282712.r9264_p3083_p3640.16818839.PAOD_2LDF._000048.pool.root")
#just randomly chose a data file (a data file is assumed contain multiple processes so would give us the full range of PromptLeptonVeto)
t = f.Get("CollectionTree")
for lep in ["Electron", "Muon"]:
  plv = rnp.tree2array(t, "HWW%ssAuxDyn.PromptLeptonVeto"%lep)
  hplv = ROOT.TH1F("Prompt%sVeto"%lep, "", 1000, -1, 1)
  [hplv.Fill(float(_[0])) for _ in plv]
  c = ROOT.TCanvas('c', 'c', 800, 600)
  hplv.Draw()
  c.Print("Prompt%sVeto.eps"%lep)
  c.Clear()
