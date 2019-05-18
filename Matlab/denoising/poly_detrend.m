function filtered_signal = poly_detrend(signal, plotting)
%% DESCRIPTION
%
%   Calculated the optimal Bayes information criterion (BIC), generate the
%   corresponding polynomial fit (order = optimal BIC), and applies a
%   polynomial detrend to denoise a time series.
%
%   Input
%       signal: nx1 array corresponding to the tested time series
%       plotting: set to 1 if you wish to see the resulting filtered signal
%
%   Output
%       filtered_signal: nx1 array corresponding to the filtered signal
%       plot (optional): plot showing the corresponding BIC evolution and
%           the original and filtered signals

%% FUNCTION

%   Signal properties
n = length(signal);
t = (1:n)';

%   Range of orders
orders = (5:40)';

%   Calculate corresponding sum of squared errors
sum_se = zeros(length(orders),1); 

%   Loop through orders
for i=1:length(orders)    
    % compute polynomial fitting time series
    yHat = polyval(polyfit(t,signal,orders(i)),t);    
    % compute corresponding fit of model to data (sum of squared errors)
    sum_se(i) = sum((yHat-signal).^2)/n;
end

%   Calculate BIC
bic = n*log(sum_se) + orders*log(n);

%   Calculate optimal BIC (i.e. lowest)
[bestP,idx] = min(bic);

%   Calculate polynomial fit
poly_coefs = polyfit(t,signal,orders(idx));

%   Calculate estimated data based on coefficients
yHat = polyval(poly_coefs,t);

%   Calculate detrended filtered signal (i.e. residual)
filtered_signal = signal - yHat;

% Plotting
if plotting == 1
    fig1 = figure;
    fig1.Color = 'w';    % set background color to white
    clf, hold on
    plot(orders,bic,'ks-','markerfacecolor','w','markersize',8,'linew',1.5)
    plot(orders(idx),bestP,'o','markersize',15,'linew',1.5)
    xlabel('Polynomial order'), ylabel('BIC')
    title('Bayes information criterion evolution')

    fig2 = figure;
    fig2.Color = 'w';    % set background color to white
    clf, hold on
    h = plot(t,signal);
    set(h,'color',[1 1 1]*.6)
    plot(t,yHat,'linew',1.5)
    plot(t,filtered_signal,'k')
    set(gca,'xlim',t([1 end]))
    xlabel('Time [sec]'), ylabel('Amplitude')
    legend({'Original';'Polynomial fit';'Filtered'})
    title(['Polynomial fit and detrending for order = ' num2str(orders(idx))])
end