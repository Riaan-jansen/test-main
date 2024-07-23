import numpy as np
import matplotlib.pyplot as plt


def gauss(x, params):
    ''''''
    y = np.empty_like(x, dtype=float)

    mean = params[0]
    amp = params[1]
    dev = params[2]
    y = amp * np.exp(-0.5 * ((x - mean) / dev)**2)
    return y


x = np.arange(-5, 5, 0.1)
params = [0, 1, 1]
y = gauss(x, params)

for i, ele in enumerate(y):
    

plt.plot(x, y)
plt.show()
