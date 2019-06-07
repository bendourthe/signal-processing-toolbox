# LIBRARIES IMPORT

import numpy as np
import scipy as sp

from scipy import interpolate

# FUNCTION

def cubic_spline_resample(time, y, rf):
    '''
    Fits a cubic spline to the data and resamples the corresponding time series to the desired sampling rate.
    Input:
        time: nx1 array corresponding to the time (in secs)
        y: nx1 array: tested time series (e.g. x coordinates of a marker)
        rf: resampling frequency (Hz)
    Output:
        y_resampled: array corresponding to resampled time series
            Note: Keeps the original values of the time series
        time_resampled: array corresponding to resampled time
    '''
    duration = time[-1]
    # calculate number of frames based on total duration and resampling rate
    num_fr = int(np.round(duration * rf, 0))
    if num_fr > len(time):
        # generate an array that contains the indices of all frames included in the original sampling rate
        fr = np.round(time * rf, 0).astype(int)
        # generate an array that contains the indices of all frames after resampling
        fr_resampled = np.arange(0,num_fr+1)
        # find the equation of the cubic spline that best fits time series
        cs = interpolate.CubicSpline(fr, y)
        # generate new time array based on resampling rate
        time_resampled = fr_resampled / rf
        # apply cubic spline equation to obtained resampled time series
        y_resampled = cs(fr_resampled)
        # use original data to fill value that match the original sampling rate
        y_resampled[fr]= y
    else:
        # generate an array that contains the indices of all frames included in the original sampling rate
        _, fr_resampled = np.unique(np.round(time * rf, 0).astype(int), return_index=True)
        time_resampled = time[fr_resampled]
        y_resampled = y[fr_resampled]

    return y_resampled, time_resampled
