% Load data
load EEGrestingState.mat

% Allocate variables from data set
signal = eegdata;
sampling_rate = srate;

% Define time vector
time = (0:length(signal)-1)/sampling_rate;

% Plot loaded data
fig = figure;
fig.Color = 'w';    % set background color to white
clf, hold on
plot(time, signal, 'linew', 1.5)
xlabel('Time [sec]'), ylabel('Amplitude')
title('Loaded EEG signal')

% Apply Welch's method to signal
%   settings
window = sampling_rate;
overlap = round(sampling_rate/2);
plotting = 1;
%   function
welch_power = welch_method(signal, sampling_rate, window, overlap, plotting);

