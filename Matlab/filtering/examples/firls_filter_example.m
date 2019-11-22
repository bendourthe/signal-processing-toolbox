% Generate a random signal
sampling_rate = 350; % Hz
time = (0:sampling_rate*7-1)/sampling_rate;
npnts = length(time);
yOrig = cumsum(randn(npnts,1));
signal = yOrig + 50*randn(npnts,1) + 40*sin(2*pi*50*time)';

% Apply FIRls filter
%   settings
mode = 0;    % 0 for low-pass, 1 for high-pass
cutoff_f = 30;
order = 7;
plotting = 1;
filtered_signal = firls_filter(signal, mode, sampling_rate, cutoff_f, order, plotting);