from scipy.io import loadmat
import numpy as np
import matplotlib.pyplot as plt

# Sampling Frequency
Fs = 12000

# Load signal
data = loadmat("dataset/healthy/Normal_0.mat")

signal = data["X097_DE_time"].flatten()

N = len(signal)

# FFT
fft = np.fft.fft(signal)

# Frequency axis
freq = np.fft.fftfreq(N, d=1/Fs)

# Magnitude
magnitude = np.abs(fft)

plt.figure(figsize=(12,5))

plt.plot(freq[:N//2], magnitude[:N//2])

plt.title("FFT of Healthy Bearing")

plt.xlabel("Frequency (Hz)")

plt.ylabel("Amplitude")

plt.grid()

plt.show()