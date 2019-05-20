% Generate random signal

%   create event (derivative of Gaussian)
dur = 100; % duration of event in time points
event = diff(exp(-linspace(-2,2,dur+1).^2));
event = event./max(event); % normalize to max=1

%   define onset times
num_events = 30;
onset = randperm(10000-dur);
onset = onset(1:num_events);

%   generate events
signal = zeros(1,10000);
for ei=1:num_events
    signal(onset(ei):onset(ei)+dur-1) = event;
end

%   add noise
signal = signal + .5*randn(size(signal));

% Restructure data into matrix and calculate average
%   settings
plotting = 1;
%   function
data_matrix = average_rep_events(signal, dur, onset, plotting);

% Plotting
%   original signal
fig = figure;
fig.Color = 'w';    % set background color to white
clf, hold on
subplot(311)
plot(signal)
xlabel('Time [sec]'), ylabel('Amplitude')
title('Original signal')
%   random single event
subplot(312)
plot(1:k, data(onsettimes(3):onsettimes(3)+k-1), 1:k, event, 'linew', 1.5)
xlabel('Time [sec]'), ylabel('Amplitude')
legend({'Averaged';'Ground-truth'})
title('Random event')
%   original event with calculated average
subplot(313)
plot(1:dur,mean(data_matrix), 1:dur, event, 'linew', 1.5)
xlabel('Time [sec]'), ylabel('Amplitude')
legend({'Averaged';'Ground-truth'})
title('Average events')