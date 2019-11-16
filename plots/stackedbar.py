import matplotlib.pyplot as plt
import numpy as np


women = np.array([5,20,40,31,17])
men = np.array([5,24,50,11,27])

x = np.arange(5)

'''
plt.bar(x+0, women, bottom=5, width=0.25)
plt.bar(x+0.25, men, bottom=10, width=0.25)

plt.show()

plt.bar(x, women, bottom=5, width=0.25)
plt.bar(x, men, bottom=10, width=0.25)

plt.show()
'''

plt.bar(x, women, bottom=0, width=0.25)
plt.bar(x, men, bottom=women, width=0.25)

plt.show()
