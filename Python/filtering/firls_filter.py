# LIBRARIES IMPORT

import numpy as np
import matplotlib.pyplot as plt
import scipy

from scipy import signal

# FUNCTION

def firls_filter(signal, mode=None, sampling_rate=None, cutoff_f=None, order=None, plotting=None):
    '''
    Applies a Finite Impulse Response (FIR) least-square filter to a time series.
        Note: uses firls function.
    Input:
        signal: nx1 array corresponding to the tested time series
        mode: select type of filter
            0: low-pass filter (gets ride of high frequencies) [default]
            1: high-pass filter (gets ride of low frequencies)
        sampling_rate: corresponding sampling rate of the time series (i.e. how many frames per seconds, in Hz) [default = length(signal)]
        cutoff_f: cut-off frequency (frequencies above this value will be filtered) [default (arbitrary) = 30]
        order: define order of the Kernel (higher order will have more time
            points and bring the Actual Kernel closer to the Ideal Kernel, but too high values will also add artifacts)
                [default = 5]
        shape: define shape of the filter Kernel (in frequency space) [default: [1 1 0 0]]
        plotting: set to 1 if you wish to see the resulting Kernel and filtered signal [default = 0]
    Output:
        filtered_signal: nx1 array corresponding to the filtered signal
        plot (optional): plots showing (1) the Kernel (in time and frequency domains), and (2) the original and filtered signals (in time and frequency domains)
    Dependencies:
        None
    '''

    # Deal with default values and potential missing input variables
    if mode == None:
        mode = 0
    if sampling_rate == None:
        sampling_rate = len(signal)
    if cutoff_f == None:
        cutoff_f = 30
    if order == None:
        order = 5
    if plotting == None:
        plotting = 0

    # Define time based on signal length and sampling rate
    time = np.arange(0,(len(signal))/sampling_rate,1/sampling_rate)

    # Define additional kernel parameters
    if mode == 0:
        shape = [1, 1, 0, 0]
    elif mode == 1:
        shape = [0, 0, 1, 1]
    nyquist = sampling_rate/2
    num_points = len(time)
    transw = .1
    order = np.round(order*sampling_rate/cutoff_f)+1
    # order must be odd
    if order%2==0:
        order += 1
    frex = [0, cutoff_f, cutoff_f+cutoff_f*transw, nyquist]

    # Build kernel
    filter_kernel = firls(order, frex, shape, fs=sampling_rate)

    # Compute the power spectrum of the signal and filter kernel
    filter_power = np.abs(sp.fftpack.fft(filter_kernel,num_points))**2

    # Compute the frequency vector and remove negative frequencies
    hz = np.linspace(0, sampling_rate/2, int(np.floor(num_points/2)+1))
    filter_power = filter_power[0:len(hz)]

    # Apply filter to the data
    filtered_signal = filtfilt(filter_kernel, 1, signal)

    # Plotting
    if plotting == 1:
        # plot Kernel (time domain)
        plt.subplot(121)
        plt.plot(np.arange(-order/2,order/2)/sampling_rate, filter_kernel, 'k')
        plt.xlabel('Time [sec]')
        plt.title('Filter Kernel (time domain)')
        # plot Kernel (frequency domain - power spectrum)
        plt.subplot(122)
        plt.plot(np.array(frex), shape, 'r')
        plt.plot(hz, filter_power[:len(hz)], 'k')
        plt.xlim([0, 2*cutoff_f])
        plt.xlabel('Frequency [Hz]')
        plt.ylabel('Gain')
        plt.title('Filter Kernel (frequency domain - power spectrum)')
        plt.show()
        # plot original and filtered signals (time domain)
        plt.subplot(211)
        plt.plot(time, signal, label='Original')
        plt.plot(time, filtered_signal, label='Filtered')
        plt.legend()
        plt.xlabel('Time (sec.)')
        plt.ylabel('Amplitude')
        plt.title('Original vs. Filtered signals (time domain)')
        # plot original and filtered signals (frequency domain - power spectra)
        yOrigX = np.abs(sp.fftpack.fft(signal)/num_points)**2
        yFiltX = np.abs(sp.fftpack.fft(filtered_signal)/num_points)**2
        plt.subplot(212)
        plt.plot(hz, yOrigX[:len(hz)], label='Original')
        plt.plot(hz, yFiltX[:len(hz)], label='Filtered')
        plt.xlim([0, sampling_rate/5])
        plt.yscale('log')
        plt.legend()
        plt.xlabel('Frequency [Hz]')
        plt.ylabel('Power [log]')
        plt.title('Original vs. Filtered signals (frequency domain - power spectra)')
        plt.show()
