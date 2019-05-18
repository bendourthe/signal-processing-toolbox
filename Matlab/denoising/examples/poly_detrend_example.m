% Generate a random signal with polynomial artifact
n = 10000;
t = (1:n)';
k = 10; % number of poles for random amplitudes
slowdrift = interp1(100*randn(k,1),linspace(1,k,n),'pchip')';
signal = slowdrift + 20*randn(n,1);

% Apply median filter
%   settings
plotting = 1;
%   function
filtered_signal = poly_detrend(signal, plotting);