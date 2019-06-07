# LIBRARIES IMPORT

import numpy as np
import matplotlib.pyplot as plt

# DEPENDENCIES

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

# APPLICATION

# Generate random signal

#   create event (derivative of Gaussian)
dur = 100 # duration of event in time points
event = np.diff(np.exp(-np.linspace(-2,2,dur+1)**2))
event = event/np.max(event) # normalize to max=1

#   define onset times
num_events = 30
onset = np.random.permutation(10000-dur)
onset = onset[0:num_events]

#   generate events
signal = np.zeros(10000)
for i in range(0,num_events):
    signal[onset[i]:onset[i]+dur] = event

#   add noise
signal = signal + .5*np.random.randn(len(signal))

# Restructure data into matrix and calculate average
#   settings
plotting = 1
#   function
data_matrix = average_rep_events(signal, dur, onset, plotting=plotting)

# Plotting
#   original signal
plt.subplot(212)
plt.plot(signal)
plt.xlabel('Time [sec]')
plt.ylabel('Amplitude')
plt.title('Original signal')
#   random single event
plt.subplot(221)
plt.plot(range(0,dur), signal[onset[3]:onset[3]+dur], label='Averaged')
plt.plot(range(0,dur), event, label='Ground-truth')
plt.xlabel('Time [sec]')
plt.ylabel('Amplitude')
plt.legend()
plt.title('Random event')
#   original event with calculated average
plt.subplot(222)
plt.plot(range(0,dur), np.mean(data_matrix, axis=0), label='Averaged')
plt.plot(range(0,dur), event, label='Ground-truth')
plt.xlabel('Time [sec]')
plt.ylabel('Amplitude')
plt.legend()
plt.title('Averaged events')
plt.show()
