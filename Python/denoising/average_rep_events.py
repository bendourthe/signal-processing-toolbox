# LIBRARIES IMPORT

import numpy as np
import matplotlib.pyplot as plt

# FUNCTION

def average_rep_events(signal, dur, onset, plotting=None):
    '''
    Restructures a time series composed of repetitive events into a matrix and calculate the corresponding average.
        Note: this code assumes that each event has a constant duration.
    Input:
        signal: nx1 array corresponding to the tested time series
        dur: duration of each event (in frames)
        onset: mx1 array corresponding to the frame numbers when each event happens (when m = number of events in the signal)
        plotting: set to 1 if you wish to see the resulting resulting restructured matrix [default = 0]
    Output:
        data_matrix: nxm array corresponding to the restructured matrix
        plot (optional): plot showing the restructured matrix
    Dependencies:
        None
    '''
    # Deal with default values and potential missing input variables
    if plotting == None:
        plotting = 0
    # Calculate number of events
    num_events = len(onset)
    # Initialize matrix
    data_matrix = np.zeros((num_events, dur))
    # Restructure data into matrix
    for i in range(0,num_events):
        data_matrix[i,:] = signal[onset[i]:onset[i]+dur]
    # Plotting
    if plotting == 1:
        plt.imshow(data_matrix)
        plt.xlabel('Time [sec]')
        plt.ylabel('Event number')
        plt.title('All events')
        plt.show()

    return data_matrix
