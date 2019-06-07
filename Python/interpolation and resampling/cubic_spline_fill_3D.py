# LIBRARIeS IMPORT

import numpy as np
import scipy as sp

from scipy import interpolate

# FUNCTION

def cubic_spline_fill_3D(data, mode=None):
    '''
    Applies cubic_spline_fill to each dimension of a 3D time series.
    Input:
        data: nx3 array: tested data set containing 3D time series
        mode: select mode to deal with edge effect
            0: set edges to zero
            1: set to edge value
            2: set edges to mean
            3: set edges to NaN [default]
            4: set edges to reflected signal
    Output:
        data_interp: new nx3 array with interpolated values
    Dependencies:
        nan_find
        cubic_spline_fill
    '''

    # Deal with default values and potential missing input variables
    if mode == None:
        mode = 3

    # Apply cubic_spline_fill to each dimension of the 3D data set
    a = cubic_spline_fill(data[:,0], mode=mode)
    b = cubic_spline_fill(data[:,1], mode=mode)
    c = cubic_spline_fill(data[:,2], mode=mode)
    data_interp = np.transpose(np.array([a, b, c]))

    return data_interp
