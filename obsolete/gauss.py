import numpy as np
import matplotlib.pyplot as plt


def gauss(x, mean, dev):
	y = (1/(dev*2*np.pi))*np.exp(-0.5*((x-mean)/(dev))**2)
	return y

n = 3000

x = np.random.uniform(-100, 100, size=n)

y = gauss(x, 0, 10) * np.random.random(size=n)

plt.scatter(x, y)
plt.show()

for i in y:
    count = 0
    if i >= 50:
        count = count + 1
    if i <= -50:
        count = count + 1


print(count)

print(f'one in a {(count/len(y))}')
