import numpy as np

arr = np.array([[1], [2], [3]])

expansion = np.expand_dims(arr, axis=0)
reduction = np.squeeze(arr, axis=1)

print(arr)
print(expansion)
print(reduction)
print("-------------------")

arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

expand_dims = np.reshape(arr, (1, 1, 2, 4))
reduction = np.reshape(arr, (4, -1))

print(arr)
print(expand_dims)
print(reduction)