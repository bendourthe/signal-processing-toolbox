# LIBRARIeS IMPORT

import numpy as np
import scipy as sp

from scipy import interpolate

# FUNCTION

def cubic_spline_fill_3D(x, y):
    '''
    Applies cubic_spline_fill to each dimension of a 3D time series.
    Input:
        x: nx1 array corresponding to the frames indices
        y: nx3 array: tested time series (e.g. x, y, z coordinates of a marker)
    Output:
        Y_interp: new nx3 array with interpolated values replacing NaNs (only returned if data has NaNs)
    Dependencies:
        nan_find
        cubic_spline_fill
    '''
    a = cubic_spline_fill(x, y[:,0])
    b = cubic_spline_fill(x, y[:,1])
    c = cubic_spline_fill(x, y[:,2])
    Y_interp = np.transpose(np.array([a, b, c]))

    return Y_interp
