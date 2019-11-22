# LIBRARY IMPORT

import numpy as numpy

# FUNCTION

def timed_event_detection(time, signal, side=None, mode=None, manual_window=None, auto_window=None, plot=None):
    '''
    Detect the first takeoff during a timed single legged hop trial.
    Input:
        time: nx1 array: define time series (in secs)
        signal: nx1 array: z-coordinates of the right/left ankle
        side: choose between 'right' and 'left'
        mode: select between 'manual' and 'auto'
        manual_window: select how many frames will be used to detect box jump and landings
                (around the actual selected point, default 5)
        auto_window: select how many frames will be used to detect box jump, landings and take-off (default 50)
        plot: plot the corresponding outcome for verification (if True)
    Output:
        events: 2x1 array including the frame indices of the different events detected (right or left)
    Depenencies:
        moving_average.py
    '''

    #   Default parameters
    if manual_window == None:
        manual_window = 5
    if auto_window == None:
        auto_window = 50

    #   Manual mode
    if mode == 'manual':

        #       Generate figure for manual selection
        fig = plt.figure()
        fig.canvas.set_window_title(trial + ': ' + side + ' ankle joint (z-axis)')
        fig.suptitle('Select first take off', fontsize=ft_size)
        ax = fig.add_subplot(111)
        ax.plot(signal)
        mng = plt.get_current_fig_manager()
        mng.window.state('zoomed')
        #       Select 1st landing, take off, and 2nd landing (in this order)
        points = plt.ginput(1, show_clicks=True)
        points = np.array(points[:]).astype(int)
        idx = np.round(points[:,0],0)
        plt.close(fig)
        #       Find peaks in negative signal
        peaks,_ = find_peaks(-signal)
        #       Take-off
        # find actual local minima closest to the selected point
        takeoff = np.argmin(signal[idx[0]-manual_window:idx[0]+manual_window]) + idx[0]-manual_window
        #       Combine events indices in one array
        events = [takeoff]

    #   Automated mode or hybrid mode
    elif mode == 'auto':

            # signal filtering (to facilitate the location of local min/max)
            signal_avg = moving_average(signal)
            #    Max jump
            maxjump = np.nanargmax(signal)
            #    Peak detection
            raw_peaks,_ = find_peaks(-signal)
            pre_max_peaks,_ = find_peaks(-signal_avg[maxjump-auto_window:maxjump])
            post_max_peaks,_ = find_peaks(-signal_avg[maxjump:maxjump+auto_window])
            #    Take off
            takeoff = raw_peaks[np.argmin(np.abs(raw_peaks - (pre_max_peaks[-1]+maxjump-auto_window) ))]
            #    Combine events indices in one array
            events = [takeoff]

    #   Plotting
    if plot == None:
        pass
    else:
        fig = plt.figure()
        fig.canvas.set_window_title(trial + ': ' + side + ' ankle joint (z-axis)')
        fig.suptitle(trial + ': ' + side + ' ankle joint (z-axis)', fontsize=ft_size)
        ax = fig.add_subplot(111)
        ax.set_xlabel('TIME [s]', fontsize=ft_size)
        ax.set_ylabel('HEIGHT [m]', fontsize=ft_size)
        ax.plot(time, signal)
        ax.plot(time[events], signal[events], '+', markersize=15)
        # plot the figure maximizes
        mng = plt.get_current_fig_manager()
        mng.window.state('zoomed')                  # for 'TkAgg' backend
        plt.show()

    return events
