# LIBRARIES IMPORT

import numpy as np
import copy
import matplotlib.pyplot as plt

# FUNCTION

def tkeo_zscore(signal, time=None, plotting=None):
    '''
    Applies a Teager-Kaiser Energy-tracking Operator (TKEO) to denoise a time series (e.g. Electromyogram).
    Input:
        signal: nx1 array corresponding to the tested time series
        time: nx1 array corresponding to the time of the tested time series [default = np.arange(0:len(signal))]
        plotting: set to 1 if you wish to see the resulting filtered signal [default = 0]
    Output:
        filtered_signal: nx1 array corresponding to the filtered signal
        signal_zscore: nx1 array corresponding to z-score of the original signal
        filtered_signal_zscore: nx1 array corresponding to z-score of the filtered signal
        plot (optional): plot showing the original and filtered signals along with the corresponding z-scores
    Dependencies:
        None
    '''

    # Deal with default values and potential missing input variables
    if time == None:
        time = np.arange(0:len(signal))
    if plotting == None:
        plotting = 0

    # Initialize filtered signal vector
    filtered_signal = copy.deepcopy(signal)

    # Apply TKEO to original time series
    filtered_signal[1:-1] = signal[1:-1]**2 - signal[0:-2]*signal[2:]

    # Concert original and filtered time series to z-score
    #   find timepoint zero
    time0 = np.argmin(time**2)
    #   convert original time series
    signal_zscore = (signal-np.mean(signal[0:time0])) / np.std(signal[0:time0])
    #  convert filtered time series
    filtered_signal_zscore = (filtered_signal-np.mean(filtered_signal[0:time0])) / std(filtered_signal[0:time0])

    # Plotting
    if plotting == 1:
        # plot original and filtered time series (normalized to max-1)
        plt.plot(time, signal/np.max(signal), label='Original signal')
        plt.plot(time, filtered_signal/np.max(filtered_signal), label='Filtered signal (TKEO)')
        plt.xlabel('Time [ms]')
        plt.ylabel('Amplitude or energy')
        plt.legend()

        plt.show()

        # plot zscored
        plt.plot(time, signal_zscore, label='Original signal')
        plt.plot(time, filtered_signal_zscore, label='Filtered signal (TKEO)')

        plt.xlabel('Time [ms]')
        plt.ylabel('Zscore relative to pre-stimulus')
        plt.legend()
        plt.show()

    return filtered_signal, signal_zscore, filtered_signal_zscore
