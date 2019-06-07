% Generate a signal with random spikes
%   number of spikes
n = 300;

%   inter-spike intervals (exponential distribution for bursts)
isi = round(exp(randn(n,1))*10);

%   generate time series
signal = 0;
for i=1:n
    signal(sum(isi(1:i))) = 1;
end

% Apply a moving average filter
%   settings
mode = 2;
sampling_rate = length(signal);
fwhm = 25;
window = 100;
plotting = 1;
%   function
filtered_signal = gaussian_filter(signal, mode, sampling_rate, fwhm, window, plotting);