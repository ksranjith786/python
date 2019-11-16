import matplotlib.pyplot as plt 
import numpy as np 

data = [
    np.random.randint(1,20,15),
    np.random.randint(1,20,15),
    np.random.randint(1,20,15)
]

[plt.plot(data[i], label=['X', 'Y', 'Z'][i], color=['lightgreen', 'lightblue', 'red'][i],
marker=['o', '^', '*'][i], markersize=10, markerfacecolor=['green', 'red', 'blue'][i], linestyle=['--', ':', '-.'][i]) for i in range(len(data))]

plt.show()