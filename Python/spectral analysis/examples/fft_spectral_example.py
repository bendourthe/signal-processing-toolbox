# LIBRARIES IMPORT

import numpy as np
import scipy.fftpack
import matplotlib.pyplot as plt

# DEPENDENCIES

def fft_spectral(signal, sampling_rate=None, plotting=None):
    '''
    Applies a Fast Fourier Transform (FFT) to perform the spectral analysis of a time series.
    Input:
        signal: nx1 array corresponding to the tested time series
        sampling_rate: corresponding sampling rate of the time series (i.e. how many frames per seconds, in Hz) [default = len(signal)]
        plotting: set to 1 if you wish to see the resulting figures [default = 0]
    Output:
        fourier_signal: nx1 array corresponding to the fourier transform of the time series
        amp_spectrum: nx1 array corresponding to amplitude spectrum of the time series (frequency space)
        recon_signal: nx1 array corresponding to the reconstructed signal using the inverse FFT
        plot (optional): plot showing the resulting signal and its inverse reconstruction in time and frequency space
    Dependencies:
        None
    '''

    # Deal with default values and potential missing input variables
    if sampling_rate == None:
        sampling_rate = len(signal)
    if plotting == None:
        plotting = 0

    # Define time vector
    time = np.arange(0, len(signal))/sampling_rate

    # Apply static Fast Fourier Transform to signal
    fourier_signal = scipy.fftpack.fft(signal)

    # Calculate corresponding amplitude spectrum
    amp_spectrum = 2*np.abs(fourier_signal)/len(signal)

    # Define frequency spectrum as a vector (in Hz)
    freq_spectr = np.linspace(0, sampling_rate/2, int(np.floor(len(signal)/2)+1))

    # Reconstruct signal using inverse Fast Fourrier Transform
    recon_signal = np.real(scipy.fftpack.ifft(fourier_signal))

    # Plotting
    if plotting == 1:
        plt.plot(time, signal, label='Original')
        plt.plot(time, recon_signal, '+', label='IFFT reconstructed')
        plt.xlabel('Time [sec])')
        plt.ylabel('Amplitude')
        plt.title('Time domain')
        plt.legend()
        plt.show()

        plt.stem(freq_spectr, amp_spectrum[0:len(freq_spectr)], 'k')
        plt.xlabel('Frequency [Hz]')
        plt.ylabel('Amplitude')
        plt.title('Frequency domain')
        plt.show()

    return fourier_signal, amp_spectrum, recon_signal

# APPLICATION

# Generate a multispectral random noisy signal
#   settings
sampling_rate = 1024               # in Hz
duration = 2                       # signal duration (in secs)
num_fr = sampling_rate*duration    # total number of frame for corresponding duration
time = np.arange(0, num_fr)/sampling_rate
freq = [12, 18, 30]                # desired frequencies of sine waves in the signal

#   initialization
signal = np.zeros(num_fr)
#   create signal using sine waves with corresponding frequencies
for i in range(0, len(freq)):
    signal = signal + i*np.sin(2*np.pi*freq[i]*time)

#   add noise
signal = signal + np.random.randn(len(signal))

# Apply FFT to signal
#   settings
plotting = 1
#   function
fourier_signal, amp_spectrum, recon_signal = fft_spectral(signal, sampling_rate=sampling_rate, plotting=plotting)

