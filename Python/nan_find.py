# LIBRARIES IMPORT

import numpy as np

# FUNCTION

def nan_find(y):
    '''
    Generates a NaNs logical array where the indices of each NaN observation is True.
    Generates a local function that can extract the indices of each NaN observation as a list.
    Input:
        - y: nx1 array that contains NaNs
    Output:
        - nan_logic: logical array where the indices of each NaN observation is True
        - find_true: function that returns the indices of all True observations in an array.
    Example:
        nan_logic, find_true = nan_find(y)
        find_true(nan_logic) -> returns array with indices of all NaN in y
        find_true(~nan_logic) -> returns array with indices of all non-NaN in y
    '''
    nan_logic = np.isnan(y)
    # lambda k: k.nonzero()[0] defines the function find_true, and k represents the corresponding input
    find_true = lambda k: k.nonzero()[0]

    return nan_logic, find_true
