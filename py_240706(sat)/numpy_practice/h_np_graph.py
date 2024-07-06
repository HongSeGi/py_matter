import numpy as np
import matplotlib.pyplot as plt

x = [i for i in range(100)]
y = [i**2 for i in range(100)]
z = [100*np.sin(3.14*i/100) for i in range(100)]

plt.subplot(221)
plt.plot(x,y,x,z)

plt.subplot(222)
plt.plot(x)
plt.subplot(223)
plt.plot(y)
plt.subplot(224)
plt.plot(z)
plt.show()

result = np.corrcoef([x, y, z])
print(result)