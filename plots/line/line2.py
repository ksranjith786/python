import matplotlib.pyplot as plt 
import numpy as np 

x = np.random.randint(1, 20, 10)
y = np.random.randint(1, 20, 10)
z = np.random.randint(1, 20, 10)


plt.plot(x, label='X', lw=5, marker='o', markersize=10, markerfacecolor='green', linestyle='--')
plt.xlabel('Time', fontsize=15)
plt.ylabel('Price', fontsize=15)
plt.title("Graph", fontsize=20, color='red', loc='center')
plt.legend(fontsize=10, loc=(1.05, 0.5))
plt.plot(y)
plt.plot(z)
plt.show()
