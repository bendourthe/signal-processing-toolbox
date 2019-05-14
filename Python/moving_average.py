# LIBRARIES IMPORT

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# FUNCTION

def moving_average(y, mode=None, window_sigma=None, plot=None):
    '''
    Applies a moving average filter to a time series.
    Input:
        y: (n,) array: tested time series (e.g. x coordinates of a marker)
        mode: select type of moving average ('standard' or 'gaussian' - default: gaussian)
        window_sigma: define the window size (standard mode) or sigma (gaussian mode)
                    recommended window sizes: 3, 6, 10, 16, 22, 35 (the bigger the smoother - default: 3)
                    recommended sigma values: 1, 2, 3, 5, 8, 10 (the bigger the smoother - default: 1)
        plot: plot the original and filtered data if True
    Output:
        y_avg: new (n,) array with filtered time series
        Note: y_avg may have less observations around the edge of the data
    '''
    # If input signal has a (n,1) shape, then change it to (n,)
    if np.shape(y)[1] == 1:
        y = y[:,0]
    if mode == 'standard':
        # Compute mask using standard method
        if window_sigma == None:
            window_sigma = 3
            avg_mask = np.ones(window_sigma) / window_sigma
        else:
            avg_mask = np.ones(window_sigma) / window_sigma
    else:
        # Compute window using Gaussian method
        if window_sigma == None:
            window_sigma = 1
            gaussian_function = lambda x, sigma: 1/np.sqrt(2*np.pi*sigma**2) * np.exp(-(x**2)/(2*sigma**2))
            gau_x = np.linspace(-2.7*window_sigma, 2.7*window_sigma, 6*window_sigma)
            avg_mask = gaussian_function(gau_x, window_sigma)
        else:
            gaussian_function = lambda x, sigma: 1/np.sqrt(2*np.pi*sigma**2) * np.exp(-(x**2)/(2*sigma**2))
            gau_x = np.linspace(-2.7*window_sigma, 2.7*window_sigma, 6*window_sigma)
            avg_mask = gaussian_function(gau_x, window_sigma)
    # Compute moving average
    y_avg = np.convolve(y, avg_mask, 'same')

    # Plotting
    if plot == True:
        # Define number of frames
        x = np.arange(0,np.shape(y)[0])
        # Create a figure canvas
        fig, ax = plt.subplots()
        # Plot the original, noisy data
        ax.plot(x, y, label='Original')
        # Plot the filtered signal
        ax.plot(x, y_avg, label='Filtered', color='orange')
        # Add legend to plot
        ax.legend()
        plt.show()

    return y_avg
