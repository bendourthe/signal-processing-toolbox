% Import data (here: Electromyogram)
load emg_sample.mat
time = emgtime;
signal = emg;

% Apply Teager-Kaiser Energy-tracking Operator (TKEO)
%   settings
sampling_rate = 512;    % in Hz
plotting = 1;
[filtered_signal, signal_zscore, filtered_signal_zscore] = tkeo_zscore(time, signal, sampling_rate, plotting);