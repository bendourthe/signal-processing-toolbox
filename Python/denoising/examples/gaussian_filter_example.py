# LIBRARIES IMPORT

import numpy as np
import matplotlib.pyplot as plt

# DEPENDENCIES

def gaussian_filter(signal, mode=None, sampling_rate=None, fwhm=None, window=None, plotting=None):
    '''
    Applies a Gaussian filter to a denoise time series.
    Input:
        signal: nx1 array corresponding to the tested time series
        mode: select mode to deal with edge effect
            0: set edges to zero
            1: set edges to original signal
            2: set edges to NaN [default]
        sampling_rate: corresponding sampling rate of the time series (i.e. how many frames per seconds, in Hz)
            [default = length(signal)]
        fwhm: full-width at half maximum, key variable defining Gaussian filter
            [default = 25]
        window: number of frames used to define the size of the window (e.g. a value of 20 would mean that every data point in the original signal will be replaced with the mean of the 20 data points before and the 20 data points after itself)
            [default = 20]
        plotting: set to 1 if you wish to see the resulting filtered signal
            [default = 0]
    Output:
        filtered_signal: nx1 array corresponding to the filtered signal
        plot (optional): plots showing (1) the Gaussian with the corresponding full-width at half maximum, and (2) the original and filtered signals
    Dependencies:
        None
    '''

    # Deal with default values and potential missing input variables
    if mode == None:
        mode = 2
    if sampling_rate == None:
        sampling_rate = len(signal)
    if fwhm == None:
        fwhm = 25
    if window == None:
        window = 20
    if plotting == None:
        plotting = 0

    # Define time based on signal length and sampling rate
    time = np.arange(0,(len(signal))/sampling_rate,1/sampling_rate)

    # Define number of frames
    n = len(signal)

    # Generate Gaussian kernel
    #   normalized time vector in ms
    gtime = 1000*np.arange(-window, window)/sampling_rate
    #   generate Gaussian window
    gauswin = np.exp(-(4*np.log(2)*gtime**2)/fwhm**2)
    #   compute empirical full-width half-maximum
    pstPeakHalf = window + np.argmin((gauswin[window:]-.5)**2)
    prePeakHalf = np.argmin((gauswin-.5)**2)
    empFWHM = gtime[pstPeakHalf] - gtime[prePeakHalf]
    #   normalize Gaussian to unit energy
    gauswinN = gauswin / np.sum(gauswin)

    # Initialize filtered signal
    if mode == 0:
        filtered_signal = np.zeros(np.shape(signal))
    elif mode == 1:
        filtered_signal = signal
    elif mode == 2:
        filtered_signal = np.empty(len(signal))
        filtered_signal[:] = np.nan

    # Apply Gaussian moving average filter with selected window
    for i in range(window+1,n-window-1):
        # each point is the weighted average of surrounding points (i.e. window length before and after)
        filtered_signal[i] = np.sum(signal[i-window:i+window]*gauswinN)

    # Plotting
    if plotting == 1:
        # plot Gaussian
        plt.plot(gtime, gauswin, 'ko-', label='Gaussian')
        plt.plot([gtime[prePeakHalf], gtime[pstPeakHalf]], [gauswin[prePeakHalf], gauswin[pstPeakHalf]], 'm', label='full-width half maximum')
        plt.legend()
        plt.title('Gaussian kernel representation')
        plt.show()
        # plot original and filtered signals
        plt.plot(time, signal, label='Original signal')
        plt.plot(time, filtered_signal, label='Gaussian-filtered')
        plt.xlabel('Time [sec]')
        plt.ylabel('Amplitude')
        plt.legend()
        plt.title('Gaussian smoothing filter')
        plt.show()

    return filtered_signal

# APPLICATION

# Generate a random signal
sampling_rate = 1000 # Hz
time = np.arange(0,3,1/sampling_rate)
n = len(time)
p = 15 # poles for random interpolation

# Define noise level (measured in standard deviations)
noiseamp = 5

# Define amplitude modulator and noise level
ampl = np.interp(np.linspace(1,p,n),np.arange(0,p),np.random.rand(p)*30)
noise = noiseamp * np.random.randn(n)
signal = ampl + noise

# Apply a moving average filter
#   settings
fwhm = 25
window = 100
plotting = 1
#   function
filtered_signal = gaussian_filter(signal, sampling_rate=sampling_rate, fwhm=fwhm, window=window, plotting=plotting)
