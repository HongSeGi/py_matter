import numpy as np

arr = np.arange(1, 5)

print(arr)
print(arr[np.newaxis])
print(arr[:, np.newaxis])

print("------------------")

arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])

print(arr1[np.newaxis] * arr2)
print(arr1[:, np.newaxis] * arr2)
print("\n")
print(arr1[np.newaxis] + arr2)
print(arr1[:, np.newaxis] + arr2)