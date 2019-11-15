import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 101, 1)
y1 = np.
y2 = np.log10(x)

print(y1)
print(y2)

plt.figure(figsize=(5,5))
plt.plot(x, y1)
plt.plot(x, y2)
plt.show()