function filtered_signal = linear_detrend(signal, plotting)
%% DESCRIPTION
%
%   Applies the detrend function remove the linear trend from a time
%       series.
%       Note: added option to plot original and filtered signals.
%
%   Input
%       signal: nx1 array corresponding to the tested time series
%       plot: set to 1 if you wish to see the resulting filtered signal
%
%   Output
%       filtered_signal: nx1 array corresponding to the filtered signal
%       plot (optional): plot showing the original and filtered signals

%% FUNCTION

% Remove linear trend using detrend function
filtered_signal = detrend(signal);

% Plotting
if plotting == 1
    fig = figure;
    fig.Color = 'w';    % set background color to white
    clf, hold on
    plot(1:length(signal), signal)
    plot(1:length(filtered_signal), filtered_signal, 'linew', 1.5)
    xlabel('Time [sec]'), ylabel('Amplitude')
    legend({ ['Original (mean=' num2str(mean(signal)) ')' ];[ 'Detrended (mean=' num2str(mean(filtered_signal)) ')' ]})
    title('Linear detrending filter')
end