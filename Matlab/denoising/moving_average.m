function filtered_signal = moving_average(signal, mode, sampling_rate, window, plotting)
%% DESCRIPTION
%
%   Applies a moving average filter to denoise a time series.
%
%   Input
%       signal: nx1 array corresponding to the tested time series
%       mode: select mode to deal with edge effect
%           0: set edges to zero
%           1: set edges to original signal
%           2: set edges to NaN [default]
%       sampling_rate: corresponding sampling rate of the time series (i.e.
%           how many frames per seconds, in Hz) [default = length(signal)]
%       window: number of frames used to define the size of the window
%           (e.g. a value of 20 would mean that every data point in the
%           original signal will be replaced with the mean of the 20 data
%           points before and the 20 data points after itself)
%           [default = 20]
%       plotting: set to 1 if you wish to see the resulting filtered signal
%           [default = 0]
%
%   Output
%       filtered_signal: nx1 array corresponding to the filtered signal
%       plot (optional): plot showing the original and filtered signals
%           along with the corresponding window size

%% FUNCTION

% Deal with default values and potential missing input variables
switch nargin
    case 1
        mode = 2;
        sampling_rate = length(signal);
        window = 20;
        plotting = 0;
    case 2
        sampling_rate = length(signal);
        window = 20;
        plotting = 0;
    case 3
        window = 20;
        plotting = 0;
    case 4
        plotting = 0;
end

% Define time based on signal length and sampling rate
time = 0:1/sampling_rate:(length(signal)-1)/sampling_rate;

% Define number of frames
n = length(time);

% Initialize filtered signal vector
if mode == 0
    filtered_signal = zeros(size(signal));
elseif mode == 1
    filtered_signal = signal;
elseif mode == 2
    filtered_signal = NaN(size(signal));
end

% Apply moving average filter with selected window
for i=window+1:n-window-1
    % each point is the average of surrounding points (within window)
    filtered_signal(i) = mean(signal(i-window:i+window));
end

% Plotting
if plotting == 1
    % compute window size in ms
    window_size = 1000*(window*2+1)/sampling_rate;

    % plot the original and filtered signals
    fig = figure;
    fig.Color = 'w';    % set background color to white
    clf, hold on
    plot(time, signal)
    plot(time, filtered_signal, 'linew', 1.5)

    % draw a patch to indicate the window size
    tidx = dsearchn(time', 1);
    ylim = get(gca, 'ylim');
    patch(time([tidx-window tidx-window tidx+window tidx+window]), ylim([1 2 2 1]), 'k', 'facealpha', .25, 'linestyle', 'none')
    plot(time([tidx tidx]), ylim,'k--')

    xlabel('Time [sec]'), ylabel('Amplitude')
    title([ 'Moving average filter with a window size of ' num2str(round(window_size)) '-ms' ])
    legend({'Original'; 'Moving aeverage'})
end