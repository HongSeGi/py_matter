import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.array([[1-1j, 2-1j], [3, 4]])
c = np.array([[1, 3], [2, 4]])
d = np.array([[1, 3], [2, 4]])

ma = np.mat(a).T
mb = np.mat(b).H
mc = np.mat(c).I
md = np.mat(d).A

print(ma)
print(mb)
print(mc)
print(md)

print(type(ma))
print(type(mb))
print(type(mc))
print(type(md))