#Q2). Find the number of times a number appears in the list?
import numpy as np
the_array = np.array([9, 7, 4, 7, 3, 5, 9])
frequencies = np.asarray((np.unique(the_array, return_counts=True))).T
print(frequencies)