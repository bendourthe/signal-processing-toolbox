% Generate a random signal
n = 2000;
signal = cumsum(randn(n,1));

% Define proportion of data points to replace with noise
propnoise = .05;

% Find noisy data points
noisepnts = randperm(n);
noisepnts = noisepnts(1:round(n*propnoise));

% Generate new signal with noise
signal(noisepnts) = 50+rand(size(noisepnts))*100;

% Apply median filter
%   settings
window = 40;
plotting = 1;
%   function
filtered_signal = median_filter(signal, 20, 0);