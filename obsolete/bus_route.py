# import random
import time
import numpy as np
from scipy import stats
# from scipy.stats import norm
import matplotlib.pyplot as plt


t_0 = time.time()
max = 100000
N = 500
stops = 6


def walkto_time():
    params = 6, 22, 4
    vals = stats.skewnorm(*params).rvs(N)

    return vals


def bus_time():
    params = 10, 18, 3
    vals = stats.skewnorm(*params).rvs(N)
    i = 0
    while i < stops:
        if np.random.random() >= 0.5:
            vals += 1
        i += 1
    return vals


def walkfrom_time():
    vals = np.random.randint(5, 9, N)

    return vals


def iterate(n):
    narray = []
    i = 0
    while i < stops:
        val = walkto_time() + bus_time() + walkfrom_time()
        narray.append(val)
        i = i + 1
    return narray


# vals = stats.skewnorm.cdf(x, a=30, loc=25, scale=100)
# plt.plot(vals)
# plt.show()


def get_data(n):
    """ Generates data for plotting histogram """
    data = iterate(n)
    plt.hist(data, color=['blue']*len(data))
    plt.title('Non-interdependent simulation')
    plt.grid()
    plt.legend()
    plt.xlabel('Time to get to work')
    plt.ylabel('Frequency of occurance')
    plt.show()


get_data(N)

print('<<< Run time = ', time.time() - t_0, '>>>')
