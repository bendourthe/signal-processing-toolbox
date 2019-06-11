% Generate a multispectral random noisy signal
%   settings
sampling_rate = 1024;               % in Hz
duration = 2;                       % signal duration (in secs)
num_fr = sampling_rate*duration;    % total number of frame for corresponding duration
time  = (0:num_fr-1)/sampling_rate;
freq  = [12 18 30];                 % desired frequencies of sine waves in the signal
%   initialization
signal = zeros(size(time));
%   create signal using sine waves with corresponding frequencies
for i=1:length(freq)
    signal = signal + i*sin(2*pi*freq(i)*time);
end
%   add noise
signal = signal + randn(size(signal));

% Apply static Fast Fourier Transform to signal
fourier_signal = fft(signal);

% Calculate corresponding amplitude spectrum
amplitude_spectrum = 2*abs(fourier_signal)/num_fr;

% Define frequency spectrum as a vector (in Hz)
freq_spectr = linspace(0,srate/2,floor(num_fr/2)+1);

% Reconstruct signal using inverse Fast Fourrier Transform
recon_signal = ifft(fourier_signal);

% Plotting
fig = figure;
fig.Color = 'w';    % set background color to white
clf, hold on
subplot(211)
plot(time,signal,'linew',1.5)
xlabel('Time [sec]'), ylabel('Amplitude')
title('Original signal in time domain')
hold on
plot(time,recon_signal,'x', 'markersize', 5)
legend({'Original';'Inverse FFT reconstructed'})

subplot(212)
stem(freq_spectr,amplitude_spectrum(1:length(freq_spectr)),'linew',1.5)
set(gca,'xlim',[0 max(frex)*3])
xlabel('Frequency [Hz]'), ylabel('Amplitude')
title('Original signal in frequency domain')


