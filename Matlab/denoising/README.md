## Denoising (Matlab)
__
### Gaussian filter
#### Definition
Applies a Gaussian filter to denoise a time series.
#### Input
    signal: nx1 array corresponding to the tested time series
    mode: select mode to deal with edge effect
            0: set edges to zero
            1: set edges to original signal
            2: set edges to NaN
    sampling_rate: corresponding sampling rate of the time series
        (i.e. how many frames per seconds, in Hz)
    fwhm: full-width at half maximum, key variable defining Gaussian
        filter
    window: number of frames used to define the size of the window
        (e.g. a value of 20 would mean that every data point in the original
        signal will be replaced with the mean of the 20 data points and 20
        data points after itself)
    plot: set to 1 if you wish to see the resulting filtered signal
#### Output
    filtered_signal: nx1 array corresponding to the filtered time series
    plot (optional): plot showing the original time series along with
        the filtered signal and the corresponding window
#### Dependencies
    None
#### Example
    -> go to example folder and run code named gaussian_example.m
        or gaussian_spikes_example.m for more details

![Alt text](denoising/examples/img/gaussian_example_fwhm.jpg "Gaussian moving average example")
![Alt text](denoising/examples/img/gaussian_example.jpg "Gaussian moving average example")
![Alt text](denoising/examples/img/gaussian_spikes_example.jpg "Gaussian moving average with spikes example")

__
### Moving average
#### Definition
Applies a moving average filter to denoise a time series.
#### Input
    signal: nx1 array corresponding to the tested time series
    sampling_rate: corresponding sampling rate of the time series
        (i.e. how many frames per seconds, in Hz)
    window: number of frames used to define the size of the window
        (e.g. a value of 20 would mean that every data point in the original
        signal will be replaced with the mean of the 20 data points and 20
        data points after itself)
    plot: set to 1 if you wish to see the resulting filtered signal
#### Output
    filtered_signal: nx1 array corresponding to the filtered time series
    plot (optional): plot showing the original time series along with the
        filtered signal and the corresponding window
#### Dependencies
    None
#### Example
    -> go to example folder and run code named moving_average_example.m for more details

![Alt text](denoising/examples/img/moving_average_example.jpg "moving average example")

__
### Teager-Kaiser Energy-tracking Operator (TKEO) and Z-Score
#### Definition
 Applies a Teager-Kaiser Energy-tracking Operator (TKEO) to denoise a time series (e.g. Electromyogram (EMG)) and generate the corresponding Z-Scores (potential application: activation detection for EMG signals).
#### Input
    signal: nx1 array corresponding to the tested time series
    sampling_rate: corresponding sampling rate of the time series (i.e.
        how many frames per seconds, in Hz)
    plot: set to 1 if you wish to see the resulting filtered signal
#### Output
    filtered_signal: nx1 array corresponding to the filtered time series
    signal_zscore: nx1 array corresponding to z-score of the original time series
    filtered_signal_zscore: nx1 array corresponding to z-score of the filtered time series
    plot (optional): plot showing the original and filtered signals along with the corresponding z-scores
#### Dependencies
    None
#### Example
    -> go to example folder and run code named tkeo_zscore_example.m and use
        the file emg_sample.mat for more details

![Alt text](denoising/examples/img/tkeo_zscore_example.jpg "Teager-Kaiser Energy-tracking Operator and Z-Score example")
