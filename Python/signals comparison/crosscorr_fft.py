# LIBRARIES IMPORT

import numpy as np
from numpy.fft import fft, ifft, fft2, ifft2, fftshift

# FUNCTION

def crosscorr_fft(x, y):
    '''
    Calculate the time shift between 2 signals using a Fast Fourier Transform (FFT).
    Input:
        x: nx1 array corresponding to the amplitude vector defining time series #1
        y: nx1 array corresponding to the amplitude vector defining time series #2
    Output:
        time_shift: time shift for every observation (time series)
    Dependencies:
        None
    '''
    # Compute FFT of both signals
    f1 = fft(x)
    f2 = fft(np.flipud(y))
    # Isolate real part of the convolution of f1 and f2
    cc = np.real(ifft(f1 * f2))
    # Return time shift for every observation
    time_shift = fftshift(cc)

    return time_shift
