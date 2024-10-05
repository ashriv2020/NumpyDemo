import numpy as np
"""
You might hear of a 0-D (zero-dimensional) array referred to as a “scalar”,
 a 1-D (one-dimensional) array as a “vector”, 
 a 2-D (two-dimensional) array as a “matrix”, 
 or an N-D (N-dimensional, where “N” is typically an integer greater than 2) 
 array as a “tensor”.
"""
a = np.array([1,2,5,8,10])
print('Array',a)

print(a.shape)

a2 = np.array([[1,2,5,8,10], [2,4,10,16,20]])
print('2D array',a2)

print(a2.shape)


print('a[0]', a[0])
print('a2[0][1]', a2[0][1])

print('modify first element  from the first array a')
a[0] = 100
print('First Array: ', a)

print('Slice first 3 elements first-Array: ', a[:3])
print('Slice after 3 elements from first-Array and assign to new variable')

b = a[3:]
print(b)
b[0] = 80
print('modifying new sliced array first element',b)

a3 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print('3D array\n',a3)
print('3D array, a[1][2]= ',a3[1][2])