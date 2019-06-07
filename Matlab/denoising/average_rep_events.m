function data_matrix = average_rep_events(signal, dur, onset, plotting)
%% DESCRIPTION
%
%   Restructures a time series composed of repetitive events into a matrix
%   and calculate the corresponding average.
%       Note: this code assumes that each event has a constant duration.
%
%   Input
%       signal: nx1 array corresponding to the tested time series
%       dur: duration of each event (in frames)
%       onset: mx1 array corresponding to the frame numbers when each event
%           happens (when m = number of events in the signal)
%       plotting: set to 1 if you wish to see the resulting resulting
%           restructured matrix [default = 0]
%
%   Output
%       data_matrix: nxm array corresponding to the restructured matrix
%       plot (optional): plot showing the restructured matrix

%% FUNCTION

%   Deal with default values and potential missing input variables
switch nargin
    case 1
        error('Missing input variables: duration and onset')
    case 2
        error('Missing input variables: onset')
    case 3
        plotting = 0;
end

%   Calculate number of events
num_events = length(onset);

%   Initialize matrix
data_matrix = zeros(num_events,dur);

%   Restructure data into matrix
for i=1:num_events
    data_matrix(i,:) = signal(onset(i):onset(i)+dur-1);
end

% Plotting
if plotting == 1
    fig = figure;
    fig.Color = 'w';    % set background color to white
    clf, hold on
    imagesc(data_matrix)
    xlabel('Time [sec]'), ylabel('Event number')
    title('All events')
end