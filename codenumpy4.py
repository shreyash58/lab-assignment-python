#Q4).How to sum the first column only in numpy ?
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)
print(newarr)
column_sums = newarr[:, 0].sum()
print(column_sums)