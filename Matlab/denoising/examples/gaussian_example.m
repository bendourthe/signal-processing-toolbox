% Generate a random signal
sampling_rate = 1000; % Hz
time = 0:1/sampling_rate:3;
n = length(time);
p = 15; % poles for random interpolation

% Define noise level (measured in standard deviations)
noiseamp = 5; 

% Define amplitude modulator and noise level
ampl   = interp1(rand(p,1)*30,linspace(1,p,n));
noise  = noiseamp * randn(size(time));
signal = ampl + noise;

% Apply a moving average filter
%   settings
fwhm = 25;
window = 40;
plotting = 1;
%   function
filtered_signal = gaussian_filter(signal, 2, sampling_rate, fwhm, window, plotting);