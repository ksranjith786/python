import matplotlib.pyplot as plt
import numpy as np


women = np.array([5,20,40,31,17])
men = np.array([5,24,50,11,27])

x = np.arange(5)

plt.barh(x, women, height=0.5)
plt.barh(x, -men, height=0.5)

plt.show()
