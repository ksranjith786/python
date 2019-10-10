import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    plt.figure(figsize=(10, 10))
    plt.plot(range(5), lw=2, label='Real')
    plt.title('Prediction')
    plt.legend(loc="best")
    plt.draw()
    plt.show()
    print("---Plot graph finish---")