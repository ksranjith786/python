import numpy as np 
import matplotlib.pyplot as plt 

x = np.arange(0, 4*np.pi, 0.1)
# x = np.linspace(0, 10, 100)

sinx = np.sin(x)

plt.plot(x, sinx)
plt.show()
