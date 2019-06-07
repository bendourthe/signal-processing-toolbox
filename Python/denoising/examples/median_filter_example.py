# LIBRARIES IMPORT

import numpy as np
import pylab
import copy
import matplotlib.pyplot as plt

# DEPENDENCIES

def median_filter(signal, window=None, plotting=None):
    '''
    Applies a Median filter to a denoise time series (especially to remove spikes).
        Note: for the manual threshold selection, look at the histogram and select a point located right from the largest concentration of points.
    Input:
        signal: nx1 array corresponding to the tested time series
        window: number of frames used to define the size of the window (e.g. a value of 20 would mean that every data point in the original signal will be replaced with the median of the 20 data points before and the 20 data points after itself) [default = 20]
        plotting: set to 1 if you wish to see the resulting filtered signal [default = 0]
    Output:
        filtered_signal: nx1 array corresponding to the filtered signal
        plot (optional): plot showing the original and filtered signals
    Dependencies:
        None
    '''

    # Deal with default values and potential missing input variables
    if window == None:
        window = 20
    if plotting == None:
        plotting = 0

    # Plot histogram to manually select filter threshold
    fig = pylab.figure(1)
    fig.canvas.set_window_title('Manual threshold selection')
    fig.suptitle('Please select a frame located right from the largest concentration of points', fontsize=12)
    ax = fig.add_subplot(111)
    ax.hist(signal,100)
    selection = np.array(plt.ginput(1))[0]
    threshold = int(selection[0])
    plt.close(fig)

    # Find outliers using threshold
    outliers = np.where(signal>threshold)[0]

    # Initialize filtered signal
    filtered_signal = copy.deepcopy(signal)

    # Loop through outliers and set to the median of the points in the corresponding window
    for i in range(0, len(outliers)):
        # find lower and upper bounds
        low_bound = np.nanmax((0, outliers[i]-window))
        upp_bound = np.nanmin((outliers[i]+window, len(signal)))
        # compute median of surrounding points
        filtered_signal[outliers[i]] = np.median(signal[low_bound:upp_bound])

    # Plotting
    if plotting == 1:
        plt.plot(range(0,n), signal, label='Original signal')
        plt.plot(range(0,n), filtered_signal, label='Median-filtered')
        plt.xlabel('Time [sec]')
        plt.ylabel('Amplitude')
        plt.legend()
        plt.title('Median spike denoising filter')
        plt.show()

    return filtered_signal

# APPLICATION

# Generate a random signal
n = 2000
signal = np.cumsum(np.random.randn(n))

# Define proportion of data points to replace with noise
propnoise = .05

# Find noisy data points
noisepnts = np.random.permutation(n)
noisepnts = noisepnts[0:int(n*propnoise)]

# Generate new signal with noise
signal[noisepnts] = 50+np.random.rand(len(noisepnts))*100

# Apply median filter
#   settings
window = 40
plotting = 1
#   function
filtered_signal = median_filter(signal, window=window, plotting=plotting)
