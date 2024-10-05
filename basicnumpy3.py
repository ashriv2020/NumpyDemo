#create a basic array
import numpy as np

a = np.zeros(2)
print('zero array:', a)
a1 = np.ones(3)
print('ones array:', a1)
a1_2 = np.ones(3, dtype=np.int64)
print('ones array2:', a1_2)

a1_3 = np.zeros(6) + 2
print('ones array3:', a1_3)

a2 = np.arange(4)
print('range of elements array:', a2)

#You can also use np.linspace() to create an array with values that are spaced linearly in
#  a specified interval:
a3_1 = np.linspace(0, 10, num=5)
print('linspace array1:', a3_1)
a3_2 = np.linspace(0, 10, num=3)
print('linspace array2:', a3_2)
a3_3 = np.linspace(0, 10, num=4)
print('linspace array3:', a3_3)

#Adding, removing, and sorting element
arr1 = np.array([2, 1, 5, 3, 7, 4, 6, 8])
asc_sort = np.sort(arr1)
print('Array before sorting:\n', arr1)
print('Array after sorting:\n', asc_sort)

arr2 = np.array([12, 11, 15, 13, 17, 14, 16, 9])
#arr1_arr2_concat = np.concatenate(arr1, arr2) 
# TypeError: only integer scalar arrays can be converted to a scalar index

arr1_arr2_concat = np.concatenate((arr1, arr2))
print('concatenated sorted array:\n', np.sort(arr1_arr2_concat))

x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6]])
print(np.concatenate((x, y), axis=0))

q = np.arange(1,6)
#strides example ::2
# print(q[::2,1])

#array index



