import numpy as np
import random
import matplotlib.pyplot as plt 
import time
import Unpacker as up
from numba import njit, prange
import threading



# Run time test
start = time.time()

n = 100000
r = 1



@njit(parallel=True)
def inside_out(radius, n):
    """ All points outside circle get added to one list, within the circle another. """
    inside = np.empty(shape=n, dtype=np.float64)
    outside = np.empty(shape=n, dtype=np.float64)

    # initialised empty sets for iterating over. Using 'prange' for parallel.
    for _ in prange(n):    
        xs = random.uniform(-radius,radius)
        ys = random.uniform(-radius,radius)
        if xs**2 + ys**2 >= radius**2:
            outside = np.append(outside, [xs, ys])
        else:
            inside = np.append(inside, (xs, ys))
    return inside, outside


def pi_calc(inside, outside):
    """ Using number of points as proportional to area calculates pi."""
    circle_area = len(inside)
    square_area = len(outside) + len(inside)
    guess_pi = 4 * (circle_area / square_area)
    return guess_pi


inside, outside = inside_out(r, n)
in_x, in_y = up.unpacker(inside)
out_x, out_y = up.unpacker(outside)


def plotting_pi(x:list[float], y, inside_x, inside_y):
    """ Scatter plot of points. 'Circle' points are pink, outside that blue."""
    plt.scatter(x, y)
    plt.scatter(inside_x, inside_y, color='magenta')
    plt.grid()
    plt.title('Monte Carlo Method of Calculating Pi')
    plt.show(BlockingIOError)


plotting_pi(out_x, out_y, in_x, in_y)


pi_calc(inside, outside)


end = time.time()
elapsed = end - start
print('<<< Run time =', elapsed, '>>>')