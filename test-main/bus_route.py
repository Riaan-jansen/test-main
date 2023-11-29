import random
import time
import numpy as np
from scipy.stats import skewnorm
import matplotlib.pyplot as plt

t_0 = time.time()
min = 0
max = 1000
N = 1000

def walkto_time():
    a, loc, scale = 10, 22, 2.5
    vals = skewnorm(a, loc, scale).rvs(max)

    return int(vals[random.randint(min, max-1)])


def bus_time():
    params = 10, 16, 3
    vals = skewnorm(*params).rvs(max)
    for _ in range(6):
        if np.random.random() >= 0.5:
            vals += 0.5

    return int(vals[random.randint(min, max-1)])


def walkfrom_time():
    vals = np.random.randint(5,9, max)

    return vals[random.randint(min, max-1)]


def iterate(n):
    narray = []
    for _ in range(n):
        val = walkto_time() + bus_time() + walkfrom_time()
        narray.append(val)
    
    return narray


def get_data(n):
    """ Generates data for plotting histogram """
    data = iterate(n)
    plt.hist(data, bins = np.arange(np.min(data), np.max(data), 1))
    plt.title('Non-interdependent simulation')
    plt.grid()
    plt.xlabel('Time to get to work')
    plt.ylabel('Frequency of occurance')
    plt.show()

get_data(N)

# def gen_data(imax, n):
#     data = np.zeros(shape=n)
#     fig, ax = plt.subplots(4)

#     for i in range(imax):
#         nlen = len(iterate(n))
#         data = np.append(data, iterate(n))

#         darr = [0, 1, 2, 3]
#         darr[i] = data[i*nlen:(i+1)*nlen]
    

#         ax[i].hist(darr[i], bins = np.arange(np.min(darr[i]), np.max(darr[i]), 1))
#         ax[i].set_title('Non-interdependent simulation')
#         ax[i].grid()

#     fig.suptitle('Journey to work')
#     fig.tight_layout()

#     plt.show()

# gen_data(4, N)


print('<<< Run time = ', time.time() - t_0, '>>>')
