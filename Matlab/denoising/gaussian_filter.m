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
%           2: set edges to NaN [default]
%       sampling_rate: corresponding sampling rate of the time series (i.e.
%           how many frames per seconds, in Hz) [default = length(signal)]
%       fwhm: full-width at half maximum, key variable defining Gaussian
%           filter [default = 25]
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
%       plot (optional): plots showing (1) the Gaussian with the
%           corresponding full-width at half maximum, and (2) the
%           original and filtered signals

%% FUNCTION

% Deal with default values and potential missing input variables
switch nargin
    case 1
        mode = 2;
        sampling_rate = length(signal);
        fwhm = 25;
        window = 20;
        plotting = 0;
    case 2
        sampling_rate = length(signal);
        fwhm = 25;
        window = 20;
        plotting = 0;
    case 3
        fwhm = 25;
        window = 20;
        plotting = 0;
    case 4
        window = 20;
        plotting = 0;
    case 5
        plotting = 0;
end

% Define time based on signal length and sampling rate
time = 0:1/sampling_rate:(length(signal)-1)/sampling_rate;

% Define number of frames
n = length(time);

% Generate Gaussian kernel

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

% Initialize filtered signal
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
    plot(gtime, gauswin, 'ko-', 'markerfacecolor', 'w', 'linew', 1.5)
    hold on
    plot(gtime([prePeakHalf pstPeakHalf]), gauswin([prePeakHalf pstPeakHalf]), 'm', 'linew', 1.5)
    legend({'Gaussian';'full-width half maximum'})
    title('Gaussian filter representation')

    fig2 = figure;
    fig2.Color = 'w';
    clf, hold on
    plot(time, signal)
    plot(time, filtered_signal, 'linew', 1.5)

    xlabel('Time [sec]'), ylabel('Amplitude')
    legend({'Original signal';'Gaussian-filtered'})
    title('Gaussian smoothing filter')
end