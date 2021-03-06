function welch_power = welch_method(signal, sampling_rate, window, overlap, plotting)
%% DESCRIPTION
%
%   Applies Welch's method to a time series for spectral density estimation.
%
%   Input
%       signal: nx1 array corresponding to the tested time series
%       sampling_rate: corresponding sampling rate of the time series (i.e.
%           how many frames per seconds, in Hz) [default = length(signal)]
%       window: number of frames used to define the size of the window
%           (i.e. how many data points are included in each isolated portion
%           of the original signal) [default = sampling rate]
%       overlap: number of frames where two consecutive windows will overlap
%           [default = half of sampling rate]
%       plotting: set to 1 if you wish to see the resulting filtered signal
%           [default = 0]
%
%   Output
%       welch_power: corresponding power spectrum using Welch's method
%       plot (optional): plots showing (1) defined Hann window and the
%           corresponding edge attenuation on a random sample, and (2) the
%           comparison between the power spectra obtained via Static FFT
%           and Welch's method

%% FUNCTION

% Deal with default values and potential missing input variables
switch nargin
    case 1
        sampling_rate = length(signal);
        window = sampling_rate;
        overlap = round(sampling_rate/2);
        plotting = 0;
    case 2
        window = sampling_rate;
        overlap = round(sampling_rate/2);
        plotting = 0;
    case 3
        overlap = round(sampling_rate/2);
        plotting = 0;
    case 4
        plotting = 0;
end

% Define window onset based on selected window and overlap
onsets = 1:overlap:length(signal)-window;

% Define frequency spectrum as a vector (in Hz)
freq_spectr = linspace(0,sampling_rate/2,floor(window/2)+1);

% Define Hann window to minimize edge effects (i.e. filter signal by
% applying a progressive attenuation around the edges)
hannw = .5 - cos(2*pi*linspace(0,1,window))./2;

% Initialize the power matrix (shape: windows x frequencies)
welch_power = zeros(1,length(freq_spectr));

% Apply Welch's method to signal
for i=1:length(onsets)
    % isolate a portion of the original signal
    signal_portion = signal(onsets(i):onsets(i)+window-1);    
    % apply Hann window to taper signal around edges
    signal_portion = signal_portion .* hannw;    
    % compute power
    power = abs(fft(signal_portion)/window).^2;    
    % enter into matrix
    welch_power = welch_power + power(1:length(freq_spectr));
end

% Divide by number of windows to obtain average
welch_power = welch_power / length(onsets);

% Plotting
if plotting == 1
    % plot Hann window and random signal portion
    fig1 = figure;
    fig1.Color = 'w';    % set background color to white
    clf, hold on
    subplot(211)
    plot(hannw, 'linew', 1.5)
    xlim([0 length(hannw)])
    ylabel('Amplitude')
    title('Hann window')
    
    subplot(212)
    rand_idx = round(rand*(length(onsets)-1)) + 1;
    signal_sample = signal(onsets(rand_idx):onsets(rand_idx)+window-1);
    plot(signal_sample, 'linew', 1.5)
    hold on
    plot(signal_sample .* hannw, 'linew', 1.5)
    xlim([0 length(signal_sample)])
    ylabel('Amplitude')
    legend({'Original sample';'Hann'})
    title('Edge effect attenuation using Hann window')

    % plot Static FFT and Welch's power spectra
    fig2 = figure;
    fig2.Color = 'w';    % set background color to white
    clf, hold on
    %   define Static FFT
    sfft_freq_spectr = linspace(0,sampling_rate/2,floor(length(signal)/2)+1);
    sfft_spectr = abs(fft(signal)/length(signal)).^2;
    plot(sfft_freq_spectr, sfft_spectr(1:length(sfft_freq_spectr)), 'linew', 1.5)
    plot(freq_spectr, welch_power/10, 'linew', 1.5)
    set(gca,'xlim',[0 40])
    xlabel('Frequency [Hz]')
    legend({'Static FFT';'Welch''s method'})
    title('Static FFT vs. Welch''s method')
end