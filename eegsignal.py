import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt

# Simulate EEG Data
fs = 250  # Sampling frequency (Hz)
t = np.arange(0, 10, 1/fs)  # Time vector (10 seconds of data)
# Generate synthetic EEG signal: combination of multiple sine waves
eeg_signal = (np.sin(2 * np.pi * 10 * t) +  # 10 Hz component (alpha band)
              0.5 * np.sin(2 * np.pi * 20 * t) +  # 20 Hz component (beta band)
              0.2 * np.sin(2 * np.pi * 40 * t))  # 40 Hz component (gamma band)
# Add some noise
eeg_signal += np.random.normal(0, 0.5, eeg_signal.shape)
 
# Filter the Signal: Bandpass filter for alpha band (8-12 Hz)
lowcut = 8.0
highcut = 12.0
nyquist = 0.5 * fs
low = lowcut / nyquist
high = highcut / nyquist
b, a = signal.butter(4,[low ,high], btype='band')

# Apply the filter
filtered_signal = signal.filtfilt(b, a, eeg_signal)

# Plot the Raw and Filtered EEG Signals
plt.figure(figsize=(12, 8))
# Raw EEG Signal
plt.subplot(2, 1, 1)
plt.plot(t, eeg_signal, label='Raw EEG Signal')
plt.title('Raw EEG Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()

# Filtered EEG Signal
plt.subplot(2, 1, 2)
plt.plot(t, filtered_signal, label='Filtered EEG Signal (8-12 Hz)', color='orange')
plt.title('Filtered EEG Signal (Alpha Band)')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()

plt.tight_layout()
plt.show()