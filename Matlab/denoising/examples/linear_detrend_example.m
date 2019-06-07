% General random signal with linear trend
n = 2000;
signal = cumsum(randn(1,n)) + linspace(-30,30,n);

% Apply linear detrending filter
%   settings
plotting = 1;
%   function
filtered_signal = linear_detrend(signal, plotting);