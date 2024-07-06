import numpy as np

for i in range(1, 5):
    a = np.eye(4, 4, k=i, dtype=int)
    print(a)

print("---------------")

for i in range(-1, -5, -1):
    a = np.eye(4, 4, k=i, dtype=int)
    print(a)

    