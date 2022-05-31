#Q7).WAP to find the mean of the numpy array in Python ?
import numpy as np
the_array = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
mean_array = the_array.mean(axis=0)
print(mean_array)