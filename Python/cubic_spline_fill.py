# LIBRARIES IMPORT

import numpy as np
import scipy as sp

from scipy import interpolate

# FUNCTION

def cubic_spline_fill(x, y):
    '''
    Assesses if time series y has missing observations (i.e. NaN).
    If yes, interpolates missing observations using a cubic spline fitted to the data.
    Input:
        x: nx1 array corresponding to the frames indices
        y: nx1 array: tested time series (e.g. x coordinates of a marker)
    Output:
        y_interp: new nx1 array with interpolated values replacing NaNs (only returned if data has NaNs)
        Notes:
            - Only interpolates time series with NaN (otherwise return original time series)
            - Does not interpolate empty time series (returns same empty time series)
            - Does not interpolate the beginning and/or end of the time series if it has missing observations (i.e. only interpolates between edges)
    Dependencies:
        nan_find
    '''
    # if no missing observation, return original signal
    if np.shape(np.where(np.isnan(y) == True))[1] == 0:

        return y

    # if empty observation, return original signal
    elif np.shape(np.where(np.isnan(y) == True))[1] == np.shape(y)[0]:

        return y

    else:
        # generate a NaNs logical array where the indices of each NaN observation is True
        nan_logic, find_true = nan_find(y)
        # find indices of non-missing observations
        obs = find_true(~nan_logic)
        # isolate non-missing portion of the signal
        a = x[obs]
        b = y[obs]
        # find the equation of the cubic spline that best fits the corresponding signal
        cs = interpolate.CubicSpline(a, b)
        # initiate y_interp as an empty array
        y_interp = np.array(np.empty(np.shape(y)[0]))
        # fill y_interp with NaNs
        y_interp[:] = np.nan
        # apply cubic spline equation to interpolate the whole signal (- missing observations at edges)
        y_interp[obs[0]:obs[-1]] = cs(x[obs[0]:obs[-1]])
        # to avoid unstable edges, NaNs are applied to the two data points at the two edges of the signal
        y_interp[obs[0]] = np.nan
        y_interp[obs[-1]] = np.nan

        return y_interp
