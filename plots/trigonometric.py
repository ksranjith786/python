import numpy as np 
import matplotlib.pyplot as plt 

x = np.arange(0, 4*np.pi, 0.1)
sinx = np.sin(x)
cosx = np.cos(x)

#print(x, sinx)

plt.plot(x, sinx)
plt.plot(x, cosx)
plt.legend()
plt.show()
