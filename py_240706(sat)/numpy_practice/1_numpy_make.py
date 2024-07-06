# import numpy as np

# a = np.array([1, 2, 3])

# print(a.shape)
# print(a.ndim)
# print(a.dtype)
# print(a.itemsize)
# print(a.size)
#---------------------------------

import numpy as np

array_a = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print('실습 1 : array_a =', array_a)

array_b = np.array(range(10))
print('실습 2 : array_b =', array_b)

array_c = np.array(range(0, 10, 2))
print('실습 3 : array_c =', array_c)

print('실습 4: ')
print('array_a의 shape :', array_a.shape)
print('array_a의 ndim :', array_a.ndim)
print('array_a의 dtype :', array_a.dtype)
print('array_a의 size :', array_a.size)
print('array_a의 itemsize :', array_a.itemsize)
print("--------------------------")
print('array_b의 shape :', array_b.shape)
print('array_b의 ndim :', array_b.ndim)
print('array_b의 dtype :', array_b.dtype)
print('array_b의 size :', array_b.size)
print('array_b의 itemsize :', array_b.itemsize)
print("--------------------------")
print('array_c의 shape :', array_c.shape)
print('array_c의 ndim :', array_c.ndim)
print('array_c의 dtype :', array_c.dtype)
print('array_c의 size :', array_c.size)
print('array_c의 itemsize :', array_c.itemsize)