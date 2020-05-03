___

<a href='http://www.dourthe.tech'> <img src='Dourthe_Technologies_Headers.png' /></a>
___
<center><em>For more information, visit <a href='http://www.dourthe.tech'>www.dourthe.tech</a></em></center>

# Signal processing toolbox (Python)

## This toolbox includes a few custom Python codes enabling essential signal processing operations

__
## Denoising

#### Definition
This folder contains a few Python codes (and some examples codes) that can be used to denoise different types of time series.

#### Content
    
| Code | Definition  |
| ---- |-------------|
| average\_rep\_events.py | Restructures a time series composed of repetitive events into a matrix and calculate the corresponding average |
| gaussian\_filter.py | Applies a Gaussian filter to denoise a time series |
| linear\_detrend.m | Applies the detrend function remove the linear trend from a time series |
| lstm\_filter.py | Applies a least-squares template-matching filter to remove a potential artifact from a data set |
| median\_filter.py | Applies a Median filter to a denoise time series (especially to remove spikes) |
| moving\_average.py | Applies a moving average filter to denoise a time series |
| moving\_gaussian.py | Applies a different moving average filter to a time series (standard and gaussian modes) |
| poly\_detrend.py | Calculates the optimal Bayes information criterion (BIC), generate the corresponding polynomial fit (order = optimal BIC), and applies a polynomial detrend to denoise a time series |
| tkeo\_zscore.py | Applies a Teager-Kaiser Energy-tracking Operator (TKEO) to denoise a time series (e.g. Electromyogram (EMG)) and generate the corresponding Z-Scores (potential application: activation detection for EMG signals) |

__
## Event detection

#### Definition
This folder contains a few Python codes (and some examples codes) that can be used to detect event within specific motion capture data.

#### Content
    
| Code | Definition  |
| ---- |-------------|
| distj\_event\_detection.py | Detects takeoff and landing during a single-legged distance jump trial |
| dvj\_event\_detection.py | Detects box jump, primary landing, takeoff, maximal jump and secondary landing during a drop vertical jump (DVJ) trial |
| timed\_event\_detection.py | Detects takeoff and time when a distance of 2.5 meters is reached during a single-legged distance jump trial |

__
## Filtering

#### Definition
This folder contains a few Matlab codes (and some examples codes) that can be used to filter different types of time series.

#### Content
    
| Code | Definition  |
| ---- |-------------|
| firls\_filter.m | Applies a Finite Impulse Response (FIR) least-square filter to a time series |

__
## Interpolation, resampling and reshaping

#### Definition
This folder contains a few Python codes (and some examples codes) that can be used to interpolate, resample, reshape different time series.

#### Content
    
| Code | Definition  |
| ---- |-------------|
| cubic\_spline\_fill.py | Interpolates missing observations within a time series using a cubic spline |
| cubic\_spline\_fill_3D.py | Applies cubic_spline_fill to each dimension of a 3D time series |
| cubic\_spline\_resample.py | Fits a cubic spline to the data and resamples the corresponding time series to the desired sampling rate |
| cubic\_spline\_resample_3D.py | Applies cubic_spline_resample to each dimension of a 3D time series |
| nan\_find.py | Generates a NaNs logical array where the indices of each NaN observation is True and generates a local function that can extract the indices of each NaN observation as a list. |
| reshape\_data.py | Reshape a data set to a specified length (down- or up-sample) |
| true\_peaks.py | Finds peaks within a noisy signal via the corresponding filtered signal (i.e. removes noisy peaks) |

__
## Signals comparison

#### Definition
This folder contains a few Python codes (and some examples codes) that can be used to compare different time series.

#### Content
    
| Code | Definition  |
| ---- |-------------|
| crosscorr\_fft.py | Calculate the time shift between 2 signals using a Fast Fourier Transform (FFT) |
| dtw\_excursion.py | Applies an approximate Dynamic Time Warping (DTW) algorithm to compare two time series and calculate the corresponding mean and standard deviations of the amplitude and temporal excursions |
| ICC\_2way\_mixed.py | Calculate the Intraclass Correlation Coefficient (ICC) using the Two-way Mixed Model for Case 3* defined by Patrick E. Shrout and Joseph L. Fleiss. “Intraclass Correlations: Uses in assessing rater reliability.” Psychological Bulletin 86.2 (2979): 420-428 (*In Case 3, each target/subject/observation is rated by each of the same m observers/judges/methods, who are the only observers/judges/methods of interest) |
| time\_delay\_fft.py | Calculate the maximal time shift between 2 signals using a Fast Fourier Transform (FFT) |

__
## Spectral analysis

#### Definition
This folder contains a few Python codes (and some examples codes) that can be used to analyse time series in the frequency domain.

#### Content
    
| Code | Definition  |
| ---- |-------------|
| fft\_spectral\_exammple.py | Applies a Fast Fourier Transform (FFT) to perform the spectral analysis of a time series |
| welch\_method.py | Applies Welch's method to a time series for spectral density estimation |
