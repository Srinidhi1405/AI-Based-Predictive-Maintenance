from scipy.io import loadmat
import numpy as np

# Load healthy data
data = loadmat("dataset/healthy/Normal_0.mat")
signal = data["X097_DE_time"]

# Flatten from (N,1) to (N,)
signal = signal.flatten()

# Calculate RMS
rms = np.sqrt(np.mean(signal**2))

print("RMS =", rms)