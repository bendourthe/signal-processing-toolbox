# LIBRARIES IMPORT

import numpy as np
import scipy.fftpack
import matplotlib.pyplot as plt

# FUNCTION

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
        plt.plot(time, recon_signal, m='+', label='IFFT reconstructed')
        plt.xlabel('Time [sec])')
        plt.ylabel('Amplitude')
        plt.title('Time domain')
        plt.legend()
        plt.show()

        plt.stem(freq_spectr, amp_spectrum[0:freq_spectr], 'k')
        plt.xlabel('Frequency [Hz]')
        plt.ylabel('Amplitude')
        plt.title('Frequency domain')
        plt.show()
