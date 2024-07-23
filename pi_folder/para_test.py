import timeit

code_setup = '''
import concurrent.futures as mtp
import numpy as np
import random
from numba import jit, prange

n = 5000000
r = 1
'''

code_pins = '''
def pin_dropper():
    """ Creates random coordinates in separate lists
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
'''


code_pi = '''
def pi_calc():
    """ Calculates pi from random pin drops"""

    out_x, _, in_x, _ = pin_dropper()
    # Using number of points as proportional to area
    circle_area = len(in_x)
    square_area = len(out_x) + len(in_x)

    guess_pi = 4 * (circle_area / square_area)
    err_pi = 100 * (abs(guess_pi - np.pi) / np.pi)

    return guess_pi, err_pi
'''

code_thread = '''
def threaded_pi():
    with mtp.ThreadPoolExecutor(max_workers=4) as executor:
        executor.submit(pi_calc)
'''

code_decor_drop = '''
@jit(nopython=True)
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
'''
code_decor_pi = '''
@jit(nopython=True)
def pi_calc_nb():
    """ Numba - Calculates pi from random pin drops"""

    out_x, _, in_x, _ = pin_dropper_nb()
    # Using number of points as proportional to area
    circle_area = len(in_x)
    square_area = len(out_x) + len(in_x)

    guess_pi = 4 * (circle_area / square_area)
    err_pi = 100 * (abs(guess_pi - np.pi) / np.pi)

    return guess_pi, err_pi
'''


control = code_pins + code_pi
thread = code_pins + code_pi + code_thread
decorator = code_decor_drop + code_decor_pi


list = timeit.repeat(setup=code_setup,
                     stmt=control,
                     repeat=5,
                     number=1000000)


average = sum(list)/len(list)
print('Control time = ', average)


thr_list = timeit.repeat(setup=code_setup,
                         stmt=thread,
                         repeat=5,
                         number=1000000)


thr_average = sum(thr_list)/len(thr_list)
print('Threaded time = ', thr_average)


decor_list = timeit.repeat(setup=code_setup,
                           stmt=decorator,
                           repeat=5,
                           number=1000000)

decor_average = sum(decor_list)/len(decor_list)
print('Decorated time = ', decor_average)
