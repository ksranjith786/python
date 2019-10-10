import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
# print(x)
plt.plot(x, np.sin(x)/np.cos(x))
# plt.plot(x, np.tan(x))

plt.show()