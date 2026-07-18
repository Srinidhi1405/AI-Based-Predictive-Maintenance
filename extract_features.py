from scipy.io import loadmat
import numpy as np
from scipy.stats import kurtosis, skew

files = {
    "Healthy": ("dataset/healthy/Normal_0.mat", "X097_DE_time"),
    "Inner Race": ("dataset/Inner_Race/IR007_0.mat", "X105_DE_time"),
    "Ball": ("dataset/Ball/B007_0.mat", "X118_DE_time"),
    "Outer Race": ("dataset/Outer_Race/OR007@6_0.mat", "X130_DE_time"),
}

print(f"{'Class':15} {'Mean':>10} {'Std':>10} {'RMS':>10} {'Peak':>10} {'Kurtosis':>12}")

for label, (path, variable) in files.items():
    data = loadmat(path)
    signal = data[variable].flatten()

    mean = np.mean(signal)
    std = np.std(signal)
    rms = np.sqrt(np.mean(signal**2))
    peak = np.max(np.abs(signal))
    kurt = kurtosis(signal)

    print(f"{label:15} {mean:10.5f} {std:10.5f} {rms:10.5f} {peak:10.5f} {kurt:12.5f}")