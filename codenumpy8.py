#Q8).WAP a program in python to find the sum of all element of numpy array ?
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)
column_sums = newarr[:, :].sum()
print(column_sums)