import numpy as np 
import matplotlib.pyplot as plt 

x = np.arange(0, 1*np.pi, 0.1)
# x = np.linspace(0, 10, 100)

coshx = np.cosh(x)

plt.plot(x, coshx)
plt.show()
