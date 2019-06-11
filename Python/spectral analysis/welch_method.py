# LIBRARIES IMPORT

import numpy as np
import scipy.fftpack
import matplotlib.pyplot as plt

# FUNCTION

def welch_method(signal, sampling_rate=None, window=None, overlap=None, plotting=None):
    '''
    Applies Welch's method to a time series for spectral density estimation.
    Input:
        signal: nx1 array corresponding to the tested time series
        sampling_rate: corresponding sampling rate of the time series (i.e. how many frames per seconds, in Hz) [default = len(signal)]
        window: number of frames used to define the size of the window (i.e. how many data points are included in each isolated portion of the original signal) [default = sampling rate]
        overlap: number of frames where two consecutive windows will overlap [default = half of sampling rate]
        plotting: set to 1 if you wish to see the resulting filtered signal [default = 0]
    Output:
        welch_power: corresponding power spectrum using Welch's method
        plot (optional): plots showing (1) defined Hann window and the corresponding edge attenuation on a random sample, and (2) the comparison between the power spectra obtained via Static FFT and Welch's method
    Dependencies:
        None
    '''

    # Deal with default values and potential missing input variables
    if sampling_rate == None:
        sampling_rate = len(signal)
    if window == None:
        window = sampling_rate
    if overlap == None:
        overlap = np.round(sampling_rate/2)
    if plotting == None:
        plotting = 0

    # Define window onset based on selected window and overlap
    onsets = np.arange(0, int(len(signal)-window), int(overlap))

    # Define frequency spectrum as a vector (in Hz)
    freq_spectr = np.linspace(0, sampling_rate/2, int(np.floor(window/2)+1))

    # Define Hann window to minimize edge effects
    # (i.e. filter signal by applying a progressive attenuation around the edges)
    hannw = .5 - np.cos(2*np.pi*np.linspace(0, 1, int(window)))/2

    # Initialize the power matrix (shape: windows x frequencies)
    welch_power = np.zeros(len(freq_spectr))

    # Apply Welch's method to signal
    for i in range(0, len(onsets)):
        # isolate a portion of the original signal
        signal_portion = signal[onsets[i]:onsets[i]+int(window)]
        # apply Hann window to taper signal around edges
        signal_portion = signal_portion * hannw
        # compute power
        power = np.abs(scipy.fftpack.fft(signal_portion)/window)**2
        # enter into matrix
        welch_power = welch_power + power[0:len(freq_spectr)]

    # Divide by number of windows to obtain average
    welch_power = welch_power / len(onsets)

    # Plotting
    if plotting == 1:
        # plot Hann window and random signal portion
        plt.subplot(211)
        plt.plot(hannw)
        plt.xlim(0, len(hannw))
        plt.ylabel('Amplitude')
        plt.title('Hann window')

        plt.subplot(212)
        rand_idx = int((random.randrange(len(onsets))))
        signal_sample = signal[onsets[rand_idx]:onsets[rand_idx]+int(window)]
        plt.plot(signal_sample, label='Original sample')
        plt.plot(signal_sample * hannw, label='Hann')
        plt.xlim(0, len(signal_sample))
        plt.ylabel('Amplitude')
        plt.legend()
        plt.title('Edge effect attenuation using Hann window')

        plt.show()

        # plot Static FFT and Welch's power spectra
        sfft_freq_spectr = np.linspace(0, sampling_rate/2, int(np.floor(len(signal)/2)+1))
        sfft_spectr = np.abs(scipy.fftpack.fft(signal)/len(signal))**2
        plt.plot(sfft_freq_spectr, sfft_spectr[0:len(sfft_freq_spectr)], label='Static FFT')
        plt.plot(freq_spectr, welch_power/10, label="Welch's method")
        plt.xlim([0,40])
        plt.xlabel('Frequency [Hz]')
        plt.legend()
        plt.title('Static FFT vs. Welch''s method')

        plt.show()

    return welch_power
