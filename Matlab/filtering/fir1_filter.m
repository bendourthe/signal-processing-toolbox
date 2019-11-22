function filtered_signal = fir1_filter(signal, sampling_rate, f2filter, bwidth, order, plotting)
%% DESCRIPTION
%
%   Applies a Finite Impulse Response (FIR) filter to a time series.
%       Note: uses fir1 function.
%
%   Input
%       signal: nx1 array corresponding to the tested time series
%       sampling_rate: corresponding sampling rate of the time series (i.e.
%           how many frames per seconds, in Hz) [default = length(signal)]
%       f2filter: define the frequencies to filter (can be more than one)
%           [default (arbitrary) = [20 45]]
%       bwidth: define the width of each band to filter (e.g. if the 1st
%           frequency in f2filter is 100 and bwidth is 5, the signal will be
%           filtered between 95 and 105 Hz)
%       order: define order of the Kernel (higher order will have more time
%           points and bring the Actual Kernel closer to the Ideal Kernel,
%           but too high values will also add artifacts) [default = 5]
%       plotting: set to 1 if you wish to see the resulting Kernel and 
%           filtered signal [default = 0]
%
%   Output
%       filtered_signal: nx1 array corresponding to the filtered signal
%       plot (optional): plots showing (1) the Kernel in frequency domains,
%           for each frequency to filter and (2) the original and filtered
%           signals (in time and frequency domains)

%% FUNCTION

% Deal with default values and potential missing input variables
switch nargin
    case 1
        sampling_rate = length(signal);
        f2filter = [20 45];
        bwidth = 1;
        order = 5;
        plotting = 0;
    case 2
        f2filter = [20 45];
        bwidth = 1;
        order = 5;
        plotting = 0;
    case 3
        bwidth = 1;
        order = 5;
        plotting = 0;
    case 4
        order = 5;
        plotting = 0;
    case 5
        plotting =0;
end

% Define time based on signal length and sampling rate
time = 0:1/sampling_rate:(length(signal)-1)/sampling_rate;

% Define additional kernel parameters
nyquist = sampling_rate/2;
num_points = length(signal);

% Initialize the filtered signal
filtered_signal = signal;

% loop over frequencies
for i=1:length(f2filter)    
    % Define filter Kernel parameters
    frange = [f2filter(i)-bwidth f2filter(i)+bwidth];
    ord = round(order*sampling_rate/frange(1));
    % Define filter Kernel
    filter_kernel = fir1(ord, frange/nyquist, 'stop');    
    % Visualize the Kernel and its spectral response
    if plotting == 1
        fig = figure(1);
        fig.Color = 'w';    % set background color to white  
        subplot(length(f2filter), 1, i)
        plot(linspace(0, sampling_rate, round(0.01*num_points)), abs(fft(filter_kernel, round(0.01*num_points))).^2, 'linew', 1.5)
        set(gca, 'xlim', [f2filter(i)-bwidth*10 f2filter(i)+bwidth*10])
        xlabel('Frequency [Hz]')
        ylabel('Gain')    
        title('Filter Kernel (frequency domain - power spectrum)')
    end
    % Iteratively apply filter to signal
    filtered_signal = filtfilt(filter_kernel, 1, filtered_signal);    
end

% Plotting
if plotting == 1
    fig = figure;
    fig.Color = 'w';    % set background color to white
    % plot original and filtered signals (time domain)
    subplot(211), hold on
    plot(time, signal, 'k')
    plot(time, filtered_signal);
    xlabel('Time [sec]')
    ylabel('Amplitude')
    legend({'Original'; 'Filtered'})
    title('Original vs. Filtered signals (time domain)')
    % plot original and filtered signals (frequency domain - power spectra)
    %   compute the power spectrum of the filtered signal
    subplot(212), cla, hold on
    %   compute power spectrum and frequencies vector
    signal_power = abs(fft(signal)/num_points).^2;
    hz = linspace(0, sampling_rate, num_points);
    filter_power = abs(fft(filtered_signal)/num_points).^2;
    plot(hz, signal_power, 'k')
    plot(hz, filter_power);
    set(gca, 'xlim', [0 nyquist], 'ylim', [0 2])
    xlabel('Frequency [Hz]')
    ylabel('Power')
    title('Original vs. Filtered signals (frequency domain - power spectra)')
end