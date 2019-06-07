# LIBRARIES IMPORT

import numpy as np
import scipy as sp

from scipy import interpolate

# FUNCTION

def cubic_spline_fill(signal, mode=None):
    '''
    Interpolates missing observations within a time series using a cubic spline.
    Notes:
        Only interpolates time series with NaN (otherwise return original time series)
        Does not interpolate empty time series (returns same empty time series)
    Input:
        signal: nx1 array: tested time series
        mode: select mode to deal with edge effect
            0: set edges to zero
            1: set to edge value
            2: set edges to mean
            3: set edges to NaN [default]
            4: set edges to reflected signal
    Output:
        signal_interp: new nx1 array with interpolated values

    Dependencies:
        nan_find
    '''

    # Deal with default values and potential missing input variables
    if mode == None:
        mode = 3

    # If no missing observation -> return original signal
    if np.shape(np.where(np.isnan(signal) == True))[1] == 0:

        return signal

    # If empty signal -> return original signal
    elif np.shape(np.where(np.isnan(signal) == True))[1] == np.shape(signal)[0]:

        return signal

    else:
        # Define frame vector
        fr = np.arange(0, len(signal))

        # Generate a NaNs logical array where the indices of each NaN observation is True
        nan_logic, find_true = nan_find(signal)

        # Find indices of non-missing observations
        obs = find_true(~nan_logic)

        # Isolate non-missing portion of the signal
        a = fr[obs]
        b = signal[obs]

        # Find equation of the cubic spline that best fits the corresponding signal
        cs = interpolate.CubicSpline(a, b)

        # Initialization
        signal_interp = np.array(np.empty(np.shape(signal)[0]))

        # Apply cubic spline equation to interpolate between edges
        signal_interp[obs[0]:obs[-1]] = cs(fr[obs[0]:obs[-1]])

        # Change edges values to neighboring values to prevent edge effects
        signal_interp[obs[0]] = signal_interp[obs[0]+1]
        signal_interp[obs[-1]] = signal_interp[obs[-1]-1]

        # Deal with edge effects
        if mode == 0:
            signal_interp[0:obs[0]] = 0
            signal_interp[obs[-1]:] = 0
        elif mode == 1:
            signal_interp[0:obs[0]] = signal_interp[obs[0]]
            signal_interp[obs[-1]:] = signal_interp[obs[-1]]
        elif mode == 2:
            signal_interp[0:obs[0]] = np.nanmean(signal)
            signal_interp[obs[-1]:] = np.nanmean(signal)
        elif mode == 3:
            signal_interp[0:obs[0]] = np.nan
            signal_interp[obs[-1]:] = np.nan
        elif mode == 4:
            pre = len(np.arange(fr[0], obs[0]))
            post = len(np.arange(obs[-1], fr[-1]))
            if pre > 0:
                if obs[-1]-obs[0] < pre:
                    signal_interp[obs[0]-(obs[-1]-obs[0]):obs[0]] = np.flip(signal_interp[obs[0]:obs[-1]])
                    signal_interp[0:obs[0]-(obs[-1]-obs[0])] = signal_interp[obs[0]-(obs[-1]-obs[0])+1]
                else:
                    signal_interp[0:obs[0]] = np.flip(signal_interp[obs[0]:obs[0]+pre])
            if post > 0:
                if obs[-1]-post-1 < 0:
                    signal_interp[obs[-1]:2*obs[-1]-obs[0]] = np.flip(signal_interp[obs[0]:obs[-1]])
                    signal_interp[2*obs[-1]-obs[0]:] = signal_interp[2*obs[-1]-obs[0]-1]
                else:
                    signal_interp[obs[-1]:] = np.flip(signal_interp[obs[-1]-post-1:obs[-1]])

        return signal_interp
