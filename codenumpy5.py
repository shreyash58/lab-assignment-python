#Q5). Convert numpy array of string to an array of floats in numpy ?
import numpy as np
string_arr = np.array(['1.1', '2.2', '3.3'])
float_arr = string_arr.astype(np.float64)
print(float_arr)