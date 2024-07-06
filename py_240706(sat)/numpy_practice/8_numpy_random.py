import numpy as np

print("seed is none")
print(np.random.seed(100))
print("rand is")
print(np.random.rand(100))
print("rand's start and stop")
print(np.random.rand(5, 3))
print("randint is")
print(np.random.randint(1, 7, size= 10))
m = 175
sigma = 10
heights = m + sigma * np.random.randn(10000)
print("mean and median test")
print(heights)
print("mean is")
print(np.mean(heights))
print("median is")
print(np.median(heights))