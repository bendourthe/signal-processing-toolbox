# LIBRARIES IMPORT

import numpy as np
import scipy.signal
import matplotlib.pyplot as plt

from scipy import *

# DEPENDENCIES

def poly_detrend(signal, plotting=None):
    '''
    Calculates the optimal Bayes information criterion (BIC), generate the corresponding polynomial fit (order = optimal BIC), and applies a polynomial detrend to denoise a time series.
    Input:
        signal: nx1 array corresponding to the tested time series
        plotting: set to 1 if you wish to see the resulting filtered signal [default = 0]
    Output:
        filtered_signal: nx1 array corresponding to the filtered signal
        plot (optional): plot showing the corresponding BIC evolution and the original and filtered signals
    Dependencies:
        None
    '''

    # Deal with default values and potential missing input variables
    if plotting == None:
        plotting = 0

    # Signal properties
    n = len(signal)
    t = range(0,n)

    # Range of orders
    orders = range(5,40)

    # Calculate corresponding sum of squared errors
    sum_se = np.zeros(len(orders))

    # Loop through orders
    for i in range(0,len(orders)):
        # compute polynomial fitting time series
        yHat = np.polyval(polyfit(t, signal, orders[i]),t)
        # compute corresponding fit of model to data (sum of squared errors)
        sum_se[i] = np.sum((yHat-signal)**2)/n

    # Calculate BIC
    bic = n*np.log(sum_se) + orders*np.log(n)

    # Calculate optimal BIC (i.e. lowest)
    bestP = min(bic)
    idx = np.argmin(bic)

    # Calculate polynomial fit
    poly_coefs = polyfit(t, signal, orders[idx])

    # Calculate estimated data based on coefficients
    yHat = polyval(poly_coefs, t)

    # Calculate detrended filtered signal (i.e. residual)
    filtered_signal = signal - yHat

    # Plotting
    if plotting == 1:
        plt.plot(orders, bic, 'ks-')
        plt.plot(orders[idx], bestP, 'o', markerfacecolor='None', ms=15)
        plt.xlabel('Polynomial order')
        plt.ylabel('BIC')
        plt.title('Bayes information criterion evolution')
        plt.show()

        plt.plot(t, signal, label='Original')
        plt.plot(t, yHat, label='Polynomial fit')
        plt.plot(t, filtered_signal, 'k', label='Filtered')
        plt.xlabel('Time [sec]')
        plt.ylabel('Amplitude')
        plt.legend()
        plt.title('Polynomial fit and detrending for order = ' + str(orders[idx]))
        plt.show()

    return filtered_signal

# APPLICATION

# Generate a random signal with polynomial artifact
n = 10000
t = range(0,n)
k = 10 # number of poles for random amplitudes
slowdrift = np.interp(np.linspace(1,k,n),np.arange(0,k),100*np.random.randn(k))
signal = slowdrift + 20*np.random.randn(n)

# Apply median filter
#   settings
plotting = 1;
#   function
filtered_signal = poly_detrend(signal, plotting=plotting)
