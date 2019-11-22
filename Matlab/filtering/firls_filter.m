function filtered_signal = firls_filter(signal, mode, sampling_rate, cutoff_f, order, plotting)
%% DESCRIPTION
%
%   Applies a Finite Impulse Response (FIR) least-square filter to a time
%   series.
%       Note: uses firls function.
%
%   Input
%       signal: nx1 array corresponding to the tested time series
%       mode: select type of filter
%           0: low-pass filter (gets ride of high frequencies) [default]
%           1: high-pass filter (gets ride of low frequencies)
%       sampling_rate: corresponding sampling rate of the time series (i.e.
%           how many frames per seconds, in Hz) [default = length(signal)]
%       cutoff_f: cut-off frequency (frequencies above this value will be
%           filtered) [default (arbitrary) = 30]
%       order: define order of the Kernel (higher order will have more time
%           points and bring the Actual Kernel closer to the Ideal Kernel,
%           but too high values will also add artifacts) [default = 5]
%       plotting: set to 1 if you wish to see the resulting Kernel and 
%           filtered signal [default = 0]
%
%   Output
%       filtered_signal: nx1 array corresponding to the filtered signal
%       plot (optional): plots showing (1) the Kernel in time and frequency
%           domains, and (2) the original and filtered signals (in time and
%           frequency domains)

%% FUNCTION

% Deal with default values and potential missing input variables
switch nargin
    case 1
        mode = 0;
        sampling_rate = length(signal);
        cutoff_f = 30;
        order = 5;
        plotting = 0;
    case 2
        sampling_rate = length(signal);
        cutoff_f = 30;
        order = 5;
        plotting = 0;
    case 3
        cutoff_f = 30;
        order = 5;
        plotting = 0;
    case 4
        order = 5;
        plotting = 0;
    case 5
        plotting = 0;
end

% Define time based on signal length and sampling rate
time = 0:1/sampling_rate:(length(signal)-1)/sampling_rate;

% Define additional kernel parameters
if mode == 0
    shape = [1 1 0 0];
elseif mode == 1
    shape = [0 0 1 1];
end
nyquist = sampling_rate/2;
num_points = length(time);
transw = .1;
order = round(order*sampling_rate/cutoff_f);
frex = [0 cutoff_f cutoff_f+cutoff_f*transw nyquist] / nyquist;

% Build kernel
filter_kernel = firls(order, frex, shape);

% Compute the power spectrum of the signal and filter kernel
filter_power = abs(fft(filter_kernel,num_points)).^2;

% Compute the frequency vector and remove negative frequencies
hz = linspace(0, sampling_rate/2, floor(num_points/2)+1);
filter_power = filter_power(1:length(hz));

% Apply filter to the data
filtered_signal = filtfilt(filter_kernel, 1, signal);

% Plotting
if plotting == 1
    % plot Kernel (time domain)
    fig = figure;
    fig.Color = 'w';    % set background color to white
    subplot(321)
    plot((-order/2:order/2)/sampling_rate, filter_kernel, 'k', 'linew', 1.5)
    xlabel('Time [sec]')
    title('Filter Kernel (time domain)')
    % plot Kernal (frequency domain - power spectrum)
    subplot(322), hold on
    plot(frex*sampling_rate/2, shape, 'r', 'linew', 1.5)
    plot(hz, filter_power(1:length(hz)), 'k', 'linew', 1.5)
    set(gca, 'xlim', [0 2*cutoff_f])
    xlabel('Frequency [Hz]')
    ylabel('Gain')
    title('Filter Kernel (frequency domain - power spectrum)')
    % plot original and filtered signals (time domain)
    subplot(312)
    h = plot(time, signal, time, filtered_signal, 'linew', 1.5);
    set(h(1), 'color', [1 1 1]*.4)
    legend({'Original';'Filtered'})
    xlabel('Time [sec]')
    ylabel('Amplitude')
    title('Original vs. Filtered signals (time domain)')
    % plot original and filtered signals (frequency domain - power spectra)
    yOrigX = abs(fft(signal)/num_points).^2;
    yFiltX = abs(fft(filtered_signal)/num_points).^2;
    subplot(313)
    plot(hz, yOrigX(1:length(hz)), hz, yFiltX(1:length(hz)), 'linew', 1.5);
    set(gca, 'xlim', [0 sampling_rate/5], 'yscale', 'log')
    legend({'Original';'Filtered'})
    xlabel('Frequency [Hz]')
    ylabel('Power [log]')
    title('Original vs. Filtered signals (frequency domain - power spectra)')
end