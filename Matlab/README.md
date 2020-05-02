___

<a href='http://www.dourthe.tech'> <img src='Dourthe_Technologies_Headers.png' /></a>
___

# Signal processing toolbox (Matlab)

## This toolbox includes a few custom Matlab codes enabling essential signal processing operations

__
## Denoising

#### Definition
This folder contains a few Matlab codes (and some examples codes) that can be used to denoise different types of time series.

#### Content
    
| Code | Definition  |
| ---- |-------------|
| average\_rep\_events.m | Restructures a time series composed of repetitive events into a matrix and calculate the corresponding average |
| gaussian\_filter.m | Applies a Gaussian filter to denoise a time series |
| linear\_detrend.m | Applies the detrend function remove the linear trend from a time series |
| lstm\_filter.m | Applies a least-squares template-matching filter to remove a potential artifact from a data set |
| median\_filter.m | Applies a Median filter to a denoise time series (especially to remove spikes) |
| moving\_average.m | Applies a moving average filter to denoise a time series |
| poly\_detrend.m | Calculates the optimal Bayes information criterion (BIC), generate the corresponding polynomial fit (order = optimal BIC), and applies a polynomial detrend to denoise a time series |
| tkeo\_zscore.py    | Applies a Teager-Kaiser Energy-tracking Operator (TKEO) to denoise a time series (e.g. Electromyogram (EMG)) and generate the corresponding Z-Scores (potential application: activation detection for EMG signals) |

__
## Filtering

#### Definition
This folder contains a few Matlab codes (and some examples codes) that can be used to filter different types of time series.

#### Content
    
| Code | Definition  |
| ---- |-------------|
| fir1\_filter.m | Applies a Finite Impulse Response (FIR) filter to a time series |
| firls\_filter.m | Applies a Finite Impulse Response (FIR) least-square filter to a time series |

__
## Spectral analysis

#### Definition
This folder contains a few Matlab codes (and some examples codes) that can be used to analyse different types of time series in the frequency domain.

#### Content
    
| Code | Definition  |
| ---- |-------------|
| welch\_method.m | Applies Welch's method to a time series for spectral density estimation |
