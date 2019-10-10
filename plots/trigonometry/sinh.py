import numpy as np 
import matplotlib.pyplot as plt 

x = np.arange(0, 2*np.pi, 0.1)
# x = np.linspace(0, 10, 100)

sinhx = np.sinh(x)

plt.plot(x, sinhx)
plt.show()
