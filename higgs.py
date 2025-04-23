import uproot
import awkward as ak
import matplotlib.pyplot as plt

# Path to your NanoAOD file (via XRootD)
file_path = "root://cmsxrootd.fnal.gov//store/mc/Run3Summer22NanoAODv12/GluGluHtoZZto4L_M-125_TuneCP5_13p6TeV_powheg2-JHUGenV752-pythia8/NANOAODSIM/130X_mcRun3_2022_realistic_v5-v2/30000/542e888a-24b0-4e51-a494-d2690f894c0d.root"

# Open the file and access the "Events" tree
with uproot.open(file_path) as file:
    tree = file["Events"]
    muon_pt = tree["Muon_pt"].array()

# Flatten the awkward array for plotting
pt_flat = ak.flatten(muon_pt)

# Plotting
plt.hist(pt_flat, bins=50, range=(0, 100), histtype='step', color='blue')
plt.xlabel("Muon $p_T$ [GeV]")
plt.ylabel("Entries")
plt.title("Muon Transverse Momentum")
plt.grid(True)
plt.show()
