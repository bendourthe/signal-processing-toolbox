# LIBRARIES IMPORT

import numpy as np
import scipy as sp

from scipy.signal import find_peaks

# FUNCTION

def true_peaks(y, y_filtered, height=None, window=None):
    '''
    Finds peaks within a noisy signal via the corresponding filtered signal (i.e. removes noisy peaks).
    Input:
        y: nx1 array: tested time series (e.g. x coordinates of a marker)
        y_filtered: nx1 array: filtered time series
        height: Required height of peaks. Either a number, None, an array matching x or a 2-element sequence of the former.The first element is always interpreted as the minimal and the second, if supplied, as the maximal required height.
        window: number of data points defining the window size within which the code will look for peaks around the detected peaks within the filtered signal
    Output:
        true_peaks: indices of the peaks within the original signal that are the highest around the filtered peaks
    '''
    if height == None:
        height = int(len(y))
    else:
        # Find peaks in filtered signal
        filtered_peaks,_ = find_peaks(y_filtered, height=height)
        # Find what is the highest peak in the original signal around a window around the filtered peak
        true_peaks = np.zeros(len(filtered_peaks)).astype(int)
        if window == None:
            window = 10
            for i in range(0, len(filtered_peaks)):
                true_peaks[i] = np.argmax(y[filtered_peaks[i]-window:filtered_peaks[i]+window]) + filtered_peaks[i]-window
        else:
            for i in range(0, len(filtered_peaks)):
                true_peaks[i] = np.argmax(y[filtered_peaks[i]-window:filtered_peaks[i]+window]) + filtered_peaks[i]-window

    return true_peaks
