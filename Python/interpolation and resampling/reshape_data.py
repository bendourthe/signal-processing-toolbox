# LIBRARIES IMPORT

import numpy as np
from scipy import interpolate               # for interpolation

# FUNCTION

def reshape_data(data, reshape_length):
    '''
    Reshape a data set to a specified length.
        If reshape length > original length, then data set will be upsampled using a cubic spline fit.
        If reshape length < original length, then data set will be downsampled by selecting data point along original signal(s).
    Input:
        data: nxm array -> original data set (n=number of observation, length | m: number of variables)
        reshape_length: desired number of observations (i.e. new data length)
    Output:
        reshaped_data: reshape_lengthxm array containing the reshaped data set
        reshape_idx: reshape_lengthx1 array containing the index of the observations that will be maintained in the reshaped signal (equally distributed)
    '''

    #   Calculate original data length
    original_length = len(data)
    #   Upsample (increase signal length by adding additional data points along a fitting spline)
    if original_length < reshape_length:
        reshaped_data = np.zeros(reshape_length)
        reshape_idx = range(0, reshape_length)
        for i in range(0,np.shape(data)[1]):
            #   Find the equation of the cubic spline that best fits time series
            if len(np.arange(0, reshape_length, reshape_length/original_length)) > len(data[:,i]):
                cs = interpolate.CubicSpline(np.arange(0, reshape_length-reshape_length/original_length, reshape_length/original_length), data[:,i])
            else:
                cs = interpolate.CubicSpline(np.arange(0, reshape_length, reshape_length/original_length), data[:,i])
            #   Apply cubic spline equation to obtained resampled time series
            y_resampled = cs(range(0,reshape_length))
            #   Add current resampled vector to resampled array
            reshaped_data = np.vstack([reshaped_data, y_resampled])
        #   Remove first row of zeros
        reshaped_data = reshaped_data[1:,:]
        #   Transpose array to match with usual format (row = observation, column = variable)
        reshaped_data = np.transpose(reshaped_data)
    #   Downsample (decrease signal length by selected equally spaced data points along the original signal)
    else:
        #   Calculated space between observations in the reshaped signal
        spacing = int(original_length/reshape_length)
        #   Generate new index array with index distribution based on the desired reshape length
        reshape_idx = range(0, reshape_length*spacing, spacing)
        #   Generate reshaped data set
        if data.ndim == 1:
            reshaped_data = data[reshape_idx]
        else:
            reshaped_data = data[reshape_idx,:]

    return reshaped_data, reshape_idx
