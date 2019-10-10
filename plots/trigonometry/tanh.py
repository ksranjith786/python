import numpy as np 
import matplotlib.pyplot as plt 

x = np.arange(0, 1*np.pi, 0.1)
# x = np.linspace(0, 10, 100)

tanhx = np.tanh(x)

plt.plot(x, tanhx)
plt.show()
