# LIBRARIES IMPORT

import numpy as np
import scipy.io as sio
import matplotlib.pyplot as plt

# DEPENDENCIES

def lstm_filter(data, artifact):
    '''
    Applies a least-squares template-matching filter to remove a potential artifact from a data set.
        Note: works for 1D time series as well as multiple channels (e.g. original data set containing 10 channels of 10 distinct time series).
    Input:
        data: nxm array corresponding to the original data set
        artifact: nxm array corresponding to the artifact data set
    Output:
        residual: nx1 array corresponding to the filtered data
    Dependencies:
        None
    '''

    # Initialize residual
    residual = np.zeros(np.shape(data))


    for i in range(0,np.shape(data)[1]):

        # Generate design matrix X
        X = np.column_stack((np.ones(len(data)), artifact[:,i]))

        # Compute regression weights
        b = np.linalg.solve(np.matrix.transpose(X)@X,np.matrix.transpose(X)@data[:,i])

        # Compute predicted data (i.e. best fit to the artifact)
        yHat = X@b

        # Generate corresponding residuals (i.e. original data - artifact)
        residual[:,i] = data[:,i] - yHat

    return residual

# APPLICATION

# Load data
matdat = sio.loadmat('lstm_sample.mat')

# Allocate variables from data set
data = matdat['EEGdat']
artifact = matdat['eyedat']
time = matdat['timevec'][0]

# Apply least-squares template-matching filter
residual = lstm_filter(data, artifact)

# Plot mean artifact, original data and residual
plt.plot(time,np.mean(artifact,axis=1), label='Artifact')
plt.plot(time,np.mean(data,axis=1), label='Original data')
plt.plot(time,np.mean(residual,1), label='Residual')

plt.legend()
plt.xlabel('Time [ms]')
plt.ylabel('Amplitude')
plt.title('Mean data')
plt.show()
