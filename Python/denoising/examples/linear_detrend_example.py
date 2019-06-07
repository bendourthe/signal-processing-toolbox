# LIBRARIES IMPORT

import numpy as np
import scipy.signal
import matplotlib.pyplot as plt

# DEPENDENCIES

def linear_detrend(signal, plotting=None):
    '''
    Applies the detrend function to remove the linear trend from a time series.
        Note: added option to plot original and filtered signals.
    Input:
        signal: nx1 array corresponding to the tested time series
        plotting: set to 1 if you wish to see the resulting filtered signal
        [default = 0]
    Output:
        filtered_signal: nx1 array corresponding to the filtered time series
        plot (optional): plot showing the original and filtered signals
    Dependencies:
        None
    '''

    # Deal with default values and potential missing input variables
    if plotting == None:
        plotting = 0

    # Remove linear trend using detrend function
    filtered_signal = scipy.signal.detrend(signal)

    # Plotting
    if plotting == 1:
        plt.plot(range(0,n), signal, label='Original (mean=%d' %np.nanmean(signal) + ')')
        plt.plot(range(0,n), filtered_signal, label='Detrended (mean=%d' %np.nanmean(filtered_signal) + ')')
        plt.xlabel('Time [sec]')
        plt.ylabel('Amplitude')
        plt.legend()
        plt.title('Linear detrending filter')
        plt.show()

# APPLICATION

# General random signal with linear trend
n = 2000
signal = np.cumsum(np.random.randn(n)) + np.linspace(-30,30,n)

# Apply linear detrending filter
#   settings
plotting = 1
#   function
filtered_signal = linear_detrend(signal, plotting)
