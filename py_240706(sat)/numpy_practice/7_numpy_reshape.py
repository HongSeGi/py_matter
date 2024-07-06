import numpy as np

y = np.arange(12)
print(y)

y = y.reshape(3, 4)
print(y)

y = y.reshape(6, -1)
print(y)

# y = y.reshape(5, -1)
# print(y)

y = y.flatten()
print(y)