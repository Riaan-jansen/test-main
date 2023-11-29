import numpy as np
import random
import matplotlib.pyplot as plt 
import time
import Unpacker as up
import numba

# Run time test
start_t = time.time()

# no of iterations
# strn = input('Input no of tries: ')
# n = int(strn)

n = 50000
r = 1

# initialise empty sets
inside = []
outside = []

# all points outside circle get added to one list, within the circle another.
def inside_out(radius, n):
    for _ in range(n):    
        xs = random.uniform(-radius,radius)
        ys = random.uniform(-radius,radius)
        if xs**2 + ys**2 >= radius**2:
            outside.extend((xs, ys))
        else:
            inside.extend((xs, ys))
    return inside, outside


# Using number of points as proportional to area
def pi_calc(inside, outside):
    circle_area = len(inside)
    square_area = len(outside) + len(inside)
    guess_pi = 4 * (circle_area / square_area)
    return guess_pi


def pi_finder(radius, n):
    inside, outside = inside_out(radius, n)
    pi = pi_calc(inside, outside)
    return pi


inside, outside = inside_out(r, n)
in_x, in_y = up.unpacker(inside)
out_x, out_y = up.unpacker(outside)


def plotting_pi(x:list[float], y, inside_x, inside_y):
    """ Scatter plot of points. 'Circle' points are pink, outside that blue."""
    plt.scatter(x, y)
    plt.scatter(inside_x, inside_y, color='magenta')
    plt.grid()
    plt.title('Monte Carlo Method of Calculating Pi')
    plt.show()


plotting_pi(out_x, out_y, in_x, in_y)


def comparing_pi(start, stop, step, radius):
    data = []
    err_data = []
    for i in range(start, stop, step):
        x = pi_finder(radius, i)
        data.append(x)
        err = np.sqrt(((x - np.pi)**2)/(len(data)))
        err_data.append(err)
    return data, err_data

start, stop, step = 100, 100000, 1000

data, err_data = comparing_pi(start, stop, step, r)

plt.scatter(np.arange(start, stop, step), data)
plt.errorbar(np.arange(start, stop, step), data, yerr=err_data, ls='none', color='r')
plt.grid()
plt.title('Computed values of pi against number of iterations')
plt.ylabel('Pi values')
plt.xlabel('No. of iterations in simulation')
print('Pi = ', pi_finder(r, stop), '')
plt.show()


end = time.time()
elapsed = end - start_t
print('<<< Run time =', elapsed, '>>>')