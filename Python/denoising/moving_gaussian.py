# LIBRARIES IMPORT

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# FUNCTION

def moving_gaussian(signal, mode=None, window=None, plotting=None):
    '''
    Applies a different moving average filter to a time series (standard and gaussian modes).
    Input:
        signal: (n,) array: tested time series (e.g. x coordinates of a marker)
        mode: select type of moving average ('standard' or 'gaussian' - [default: gaussian])
        window: define the window size (standard mode) or sigma (gaussian mode)
            recommended window sizes: 3, 6, 10, 16, 22, 35 (the bigger the smoother - [default: 3])
            recommended sigma values: 1, 2, 3, 5, 8, 10 (the bigger the smoother - [default: 1])
        plotting: set to 1 if you wish to see the resulting filtered signal [default = 0]
    Output:
        filtered_signal: new (n,) array with filtered time series
        Note: filtered_signal may have less observations around the edge of the data
    '''
    # Deal with default values and potential missing input variables
    if mode == None:
        mode = 'gaussian'
    if window == None:
        if mode == 'standard':
            window = 3
        elif mode == 'gaussian':
            window = 1
    if plotting == None:
        plotting = 0

    if mode == 'standard':
        # Compute mask using standard method
        avg_mask = np.ones(window) / window
    else:
        # Compute window using Gaussian method
        gaussian_function = lambda x, sigma: 1/np.sqrt(2*np.pi*sigma**2) * np.exp(-(x**2)/(2*sigma**2))
        gau_x = np.linspace(-2.7*window, 2.7*window, 6*window)
        avg_mask = gaussian_function(gau_x, window)
    # Compute moving average
    filtered_signal = np.convolve(signal, avg_mask, 'same')

    # Plotting
    if plotting == 1:
        # Define number of frames
        x = np.arange(0,np.shape(signal)[0])
        # Create a figure canvas
        fig, ax = plt.subplots()
        # Plot the original, noisy data
        ax.plot(x, signal, label='Original')
        # Plot the filtered signal
        ax.plot(x, filtered_signal, label='Filtered', color='orange')
        # Add legend to plot
        ax.legend()
        plt.xlabel('Time [sec]')
        plt.ylabel('Amplitude')
        plt.title('Moving gaussian filter')
        plt.show()

    return filtered_signal
