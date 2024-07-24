import numpy as np
arr = np.array([1,2,3,4])
print (arr.dtype)

print("-----------")
# cambiar el tipo de dato forma 1

arr = np.array([1,2,3,4], dtype = 'float64') # cambiar el tipo de dato a float64
print (arr.dtype)
print(arr)

print("-----------")
# cambiar el tipo de dato del array, directamente desde numpy

arr = arr.astype(np.float64)
print(arr)
