import matplotlib.pyplot as plt 
import numpy as np 

x = np.random.randint(1, 100, 20)
y = np.random.randint(1, 100, 20)

area = np.random.randint(1, 100, 20) ** 2
color = np.random.randint(1, 100, 20)

plt.scatter(x, y, s = area, c = color, marker='o', edgecolors='k', lw=2)
plt.show()