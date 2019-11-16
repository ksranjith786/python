import matplotlib.pyplot as plt 
import numpy as np 

x = np.random.randint(1, 100, 20)
y = np.random.randint(1, 100, 20)

plt.scatter(x, y)
plt.show()