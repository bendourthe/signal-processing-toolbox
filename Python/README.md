# Signal processing toolbox (Python)

## This toolbox includes a few custom Python codes enabling essential signal processing operations

__
## Denoising

#### Definition
This folder contains a few Python codes (and some examples codes) that can be used to denoise different types of time series.

#### Content
    
| Code | Definition  |
| ---- |-------------|
| average\_rep\_events.m | Restructures a time series composed of repetitive events into a matrix and calculate the corresponding average |
| gaussian\_filter.m | Applies a Gaussian filter to denoise a time series |
| linear\_detrend.m | Applies the detrend function remove the linear trend from a time series |
| lstm\_filter.m | Applies a least-squares template-matching filter to remove a potential artifact from a data set |
| median\_filter.m | Applies a Median filter to a denoise time series (especially to remove spikes) |
| moving\_average.m | Applies a moving average filter to denoise a time series |
| moving\_gaussian.m | Applies a different moving average filter to a time series (standard and gaussian modes) |
| poly\_detrend.m | Calculates the optimal Bayes information criterion (BIC), generate the corresponding polynomial fit (order = optimal BIC), and applies a polynomial detrend to denoise a time series |
| tkeo\_zscore.py    | Applies a Teager-Kaiser Energy-tracking Operator (TKEO) to denoise a time series (e.g. Electromyogram (EMG)) and generate the corresponding Z-Scores (potential application: activation detection for EMG signals) |

__
## Event detection

#### Definition
This folder contains a few Python codes (and some examples codes) that can be used to detect event within specific motion capture data.

#### Content
    
| Code | Definition  |
| ---- |-------------|
| distj\_event\_detection.m | Detects takeoff and landing during a single-legged distance jump trial |
| dvj\_event\_detection.m | Detects box jump, primary landing, takeoff, maximal jump and secondary landing during a drop vertical jump (DVJ) trial |

__
## Interpolation, resampling and reshaping

#### Definition
This folder contains a few Python codes (and some examples codes) that can be used to interpolate, resample, reshape different time series.

#### Content
    
| Code | Definition  |
| ---- |-------------|
| cubic\_spline\_fill.m | Interpolates missing observations within a time series using a cubic spline |
| cubic\_spline\_fill_3D.m | Applies cubic_spline_fill to each dimension of a 3D time series |
| cubic\_spline\_resample.m | Fits a cubic spline to the data and resamples the corresponding time series to the desired sampling rate |
| cubic\_spline\_resample_3D.m | Applies cubic_spline_resample to each dimension of a 3D time series |
| nan\_find.m | Generates a NaNs logical array where the indices of each NaN observation is True and generates a local function that can extract the indices of each NaN observation as a list. |
| reshape\_data.m | Reshape a data set to a specified length |
| true\_peaks.m | Finds peaks within a noisy signal via the corresponding filtered signal (i.e. removes noisy peaks) |

__
## Signals comparison

#### Definition
This folder contains a few Python codes (and some examples codes) that can be used to compare different time series.

#### Content
    
| Code | Definition  |
| ---- |-------------|
| dtw\_excursion.m | Applies an approximate Dynamic Time Warping (DTW) algorithm to compare two time series and calculate the corresponding mean and standard deviations of the amplitude and temporal excursions |
