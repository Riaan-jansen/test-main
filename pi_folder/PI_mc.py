'''
Finalised basic monte carlo calculating pi task
'''
from numpy import pi, random, arange
import matplotlib.pyplot as plt
import time


class mc():
    def __init__(self):
        self.radius = 1
        self.trials = 1000000


def pin_dropper(n, r):
    """ Creates random coordinates in separate lists
    and compares to see if in circle"""
    # initialise empty sets
    out_x = []
    out_y = []
    in_x = []
    in_y = []
    # all points outside circle get added to one list,
    # within the circle another.
    for _ in range(n):
        xs = random.uniform(-r, r)
        ys = random.uniform(-r, r)
        if xs**2 + ys**2 >= r**2:
            out_x.append(xs)
            out_y.append(ys)
        else:
            in_x.append(xs)
            in_y.append(ys)
        return out_x, out_y, in_x, in_y


def pi_calc(n, r):
    """ Calculates pi from random pin drops"""
    out_x, _, in_x, _ = pin_dropper(n, r)
    # Using number of points as proportional to area
    circle_area = len(in_x)
    square_area = len(out_x) + len(in_x)
    guess_pi = 4 * (circle_area / square_area)
    err_pi = 100 * (abs(guess_pi - pi) / pi)

    return guess_pi, err_pi


def pi_plotter(n, r):
    """Scatter plot of points. 'Circle' points are pink, outside blue."""
    out_x, out_y, in_x, in_y = pin_dropper(n, r)
    guess_pi, err_pi = pi_calc(n, r)
    plt.scatter(out_x, out_y)
    plt.scatter(in_x, in_y, color='magenta')
    # plt.plot(xc, yc, color='r', ls='--')
    plt.grid()
    plt.title('Monte Carlo Method of Calculating Pi')
    print('Pi = ', guess_pi, '+/-', err_pi)
    plt.show()
    return None


def plot_guess_accuracy(n_start, n_stop, r):
    """with an array of different iteration sizes, demonstrates
    the increase in simulation accuracy with iteration increase"""
    step = int((n_stop - n_start) / 50)
    iter_array = range(n_start, n_stop, step)
    guess_list = []
    guess_errs = []
    for n in iter_array:
        guess_pi, err_pi = pi_calc(n, r)
        guess_list.append(guess_pi)
        guess_errs.append(err_pi)
    values = arange(pi, pi, pi/10)
    labels = []
    for i in values:
        label = 'π %.3f' % i
        labels.append(label)
    plt.yticks(values, labels)
    plt.scatter(iter_array, guess_list)
    plt.grid()
    plt.show()
    return iter_array, guess_list, guess_errs


obj = mc()
start = time.time()
n0 = 1000
nend = 100000
pi_plotter(obj.trials, obj.radius)
plot_guess_accuracy(n0, nend, obj.radius)

end = time.time()
elapsed = end - start
print('<<< Run time =', elapsed, '>>>')
