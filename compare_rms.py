from scipy.io import loadmat
import numpy as np

# Dictionary of file paths and variable names
files = {
    "Healthy": ("dataset/healthy/Normal_0.mat", "X097_DE_time"),
    "Inner Race": ("dataset/Inner_Race/IR007_0.mat", "X105_DE_time"),
    "Ball": ("dataset/Ball/B007_0.mat", "X118_DE_time"),
    "Outer Race": ("dataset/Outer_Race/OR007@6_0.mat", "X130_DE_time"),
}

print("-" * 40)
print("RMS Comparison")
print("-" * 40)

for label, (path, variable) in files.items():
    data = loadmat(path)

    signal = data[variable].flatten()

    rms = np.sqrt(np.mean(signal**2))

    print(f"{label:15s}: {rms:.6f}")