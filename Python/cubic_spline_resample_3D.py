# LIBRARIES IMPORT

import numpy as np
import scipy as sp

from scipy import interpolate

# FUNCTION

def cubic_spline_resample_3D(time, y, rf):
    '''
    Applies cubic_spline_resample to each dimension of a 3D time series.
    Input:
        time: nx1 array corresponding to the time (in secs)
        y: nx3 array: tested time series (e.g. x coordinates of a marker)
        rf: resampling frequency (Hz)
    Output:
        Y_resampled: array corresponding to resampled time series
            Note: Keeps the original values of the time series
        time_resampled: array corresponding to resampled time
    Dependencies:
        cubic_spline_resample
    '''
    a, time_resampled = cubic_spline_resample(time, y[:,0], rf)
    b, _ = cubic_spline_resample(time, y[:,1], rf)
    c, _ = cubic_spline_resample(time, y[:,2], rf)
    Y_resampled = np.transpose(np.array([a, b, c]))

    return Y_resampled, time_resampled
