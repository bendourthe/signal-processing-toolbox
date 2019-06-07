% Import data (here: Electromyogram)
load emg_sample.mat
time = emgtime;
signal = emg;

% Apply Teager-Kaiser Energy-tracking Operator (TKEO)
%   settings
plotting = 1;
%   function
[filtered_signal, signal_zscore, filtered_signal_zscore] = tkeo_zscore(signal, time, plotting);