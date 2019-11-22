% Load data file (noisy signal)
load lineNoiseData.mat
signal = data;
sampling_rate = srate;

% Apply FIR1 filter
%   settings
f2filter = [50 150 250];
bwidth = 0.5;
order = 150;
plotting = 1;
filtered_signal = fir1_filter(signal, sampling_rate, f2filter, bwidth, order, plotting);
