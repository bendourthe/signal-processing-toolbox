# LIBRARIES IMPORT

import numpy as np

# FUNCTION

def reshape_data(data, reshape_length):
    '''
    Reshape a data set to a specified length.
    Input:
        data: nxm array -> original data set (n=number of observation, length | m: number of variables)
        reshape_length: desired number of observations (i.e. new data length)
    Output:
        reshaped_data: reshape_lengthxm array containing the reshaped data set
        idx_array: reshape_lengthx1 array containing the index of the observations that will be maintained in the reshaped signal (equally distributed)
    '''

    #   Calculate original data length
    original_length = len(data)
    #   Calculated space between observations in the reshaped signal
    spacing = int(original_length/reshape_length)
    #   Generate new index array with index distribution based on the desired reshape length
    idx_array = range(0, reshape_length*spacing, spacing)
    #   Generate reshaped data set
    reshaped_data = data[idx_array,:]

    return reshaped_data, idx_array
