% Load data set
load templateProjection.mat

% Atribute data sets
data = EEGdat;
artifact = eyedat;

% Apply least-squares template-matching filter
residual = lstm_filter(data, artifact);

% Plot mean artifact, original data and residual
fig1 = figure;
fig1.Color = 'w';    % set background color to white
clf, hold on
plot(timevec, mean(eyedat,2), timevec, mean(EEGdat,2), timevec, mean(residual,2), 'linew', 1.5)
legend({'Artifact';'Original data';'Residual'})
xlabel('Time [ms]'), ylabel('Amplitude')
title('Mean data')

% Plot all trials in a map
clim = [-1 1]*20;

fig2 = figure;
fig2.Color = 'w';    % set background color to white
clf, hold on
subplot(131)
imagesc(timevec,[],eyedat')
set(gca,'clim',clim)
xlabel('Time [ms]'), ylabel('Trials')
title('Artifact')

subplot(132)
imagesc(timevec,[],EEGdat')
set(gca,'clim',clim)
xlabel('Time [ms]'), ylabel('Trials')
title('Original data')

subplot(133)
imagesc(timevec,[],resdat')
set(gca,'clim',clim)
xlabel('Time [ms]'), ylabel('Trials')
title('Residual')