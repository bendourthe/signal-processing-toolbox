# LIBRARY IMPORT

import numpy as numpy

# FUNCTION

def dvj_event_detection(time, right_signal, left_signal, mode=None, height_threshold_factor=None, manual_window=None, auto_window=None, plot=None):
    '''
    Detect box jump, primary landing, takeoff, maximal jump and secondary landing during a drop vertical jump (DVJ) trial.
    Input:
        time: nx1 array: define time series (in secs)
        right_signal: nx1 array: z-coordinates of the right ankle
        left_signal: nx1 array: z-coordinates of the left ankle
        mode: select between 'manual', 'auto' and 'hybrid'
        height_threshold_factor: select a height threshold factor for the detection of peaks (in %)
                e.g. a value of X means that only peaks that have a y-value of more than X% of the max height of the signal will be found (default: 80% of the max)
        manual_window: select how many frames will be used to detect box jump and landings
                (around the actual selected point, default 5)
        auto_window: select how many frames will be used to detect box jump, landings and take-off (default 50)
        plot: plot the corresponding outcome for verification (if True)
    Output:
        R_events: 5x1 array including the frame indices of the different events detected for the right foot
        L_events: 5x1 array including the frame indices of the different events detected for the left foot
    '''

    #   Default parameters
    if height_threshold_factor == None:
        height_threshold_factor = 80
    if manual_window == None:
        manual_window = 5
    if auto_window == None:
        auto_window = 50

    #   Input signal (i.e. ankle vertical position (z-axis))
    RAJz = right_signal
    LAJz = left_signal

    #   Manual mode
    if mode == 'manual':

        #   Right side
        #       Generate figure for manual selection
        fig = plt.figure()
        fig.canvas.set_window_title(trial + ': Right ankle joint (z-axis)')
        fig.suptitle('Select box jump, primary landing, take off, and secondary landing\n (in this order)', fontsize=ft_size)
        ax = fig.add_subplot(111)
        ax.plot(RAJz)
        mng = plt.get_current_fig_manager()
        mng.window.state('zoomed')
        #       Select 1st landing, take off, and 2nd landing (in this order)
        points = plt.ginput(4, show_clicks=True)
        points = np.array(points[:]).astype(int)
        idx = np.round(points[:,0],0)
        plt.close(fig)
        #       Find peaks in negative signal
        peaks,_ = find_peaks(-RAJz)
        #       Box jump
        # find actual local maxima closest to the selected point
        R_boxjump = np.argmax(RAJz[idx[0]-manual_window:idx[0]+manual_window]) + idx[0]-manual_window
        #       Landings
        # find actual local minima closest to the selected point
        R_landing1 = np.argmin(RAJz[idx[1]-manual_window:idx[1]+manual_window]) + idx[1]-manual_window
        # find actual local minima closest to the selected point
        R_landing2 = np.argmin(RAJz[idx[3]-manual_window:idx[3]+manual_window]) + idx[3]-manual_window
        #       Take-off
        R_takeoff = idx[2]
        #       Max jump
        R_maxjump = np.argmax(RAJz[R_takeoff:R_landing2]) + R_takeoff
        #       Combine events indices in one array
        R_events = [R_boxjump, R_landing1, R_takeoff, R_maxjump, R_landing2]

        #   Left side
        #       Generate figure for manual selection
        fig = plt.figure()
        fig.canvas.set_window_title(trial + ': Left ankle joint (z-axis)')
        fig.suptitle('Select box jump, primary landing, take off, and secondary landing\n (in this order)', fontsize=ft_size)
        ax = fig.add_subplot(111)
        ax.plot(LAJz)
        mng = plt.get_current_fig_manager()
        mng.window.state('zoomed')
        #       Select 1st landing, take off, and 2nd landing (in this order)
        points = plt.ginput(4, show_clicks=True)
        points = np.array(points[:]).astype(int)
        idx = np.round(points[:,0],0)
        plt.close(fig)
        #       Box jump
        # find actual local maxima closest to the selected point
        L_boxjump = np.argmax(LAJz[idx[0]-manual_window:idx[0]+manual_window]) + idx[0]-manual_window
        #       Landings
        # find actual local minima closest to the selected point
        L_landing1 = np.argmin(LAJz[idx[1]-manual_window:idx[1]+manual_window]) + idx[1]-manual_window
        # find actual local minima closest to the selected point
        L_landing2 = np.argmin(LAJz[idx[3]-manual_window:idx[3]+manual_window]) + idx[3]-manual_window
        #       Take-off
        L_takeoff = idx[2]
        #       Max jump
        L_maxjump = np.argmax(LAJz[L_takeoff:L_landing2]) + L_takeoff
        #       Combine events indices in one array
        L_events = [L_boxjump, L_landing1, L_takeoff, L_maxjump, L_landing2]

    #   Automated mode or hybrid mode
    elif mode == 'auto' or 'hybrid':

        #   Right side
        #       Max jump
        # return the indices of the peaks found above a height that is half of the signal's max. Applied on the flipped signal (i.e. time is reversed, going from the end to the beginning of the trial)
        peaks,_ = find_peaks(np.flip(RAJz), height = np.nanmax(RAJz)*height_threshold_factor/100)
        # return index of the first peak, which should be the max jump peak
        R_maxjump = len(RAJz) - peaks[0] - 1
        #       2nd landing
        # return indices of minimal peaks happening after max jump
        post_jump,_ = find_peaks(-RAJz[R_maxjump:R_maxjump+auto_window])
        # return index of first minimal peak happening right after max jump (i.e. 2nd landing)
        R_landing2 = post_jump[0] + R_maxjump
        #       Take-off
        # return indices of minimal peaks happening before max jump
        pre_jump,_ = find_peaks(-RAJz[R_maxjump-auto_window:R_maxjump] - np.nanmin(-RAJz), height=np.nanmax(-RAJz[R_maxjump-auto_window:R_maxjump]-np.nanmin(-RAJz))*height_threshold_factor/100)
        # if hybrid mode selected, select take off location manually
        if mode == 'hybrid':
            # generate figure for manual selection of take off location
            fig = plt.figure()
            fig.canvas.set_window_title(trial + ': Right ankle joint (z-axis): zoomed between 1st landing and max jump height')
            fig.suptitle('HYBRID MODE ACTIVATED\n\nManually select take off location', fontsize=ft_size)
            if data_type == 'Vicon':
                window_premax_plot = int(auto_window*2)
            elif data_type == 'Kinect':
                window_premax_plot = int(auto_window/2)
            ax = fig.add_subplot(111)
            ax.plot(RAJz[R_maxjump-window_premax_plot:R_maxjump])
            mng = plt.get_current_fig_manager()
            mng.window.state('zoomed')
            # select take off
            R_takeoff = plt.ginput(1, show_clicks=True)
            R_takeoff = np.array(R_takeoff[:]).astype(int)
            R_takeoff = int(np.round(R_takeoff[:,0],0) + R_maxjump-window_premax_plot)
            plt.close(fig)
        else:
            # return index of last minimal peak happening right before max jump (i.e. take off)
            R_takeoff = pre_jump[-1] + R_maxjump-auto_window
        #       1st landing
        # return indices of minimal peaks happening before take off
        pre_takeoff,_ = find_peaks(-RAJz[R_takeoff-auto_window:R_takeoff] - np.nanmin(-RAJz), height=np.nanmax(-RAJz[R_takeoff-auto_window:R_takeoff] - np.nanmin(-RAJz))*height_threshold_factor/100)
        # check if any negative peak exists between the currently detected take off and the 30 data points preceeding it
        #   if no: switch to Hybrid mode (i.e. manual selection of take off only, rest remains auto)
        if np.shape(pre_takeoff)[0] == 0:
            print('     Failed to locate take off -> Switched to hybrid mode')
            # generate figure for manual selection
            fig = plt.figure()
            fig.canvas.set_window_title(trial + ': Right ankle joint (z-axis): zoomed between 1st landing and max jump height')
            fig.suptitle('HYBRID MODE ACTIVATED\n\nManually select take off location', fontsize=ft_size)
            ax = fig.add_subplot(111)
            if data_type == 'Vicon':
                window_premax_plot = int(auto_window*2)
            elif data_type == 'Kinect':
                window_premax_plot = int(auto_window/2)
            ax.plot(RAJz[R_maxjump-window_premax_plot:R_maxjump])
            mng = plt.get_current_fig_manager()
            mng.window.state('zoomed')
            # select take off
            R_takeoff = plt.ginput(1, show_clicks=True)
            R_takeoff = np.array(R_takeoff[:]).astype(int)
            R_takeoff = int(np.round(R_takeoff[:,0],0) + R_maxjump-window_premax_plot)
            plt.close(fig)
            # return indices of minimal peaks happening before take off
            pre_takeoff,_ = find_peaks(-RAJz[R_takeoff-auto_window:R_takeoff] - np.nanmin(-RAJz), height=np.nanmax(-RAJz[R_takeoff-auto_window:R_takeoff] - np.nanmin(-RAJz))*height_threshold_factor/100)
            # return index of first minimal peak happening before take off (i.e. should be 1st landing)
            R_landing1 = pre_takeoff[np.argmin(RAJz[pre_takeoff + R_takeoff-auto_window])] + R_takeoff-auto_window
        #   if yes: find the minimal negative peak before take off
        else:
            # return index of first minimal negative peak before take off (i.e. should be 1st landing)
            R_landing1 = pre_takeoff[np.argmin(RAJz[pre_takeoff + R_takeoff-auto_window])] + R_takeoff-auto_window
        #       Box jump
        R_boxjump = np.argmax(RAJz[R_landing1-auto_window:R_landing1]) + R_landing1-auto_window
        #       Combine events indices in one array
        R_events = [R_boxjump, R_landing1, R_takeoff, R_maxjump, R_landing2]

        #   Left side
        #       Max jump
        # return the indices of the peaks found above a height that is half of the signal's max. Applied on the flipped signal (i.e. time is reversed, going from the end to the beginning of the trial)
        peaks,_ = find_peaks(np.flip(LAJz), height = np.nanmax(LAJz)*height_threshold_factor/100)
        # return index of the first peak, which should be the max jump peak
        L_maxjump = len(LAJz) - peaks[0] - 1
        #       2nd landing
        # return indices of minimal peaks happening after max jump
        post_jump,_ = find_peaks(-LAJz[L_maxjump:L_maxjump+auto_window])
        # return index of first minimal peak happening right after max jump (i.e. 2nd landing)
        L_landing2 = post_jump[0] + L_maxjump
        #       Take-off
        # return indices of minimal peaks happening before max jump
        pre_jump,_ = find_peaks(-LAJz[L_maxjump-auto_window:L_maxjump] - np.nanmin(-LAJz), height=np.nanmax(-LAJz[L_maxjump-auto_window:L_maxjump] - np.nanmin(-LAJz))*height_threshold_factor/100)
        if mode == 'hybrid':
            # generate figure for manual selection of take off location
            fig = plt.figure()
            fig.canvas.set_window_title(trial + ': Left ankle joint (z-axis): zoomed between 1st landing and max jump height')
            fig.suptitle('HYBRID MODE ACTIVATED\n\nManually select take off location', fontsize=ft_size)
            if data_type == 'Vicon':
                window_premax_plot = int(auto_window*2)
            elif data_type == 'Kinect':
                window_premax_plot = int(auto_window/2)
            ax = fig.add_subplot(111)
            ax.plot(LAJz[L_maxjump-window_premax_plot:L_maxjump])
            mng = plt.get_current_fig_manager()
            mng.window.state('zoomed')
            # select take off
            L_takeoff = plt.ginput(1, show_clicks=True)
            L_takeoff = np.array(L_takeoff[:]).astype(int)
            L_takeoff = int(np.round(L_takeoff[:,0],0) + L_maxjump-window_premax_plot)
            plt.close(fig)
        else:
            # return index of last minimal peak happening right before max jump (i.e. take off)
            L_takeoff = pre_jump[-1] + L_maxjump-auto_window
        #       1st landing
        # return indices of minimal peaks happening before take off
        pre_takeoff,_ = find_peaks(-LAJz[L_takeoff-auto_window:L_takeoff] - np.nanmin(-LAJz), height=np.nanmax(-LAJz[L_takeoff-auto_window:L_takeoff] - np.nanmin(-LAJz))*height_threshold_factor/100)
        # check if any negative peak exists between the currently detected take off and the 30 data points preceeding it
        #   if no: switch to Hybrid mode (i.e. manual selection of take off only, rest remains auto)
        if np.shape(pre_takeoff)[0] == 0:
            print('     Failed to locate take off -> Switched to hybrid mode')
            # generate figure for manual selection
            fig = plt.figure()
            fig.canvas.set_window_title(trial + ': Left ankle joint (z-axis): zoomed between 1st landing and max jump height')
            fig.suptitle('HYBRID MODE ACTIVATED\n\nManually select take off location', fontsize=ft_size)
            if data_type == 'Vicon':
                window_premax_plot = int(auto_window*2)
            elif data_type == 'Kinect':
                window_premax_plot = int(auto_window/2)
            ax = fig.add_subplot(111)
            ax.plot(LAJz[L_maxjump-window_premax_plot:L_maxjump])
            mng = plt.get_current_fig_manager()
            mng.window.state('zoomed')
            # select take off
            L_takeoff = plt.ginput(1, show_clicks=True)
            L_takeoff = np.array(L_takeoff[:]).astype(int)
            L_takeoff = int(np.round(L_takeoff[:,0],0) + L_maxjump-window_premax_plot)
            plt.close(fig)
            # return indices of minimal peaks happening before take off
            pre_takeoff,_ = find_peaks(-LAJz[L_takeoff-auto_window:L_takeoff] - np.nanmin(-LAJz), height=np.nanmax(-LAJz[L_takeoff-auto_window:L_takeoff] - np.nanmin(-LAJz))*height_threshold_factor/100)
            # return index of first minimal peak happening before take off (i.e. should be 1st landing)
            L_landing1 = pre_takeoff[np.argmin(LAJz[pre_takeoff + L_takeoff-auto_window])] + L_takeoff-auto_window
        #   if yes: find the minimal negative peak before take off
        else:
            # return index of first minimal negative peak before take off (i.e. should be 1st landing)
            L_landing1 = pre_takeoff[np.argmin(LAJz[pre_takeoff + L_takeoff-auto_window])] + L_takeoff-auto_window
        #       Box jump
        L_boxjump = np.argmax(LAJz[L_landing1-auto_window:L_landing1]) + L_landing1-auto_window
        #       Combine events indices in one array
        L_events = [L_boxjump, L_landing1, L_takeoff, L_maxjump, L_landing2]

    #   Plotting
    if plot == None:
        pass
    else:
        #       Right side
        fig = plt.figure()
        fig.canvas.set_window_title(trial + ': Right ankle joint (z-axis)')
        fig.suptitle(trial + ': Right ankle joint (z-axis)\n\nIn order: primary landing, take off, max jump and postjump landing', fontsize=ft_size)
        ax = fig.add_subplot(111)
        ax.set_xlabel('TIME [s]', fontsize=ft_size)
        ax.set_ylabel('HEIGHT [m]', fontsize=ft_size)
        ax.plot(time, RAJz)
        ax.plot(time[R_events], RAJz[R_events], '+', markersize=15)
        # plot the figure maximizes
        mng = plt.get_current_fig_manager()
        mng.window.state('zoomed')                  # for 'TkAgg' backend
        plt.show(block=False)
        #       Left side
        fig = plt.figure()
        fig.canvas.set_window_title(trial + ': Left ankle joint (z-axis)')
        fig.suptitle(trial + ': Left ankle joint (z-axis)\n\nIn order: primary landing, take off, max jump and postjump landing', fontsize=ft_size)
        ax = fig.add_subplot(111)
        ax.set_xlabel('TIME [s]', fontsize=ft_size)
        ax.set_ylabel('HEIGHT [m]', fontsize=ft_size)
        ax.plot(time, LAJz)
        ax.plot(time[L_events], LAJz[L_events], '+', markersize=20)
        # plot the figure maximizes
        mng = plt.get_current_fig_manager()
        mng.window.state('zoomed')                  # for 'TkAgg' backend
        plt.show()

    return R_events, L_events
