function filtered_signal = linear_detrend(signal, plotting)
%% DESCRIPTION
%
%   Applies the detrend function to remove the linear trend from a time
%       series.
%       Note: added option to plot original and filtered signals.
%
%   Input
%       signal: nx1 array corresponding to the tested time series
%       plotting: set to 1 if you wish to see the resulting filtered signal
%           [default = 0]
%
%   Output
%       filtered_signal: nx1 array corresponding to the filtered signal
%       plot (optional): plot showing the original and filtered signals

%% FUNCTION

% Deal with default values and potential missing input variables
switch nargin
    case 1
        plotting = 0;
end

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