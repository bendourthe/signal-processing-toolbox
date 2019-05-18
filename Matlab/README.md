# Signal processing toolbox (Matlab)

## This toolbox includes a few custom Matlab codes enabling essential signal processing operations

__
## Denoising
__
#### Definition
This folder contains a few Matlab codes (and some examples codes) that can be used to denoise different types of time series.

#### Content
    
| Code | Definition  |
| ---- |-------------|
| gaussian\_filter.m | Applies a Gaussian filter to denoise a time series |
| linear\_detrend.m | Applies the detrend function remove the linear trend from a time series |
| median\_filter.m | Applies a Median filter to a denoise time series (especially to remove spikes) |
| moving\_average.m | Applies a moving average filter to denoise a time series |
| poly\_detrend.m | Calculated the optimal Bayes information criterion (BIC), generate the corresponding polynomial fit (order = optimal BIC), and applies a polynomial detrend to denoise a time series |
| tkeo\_zscore.py    | Applies a Teager-Kaiser Energy-tracking Operator (TKEO) to denoise a time series (e.g. Electromyogram (EMG)) and generate the corresponding Z-Scores (potential application: activation detection for EMG signals) |
