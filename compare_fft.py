from scipy.io import loadmat
import numpy as np
import matplotlib.pyplot as plt

Fs = 12000

files = {
    "Healthy": ("dataset/healthy/Normal_0.mat", "X097_DE_time"),
    "Inner Race": ("dataset/Inner_Race/IR007_0.mat", "X105_DE_time"),
    "Ball": ("dataset/Ball/B007_0.mat", "X118_DE_time"),
    "Outer Race": ("dataset/Outer_Race/OR007@6_0.mat", "X130_DE_time"),
}

plt.figure(figsize=(14,10))

for i, (label, (path, variable)) in enumerate(files.items()):

    data = loadmat(path)

    signal = data[variable].flatten()

    N = len(signal)

    fft = np.fft.fft(signal)

    freq = np.fft.fftfreq(N, 1/Fs)

    magnitude = np.abs(fft)

    plt.subplot(2,2,i+1)

    plt.plot(freq[:N//2], magnitude[:N//2])

    plt.title(label)

    plt.xlabel("Frequency (Hz)")

    plt.ylabel("Amplitude")

    plt.grid()

plt.tight_layout()

plt.show()