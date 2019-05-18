function filtered_signal = median_filter(signal, window, plotting)
%% DESCRIPTION
%
%   Applies a Median filter to a denoise time series (especially to remove
%   spikes).
%       Note: for the manual threshold selection, look at the histogram and
%       select a point located right from the largest concentration of
%       points.
%
%   Input
%       signal: nx1 array corresponding to the tested time series
%       window: number of frames used to define the size of the window
%           (e.g. a value of 20 would mean that every data point in the
%           original signal will be replaced with the median of the 20 data
%           points before and the 20 data points after itself)
%       plot: set to 1 if you wish to see the resulting filtered signal
%
%   Output
%       filtered_signal: nx1 array corresponding to the filtered time
%           series
%       plot (optional): plot showing the original and filtered signals

%% FUNCTION

%   Plot histogram to manually select filter threshold
fig = figure;
clf
fig.Color = 'w';    % set background color to white
histogram(signal,100)
selection = ginput(1);
threshold = round(selection(1));

%   Find outliers using threshold
outliers = find(signal>threshold);

%   Initialize filtered signal
filtered_signal = signal;

%   Loop through outliers and set to the median of the points in the
%   corresponding window
for i=1:length(outliers)    
    % find lower and upper bounds
    low_bound = max(1,outliers(i)-window);
    upp_bound = min(outliers(i)+window, length(signal));    
    % compute median of surrounding points
    filtered_signal(outliers(i)) = median(signal(low_bound:upp_bound));
end

% Plotting
if plotting == 1
    % plot Gaussian
    fig = figure;
    fig.Color = 'w';    % set background color to white
    clf, hold on
    plot(1:length(signal), signal)
    plot(1:length(signal), filtered_signal, 'linew', 1.5)
    xlabel('Time [sec]'), ylabel('Amplitude')
    legend({'Original signal';'Median-filtered'})
    title('Median spike denoising filter')
end