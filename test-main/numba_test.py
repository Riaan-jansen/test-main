import concurrent.futures as mtp
import time
import numpy as np
import random
import matplotlib.pyplot as plt 
from numba import jit, prange
import threading

# All the variables (can move to be function arguments but for now easier)
n = int(1e07)
r = 1


@jit(nopython=True, parallel=True)
def pin_dropper():
    """ Creates random coordinates in separate lists and compares to see if in circle"""
    # initialise empty sets
    out_x = []
    out_y = []
    in_x = []
    in_y = []

    # all points outside circle get added to one list, within the circle another.
    for _ in range(n):    
        xs = random.uniform(-r,r)
        ys = random.uniform(-r,r)
        if xs**2 + ys**2 >= r**2:
            out_x.append(xs)
            out_y.append(ys)
        else:
            in_x.append(xs)
            in_y.append(ys)
    return out_x, out_y, in_x, in_y

@jit(nopython=True, parallel=True)
def pi_calc():

    """ Calculates pi from random pin drops"""

    out_x, _ , in_x, _ = pin_dropper()

    # Using number of points as proportional to area
    circle_area = len(in_x)
    square_area = len(out_x) + len(in_x)

    guess_pi = 4 * (circle_area / square_area)
    err_pi = 100 * (abs(guess_pi - np.pi) / np.pi)

    print(' --- pi = ', guess_pi, ' +/- ', err_pi , '%.')
    
    return guess_pi, err_pi


def threaded_pi():
    with mtp.ThreadPoolExecutor(max_workers=8) as executor:
        future = executor.submit(pi_calc)
    return future

t_0 = time.time()
pi_calc()
print('<<< Run time = ', time.time()-t_0, '>>>')

t_1 = time.time()
threaded_pi()
print('<<< Run time = ', time.time()-t_1, '>>>')
