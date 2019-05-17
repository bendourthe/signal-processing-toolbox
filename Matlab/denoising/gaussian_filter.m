function filtered_signal = gaussian_filter(signal, mode, sampling_rate, fwhm, window, plotting)
%% DESCRIPTION
%
%   Applies a Gaussian filter to a denoise time series.
%
%   Input
%       signal: nx1 array corresponding to the tested time series
%       mode: select mode to deal with edge effect
%           0: set edges to zero
%           1: set edges to original signal
%           2: set edges to NaN
%       sampling_rate: corresponding sampling rate of the time series (i.e.
%           how many frames per seconds, in Hz)
%       fwhm: full-width at half maximum, key variable defining Gaussian
%           filter
%       window: number of frames used to define the size of the window
%           (e.g. a value of 20 would mean that every data point in the
%           original signal will be replaced with the mean of the 20 data
%           points and 20 data points after itself)
%       plot: set to 1 if you wish to see the resulting filtered signal
%
%   Output
%       filtered_signal: nx1 array corresponding to the filtered time
%           series
%       plot (optional): plot showing the original and filtered signals
%           along with the corresponding window size

%% FUNCTION

% Define time based on signal length and sampling rate
time = 0:1/sampling_rate:(length(signal)-1)/sampling_rate;

% Define number of frames
n = length(time);

% Generate Gaussian kernel

%   full-width half-maximum
fwhm = 25; % in ms

%   normalized time vector in ms
gtime = 1000*(-window:window)/sampling_rate;

%   generate Gaussian window
gauswin = exp(-(4*log(2)*gtime.^2) / fwhm^2);

%   compute empirical full-width half-maximum
pstPeakHalf = window+dsearchn(gauswin(window+1:end)',.5);
prePeakHalf = dsearchn(gauswin(1:window)',.5);

empFWHM = gtime(pstPeakHalf) - gtime(prePeakHalf);

%   normalize Gaussian to unit energy
gauswin = gauswin / sum(gauswin);
title([ 'Gaussian kernel with requeted FWHM ' num2str(fwhm) ' ms (' num2str(empFWHM) ' ms achieved)' ])
xlabel('Time (ms)'), ylabel('Gain')

% Initialize filtered signal vector
if mode == 0
    filtered_signal = zeros(size(signal));
elseif mode == 1
    filtered_signal = signal;
elseif mode == 2
    filtered_signal = NaN(length(signal));
end

% Apply Gaussian moving average filter with selected window
for i=window+1:n-window-1
    % each point is the weighted average of k surrounding points
    filtered_signal(i) = sum(signal(i-window:i+window).*gauswin);
end

% Plotting
if plotting == 1
    % plot Gaussian
    fig = figure;
    fig.Color = 'w';    % set background color to white
    clf, hold on
    plot(gtime, gauswin, 'ko-', 'markerfacecolor', 'w', 'linew', 2)
    hold on
    plot(gtime([prePeakHalf pstPeakHalf]), gauswin([prePeakHalf pstPeakHalf]), 'm', 'linew', 2)
    legend({'Gaussian';'full-width half maximum'})
    title('Gaussian filter representation')

    fig2 = figure;
    fig2.Color = 'w';
    clf, hold on
    plot(time, signal)
    plot(time, filtered_signal, 'linew', 2)

    xlabel('Time [sec]'), ylabel('Amplitude')
    legend({'Original signal';'Gaussian-filtered'})
    title('Gaussian smoothing filter')
else
end