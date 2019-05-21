function residual = lstm_filter(data, artifact)
%% DESCRIPTION
%
%   Applies a least-squares template-matching filter to remove a potential
%   artifact from a data set.
%       Note: works for 1D time series as well as multiple channels (e.g.
%       original data set containing 10 channels of 10 distinct time
%       series).
%
%   Input
%       data: nxm array corresponding to the original data set
%       artifact: nxm array corresponding to the artifact data set
%
%   Output
%       residual: nx1 array corresponding to the filtered data

%% FUNCTION

%   Initialize residual
residual = zeros(size(data));

for i=1:size(residual,2)
    
    % generate design matrix X
    X = [ones(length(data),1) artifact(:,i)];
    
    % compute regression weights
    b = (X'*X) \ (X'*data(:,i));
    
    % compute predicted data (i.e. best fit to the artifact)
    yHat = X*b;
    
    % generate corresponding residuals (i.e. original data - artifact)
    residual(:,i) = (data(:,i) - yHat)';
end