# LIBRARY IMPORT

import numpy as numpy

# FUNCTION

def distj_event_detection(time, signal, side=None, mode=None, plot=None):
    '''
    Detect takeoff and landing during a single-legged distance jump trial.
    Input:
        time: nx1 array: define time series (in secs)
        signal: nx1 array: z-coordinates of the right/left ankle
        side: choose between 'right' and 'left'
        mode: select between 'manual' and 'auto'
        plot: plot the corresponding outcome for verification (if True)
    Output:
        events: 2x1 array including the frame indices of the different events detected (right or left)
    Depenencies:
        moving_average.py
    '''

    #   Manual mode
    if mode == 'manual':

        #       Generate figure for manual selection
        fig = plt.figure()
        fig.canvas.set_window_title(trial + ': ' + side + ' ankle joint (z-axis)')
        fig.suptitle('Select take off and landing\n (in this order)', fontsize=ft_size)
        ax = fig.add_subplot(111)
        ax.plot(signal)
        mng = plt.get_current_fig_manager()
        mng.window.state('zoomed')
        #       Select 1st landing, take off, and 2nd landing (in this order)
        points = plt.ginput(2, show_clicks=True)
        points = np.array(points[:]).astype(int)
        idx = np.round(points[:,0],0)
        plt.close(fig)
        #       Find peaks in negative signal
        peaks,_ = find_peaks(-signal)
        #       Take-off
        # find actual local minima closest to the selected point
        takeoff = np.argmin(signal[idx[0]-10:idx[0]+10]) + idx[0]-10
        #       Landing
        # find actual local minima closest to the selected point
        landing = np.argmin(signal[idx[1]-10:idx[1]+10]) + idx[1]-10
        #       Combine events indices in one array
        events = [takeoff, landing]

    #   Automated mode or hybrid mode
    elif mode == 'auto':

            # signal filtering (to facilitate the location of local min/max)
            signal_avg = moving_average(signal)
            #    Max jump
            maxjump = np.nanargmax(signal)
            #    Peak detection
            raw_peaks,_ = find_peaks(-signal)
            pre_max_peaks,_ = find_peaks(-signal_avg[maxjump-50:maxjump])
            post_max_peaks,_ = find_peaks(-signal_avg[maxjump:maxjump+50])
            #    Take off
            takeoff = raw_peaks[np.argmin(np.abs(raw_peaks - (pre_max_peaks[-1]+maxjump-50) ))]
            #    Landing
            landing = raw_peaks[np.argmin(np.abs(raw_peaks - (post_max_peaks[0]+maxjump) ))]
            #    Combine events indices in one array
            events = [takeoff, landing]

    #   Plotting
    if plot == None:
        pass
    else:
        fig = plt.figure()
        fig.canvas.set_window_title(trial + ': ' + side + ' ankle joint (z-axis)')
        fig.suptitle(trial + ': ' + side + ' ankle joint (z-axis)\n\nIn order: take off and postjump landing', fontsize=ft_size)
        ax = fig.add_subplot(111)
        ax.set_xlabel('TIME [s]', fontsize=ft_size)
        ax.set_ylabel('HEIGHT [m]', fontsize=ft_size)
        ax.plot(time, signal)
        ax.plot(time[R_events], signal[R_events], '+', markersize=15)
        # plot the figure maximizes
        mng = plt.get_current_fig_manager()
        mng.window.state('zoomed')                  # for 'TkAgg' backend
        plt.show()

    return events
