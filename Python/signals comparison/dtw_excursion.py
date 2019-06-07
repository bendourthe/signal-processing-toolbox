# LIBRARIES IMPORT

import numpy as np
import matplotlib.pyplot as plt

from scipy.spatial.distance import euclidean
from fastdtw import fastdtw

# FUNCTION

def dtw_excursion(x_series1, y_series1, x_series2, y_series2, plot=None, mode=None):
    '''
    Applies an approximate Dynamic Time Warping (DTW) algorithm [1] to compare two time series and calculate the corresponding mean and standard deviations of the amplitude and temporal excursions.
        Note: the DTW used does not work if time series has infinite or NaN values, therefore, the code will look for NaNs and only keep the non-NaN values.
            [1] provides optimal or near-optimal alignments with an O(N) time and memory complexity, written based on Stan Salvador, and Philip Chan. “FastDTW: Toward accurate dynamic time warping in linear time and space.” Intelligent Data Analysis 11.5 (2007): 561-580.
    Input:
        x_series1: nx1 array corresponding to the time vector defining time series #1
        y_series1: nx1 array corresponding to the amplitude vector defining time series #1
        x_series2: nx1 array corresponding to the time vector defining time series #2
        y_series2: nx1 array corresponding to the amplitude vector defining time series #2
        plot: if set to True will plot the two time series with the corresponding connections resulting from the shortest path calculated by the fast DTW
    Output:
        m_temp_exc: mean temporal excursion
        std_temp_exc: standard deviation of the temporal excursion
        m_amp_exc: mean amplitude excursion
        std_amp_exc: standard deviation of the amplitude excursion
    Dependencies:
        nan_find
    '''
    # Look for potential NaNs (-> dynamic time wrapping doesn't work if time series has infs or NaNs)
    #   generate a NaNs logical array where the indices of each NaN observation is True
    nan_logic1, find_true1 = nan_find(y_series1)
    nan_logic2, find_true2 = nan_find(y_series2)
    #   find indices of non-missing observations
    obs1 = find_true1(~nan_logic1)
    obs2 = find_true2(~nan_logic2)
    # Restructure the data based on non-missing observations
    series1 = np.transpose(np.vstack([x_series1[obs1], y_series1[obs1]]))
    series2 = np.transpose(np.vstack([x_series2[obs2], y_series2[obs2]]))
    # Compute the fast DTW
    distance, path = fastdtw(series1, series2, dist=euclidean)
    path = np.array(path)
    # Compute time excursion
    #   calculate the x-projection of the vector connecting the shortest dtw path between points in both time series
    temp_exc = x_series1[path[0,0]] - x_series2[path[0,1]]
    for i in range(1, len(path)):
        x = x_series1[path[i,0]] - x_series2[path[i,1]]
        temp_exc = np.vstack([temp_exc, x])
    # Compute amplitude excursion
    #   calculate the y-projection of the vector connecting the shortest dtw path between points in both time series
    amp_exc = y_series1[path[0,0]] - y_series2[path[0,1]]
    for i in range(1, len(path)):
        y = y_series1[path[i,0]] - y_series2[path[i,1]]
        amp_exc = np.vstack([amp_exc, y])
    # Compute means and standard deviations
    if mode == 'absolute':
        m_temp_exc = np.nanmean(np.absolute(temp_exc))
        std_temp_exc = np.nanstd(np.absolute(temp_exc))
        m_amp_exc = np.nanmean(np.absolute(amp_exc))
        std_amp_exc = np.nanstd(np.absolute(amp_exc))
    elif mode == None:
        m_temp_exc = np.nanmean(temp_exc)
        std_temp_exc = np.nanstd(temp_exc)
        m_amp_exc = np.nanmean(amp_exc)
        std_amp_exc = np.nanstd(amp_exc)

    # Plotting
    if plot == True:
        fig, ax = plt.subplots()
        ax.plot(x_series1, y_series1, label='Time series 1')
        ax.plot(x_series2, y_series2, label='Time series 2')
        for i in range(0, len(path)):
            x = np.array([x_series1[path[i,0]], x_series2[path[i,1]]])
            y = np.array([y_series1[path[i,0]], y_series2[path[i,1]]])
            ax.plot(x, y, color='green', linewidth=0.25)
        ax.set_xlabel('Time [secs]')
        ax.set_ylabel('Amplitude')
        ax.legend()
        plt.show()

    return m_temp_exc, std_temp_exc, m_amp_exc, std_amp_exc
