function [filtered_signal, signal_zscore, filtered_signal_zscore] = tkeo_zscore(time, signal, sampling_rate, plotting)
%% DESCRIPTION
%
%   Applies a Teager-Kaiser Energy-tracking Operator (TKEO) to denoise a
%   time series (e.g. Electromyogram).
%
%   Input
%       signal: nx1 array corresponding to the tested time series
%       sampling_rate: corresponding sampling rate of the time series (i.e.
%           how many frames per seconds, in Hz)
%       plot: set to 1 if you wish to see the resulting filtered signal
%
%   Output
%       filtered_signal: nx1 array corresponding to the filtered time
%           series
%       signal_zscore: nx1 array corresponding to z-score of the original
%           time series
%       filtered_signal_zscore: nx1 array corresponding to z-score of the
%           filtered time series
%       plot (optional): plot showing the original and filtered signals
%           along with the corresponding z-scores

%% FUNCTION

% Initialize filtered signal vector
filtered_signal = signal;

% Apply TKEO to original time series
filtered_signal(2:end-1) = signal(2:end-1).^2 - signal(1:end-2).*signal(3:end);

% Concert original and filtered time series to z-score
%   find timepoint zero
time0 = dsearchn(time',0)

%   convert original time series
signal_zscore = (signal-mean(signal(1:time0))) / std(signal(1:time0));

%	convert filtered time series
filtered_signal_zscore = (filtered_signal-mean(filtered_signal(1:time0))) / std(filtered_signal(1:time0));

% Plotting
if plotting == 1
    fig = figure;
    fig.Color = 'w';    % set background color to white
    clf
    % plot original and filtered time series (normalized to max-1)
    subplot(211), hold on
    plot(time, signal./max(signal), 'linew', 1.5)
    plot(time, filtered_signal./max(filtered_signal), 'linew', 1.5)
    xlabel('Time [ms]'), ylabel('Amplitude or energy')
    legend({'signal'; 'filtered signal (TKEO)'})

    % plot zscores
    subplot(212), hold on
    plot(time, signal_zscore, 'linew', 1.5)
    plot(time, filtered_signal_zscore, 'linew', 1.5)
    xlabel('Time [ms]'), ylabel('z-score')
    legend({'signal'; 'filtered signal (TKEO)'})
end