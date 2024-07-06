import numpy as np

a = np.empty((2, 2), dtype= int)
b = np.arange(1, 6)
c = np.empty_like(b, dtype= int) #쓰레기값 들어간거.

print(a)
print(b)
print(c)

print("----------------------")
a = np.identity(4, dtype=int)   #항등행렬(?) 만들어주는거.
b = np.eye(4, 4, k=1, dtype=int)

print(a)
print(b)