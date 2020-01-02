# LIBRARIES IMPORT

import numpy as np
from numpy.fft import fft, ifft, fft2, ifft2, fftshift

# FUNCTION

def time_shift_fft(x, y):
    '''
    Calculate the maximal time shift between 2 signals using a Fast Fourier Transform (FFT).
    Input:
        x: nx1 array corresponding to the amplitude vector defining time series #1
        y: nx1 array corresponding to the amplitude vector defining time series #2
    Output:
        max_time_shift: maximal time shift
    Dependencies:
        crosscorr_fft.py
    '''
    # Check that the length of each signal matches
    assert len(x) == len(y)
    # Apply crosscorr_fft to calculate the time shift for each observation
    time_shift = crosscorr_fft(x, y)
    # Check for signal length
    assert len(time_shift) == len(x)
    # Calculate index of maximal shift
    zero_index = int(len(x) / 2) - 1
    # Calculate maximal shift
    max_time_shift = zero_index - np.argmax(time_shift)

    return max_time_shift
