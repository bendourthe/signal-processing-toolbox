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
    #   Initialize reshaped data array
    reshaped_data = np.zeros(reshape_length)
    reshape_idx = range(0, reshape_length)
    #   If data has only one column
    if len(np.shape(data)) == 1:
        #   Resampling
        #       Define new indices vector
        reshaped_idx = np.arange(0, reshape_length, reshape_length/original_length)
        #       Find the equation of the cubic spline that best fits time series
        if len(np.arange(0, reshape_length, reshape_length/original_length)) > len(data):
            cs = interpolate.CubicSpline(reshaped_idx[0:len(reshaped_idx)-1], data)
        else:
            cs = interpolate.CubicSpline(reshaped_idx, data)
        #       Apply cubic spline equation to obtained resampled time series
        y_resampled = cs(range(0,reshape_length))
        #   Add current resampled vector to resampled array
        reshaped_data = np.vstack([reshaped_data, y_resampled])
    #   If data has multiple columns
    else:
        for i in range(0, np.shape(data)[1]):
            #   Upsampling
            #       Find the equation of the cubic spline that best fits time series
            if len(np.arange(0, reshape_length, reshape_length/original_length)) > len(data[:,i]):
                cs = interpolate.CubicSpline(np.arange(0, reshape_length-reshape_length/original_length, reshape_length/original_length), data[:,i])
            else:
                cs = interpolate.CubicSpline(np.arange(0, reshape_length, reshape_length/original_length), data[:,i])
            #       Apply cubic spline equation to obtained resampled time series
            y_resampled = cs(range(0,reshape_length))
            #   Add current resampled vector to resampled array
            reshaped_data = np.vstack([reshaped_data, y_resampled])
    #   Remove first row of zeros
    if len(np.shape(data)) == 1:
        reshaped_data = reshaped_data[1:]
    else:
        reshaped_data = reshaped_data[1:,:]
    #   Transpose array to match with usual format (row = observation, column = variable)
    reshaped_data = np.transpose(reshaped_data)
    #   If only one column, ensure to have a consistent output with shape (reshape length,)
    if len(np.shape(reshaped_data)) > 1:
        reshaped_data = reshaped_data[:,0]

    return reshaped_data, reshape_idx
