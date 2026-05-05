import scipy.io
import matplotlib.pyplot as plt
import numpy as np

data = scipy.io.loadmat('Xtrain.mat')
Xtrain = data['Xtrain'].flatten()  # flatten to 1D array of 1000 values

# As a line plot
plt.figure(figsize=(12, 4))
plt.plot(Xtrain)
plt.title('Xtrain')
plt.xlabel('Sample index')
plt.ylabel('Value')
plt.show()

# As a histogram (to see distribution)
plt.figure()
plt.hist(Xtrain, bins=30)
plt.title('Xtrain distribution')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()