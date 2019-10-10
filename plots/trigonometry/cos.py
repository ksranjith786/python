import numpy as np 
import matplotlib.pyplot as plt 

x = np.linspace(0, 10, 100)
# x = np.arange(0, 4*np.pi, 0.1)

cosx = np.cos(x)

plt.plot(x, cosx, label='cosine curve', color='red', linestyle='solid', marker='.', markerfacecolor='yellow', markersize=10)

plt.title('Trigonometric cosine curve')
plt.legend()

plt.xlabel("rad (Radians) -->")
plt.ylabel('cos(rad) -->')

plt.show()

'''
linestyle -> ValueError: 'daa' is not a valid value for ls; supported values are '-', '--', '-.', ':', 'None', ' ', '', 'solid', 'dashed', 'dashdot', 'dotted'

'''