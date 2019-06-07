# LIBRARIES IMPORT

import numpy as np
import copy
import matplotlib.pyplot as plt

# FUNCTION

def moving_average(signal, mode=None, sampling_rate=None, window=None, plotting=None):
    '''
    Applies a Median filter to a denoise time series (especially to remove spikes).
        Note: for the manual threshold selection, look at the histogram and select a point located right from the largest concentration of points.
    Input:
        signal: nx1 array corresponding to the tested time series
        mode: select mode to deal with edge effect
            0: set edges to zero
            1: set edges to original signal
            2: set edges to NaN [default]
        sampling_rate: corresponding sampling rate of the time series (i.e. how many frames per seconds, in Hz) [default = len(signal)]
        window: number of frames used to define the size of the window (e.g. a value of 20 would mean that every data point in the original signal will be replaced with the mean of the 20 data points before and the 20 data points after itself) [default = 20]
        plotting: set to 1 if you wish to see the resulting filtered signal [default = 0]
    Output:
        filtered_signal: nx1 array corresponding to the filtered signal
        plot (optional): plot showing the original and filtered signals along with the corresponding window size
    Dependencies:
        None
    '''

    # Deal with default values and potential missing input variables
    if mode == None:
        mode = 2
    if sampling_rate == None:
        sampling_rate = len(signal)
    if window == None:
        window = 20
    if plotting == None:
        plotting = 0

    # Define time based on signal length and sampling rate
    time = np.arange(0, (len(signal))/sampling_rate, 1/sampling_rate)

    # Define number of frames
    n = len(time)

    # Initialize filtered signal vector
    if mode == 0:
        filtered_signal = np.zeros(np.shape(signal))
    elif mode == 1:
        filtered_signal = copy.deepcopy(signal)
    elif mode == 2:
        filtered_signal = np.empty(len(signal))
        filtered_signal[:] = np.nan

    # Apply moving average filter with selected window
    for i in range(window+1,n-window-1):
        # each point is the average of surrounding points (within window)
        filtered_signal[i] = np.mean(signal[i-window:i+window])

    # Plotting
    if plotting == 1:
        # compute window size in ms
        window_size = 1000*(window*2+1)/sampling_rate
        # plot the original and filtered signals
        plt.plot(time, signal, label='Original')
        plt.plot(time, filtered_signal, label='Moving average')
        plt.xlabel('Time [sec]')
        plt.ylabel('Amplitude')
        plt.title('Moving average filter with a window size of ' + str(int(window_size)) + '-ms')
        plt.show()

    return filtered_signal
