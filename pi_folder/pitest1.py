import numpy as np
import random
from numba import jit, prange
import time


n = 100000
r = 1


@jit(nopython=True, parallel=True)
def pin_dropper_nb():
    """ Numba - Creates random coordinates in separate lists
      and compares to see if in circle"""
    # initialise empty sets
    out_x = []
    out_y = []
    in_x = []
    in_y = []

    # all points outside circle get added to one list,
    # within the circle another.
    for _ in prange(n):
        xs = random.uniform(-r, r)
        ys = random.uniform(-r, r)
        if xs**2 + ys**2 >= r**2:
            out_x.append(xs)
            out_y.append(ys)
        else:
            in_x.append(xs)
            in_y.append(ys)

    return out_x, out_y, in_x, in_y


@jit(nopython=True)
def pi_calc_nb():
    """ Numba - Calculates pi from random pin drops"""

    out_x, _, in_x, _ = pin_dropper_nb()
    # Using number of points as proportional to area
    circle_area = len(in_x)
    square_area = len(out_x) + len(in_x)

    guess_pi = 4 * (circle_area / square_area)
    err_pi = 100 * (abs(guess_pi - np.pi) / np.pi)

    # print(' --- pi = ', guess_pi, ' +/- ', err_pi, '%.')

    return guess_pi, err_pi


t_0 = time.time()
pi, _ = pi_calc_nb()
print(pi)
print('<<< Run time = ', time.time()-t_0)


t_0 = time.time()
pi, _ = pi_calc_nb()
print(pi)
print('<<< Run time = ', time.time()-t_0)
