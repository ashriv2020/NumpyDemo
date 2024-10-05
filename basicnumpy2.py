import numpy as np

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
number_of_dimension = a.ndim

print('Array:',  a)
print('number_of_dimension:', number_of_dimension)

array_shape = a.shape
print('array_shape:', array_shape)

if len(array_shape) == number_of_dimension:
    print('Shape and Dimensions are equal!')
else:
    print('Shape and Dimensions are not equal!') 

array_size = a.size    
print('array_size:', array_size)   

import math
if array_size == math.prod(a.shape):
    print('Shape and Size are equal!')
else:
    print('Shape and Size are not equal!') 

# Arrays are typically “homogeneous”, meaning that they contain elements of only one “data type”. 
# The data type is recorded in the dtype attribute.
array_datatype = a.dtype
print('array_datatype:', array_datatype)
