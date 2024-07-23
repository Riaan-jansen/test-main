'''
Finalised basic monte carlo calculating pi task
'''
from numpy import pi, random, logspace
import numpy as np
import matplotlib.pyplot as plt
import timeit


class pi_mc:
    '''monte carlo pi class. contains fucntions to calculate pi
    and constants. benefit of class is declaration of variables
    here in __init__.'''
    def __init__(self):
        '''starting values, radius and n iterations'''
        self.r = 1
        self.n = 1000000
        self.n0 = 1000
        self.nend = 1000000

    def pin_dropper(self):
        """ Creates random coordinates in separate lists
        and compares to see if in circle"""
        # initialise empty sets and constants
        r = self.r
        n = self.n
        out_x = []
        out_y = []
        in_x = []
        in_y = []

        # all points outside circle get added to one list,
        # within the circle another.
        i = 0
        while i < n:
            xs = random.uniform(-r, r)
            ys = random.uniform(-r, r)
            if xs**2 + ys**2 >= r**2:
                out_x.append(xs)
                out_y.append(ys)
            else:
                in_x.append(xs)
                in_y.append(ys)
            i = i + 1

        # only x & y for plotting, not needed
        return out_x, out_y, in_x, in_y

    def pi_calc(self):
        """ Calculates pi from random pin drops"""
        out_x, _, in_x, _ = pi_mc.pin_dropper(self)
        # Using number of points as proportional to area
        circle_area = len(in_x)
        square_area = self.n

        guess_pi = 4 * (circle_area / square_area)
        err_pi = 100 * (abs(guess_pi - pi) / pi)

        return guess_pi, err_pi

    def pi_plotter(self):
        """Scatter plot of points. 'Circle' points are pink, outside blue."""
        out_x, out_y, in_x, in_y = pi_mc.pin_dropper(self)
        guess_pi, err_pi = pi_mc.pi_calc(self)
        plt.scatter(out_x, out_y)
        plt.scatter(in_x, in_y, color='magenta')
        # plt.plot(xc, yc, color='r', ls='--')
        plt.grid()
        plt.title('Monte Carlo Method of Calculating Pi')
        print('Pi = ', guess_pi, '+/-', err_pi)
        plt.show()
        return None

    def plot_guess_accuracy(self):
        """with an array of different iteration sizes, demonstrates
        the increase in simulation accuracy with iteration increase"""
        obj = pi_mc()
        i = 0
        trials = 10
        guess_list = []
        guess_errs = []
        cycles = logspace(2.0, 6.0, num=10, base=10)
        while i < len(cycles):
            obj.n = cycles[i]
            print(cycles[i])
            j = 0
            trial_list = []
            while j < trials:
                guess_pi, err_pi = pi_mc.pi_calc(self)
                trial_list.append(guess_pi)

                j = j + 1
            i = i + 1
        # step = int((n_stop - n_start) / 1000)
        # iter_array = range(n_start, n_stop, step)

        # values = arange(pi, pi, pi/10)
        # labels = []
        # for i in values:
        #     label = 'π %.3f' % i
        #     labels.append(label)
        # plt.yticks(values, labels)
        plt.hlines(pi, 0, 1000000)
        plt.scatter(cycles, guess_list)
        plt.xscale("log")
        plt.grid()
        plt.show()
        return


class findPi():
    '''simple class finds pi. contains pinDropper, piCalc, devPi.'''
    def __init__(self):
        self.radius = 1.0
        self.trials = 50000000
        self.cycles = 1

    def pinDropper(self):
        '''returns number of pins within the circle.'''
        i = 0
        ins = 0
        while i < self.trials:
            x = random.uniform(0, self.radius)
            y = random.uniform(0, self.radius)
            if x**2 + y**2 <= (self.radius)**2:
                ins = ins + 1
            i = i + 1
        return ins

    def calcPi(self):
        '''using assumption pins inside/outside the cirlce are
        approximately equal to surface area of quadrant/square.
        returns pi.'''
        inside = findPi.pinDropper(self)
        pie = 4 * inside / self.trials
        return pie

    def devPi(self):
        '''calculates standard deviation'''
        estimates = []
        for i in range(self.cycles):
            guessPi = findPi.calcPi(self)
            estimates.append(guessPi)
        std = np.std(estimates)
        mean = sum(estimates) / len(estimates)
        reg = 0
        for i in range(self.cycles):
            reg = reg + (estimates[i] - mean)**2
        Dev = reg / float(self.cycles)
        return std, Dev, estimates


def timePi():
    SETUP_CODE = '''
from __main__ import findPi
from numpy import random
'''
    RUN_CODE = '''
Pi = findPi()
pie = findPi.calcPi(Pi)
print(f'pi = {pie}')
'''
    times = timeit.repeat(setup=SETUP_CODE,
                          stmt=RUN_CODE,
                          repeat=3,
                          number=5)
    print(f'Minimum run time {min(times):.5f}')
    print(f'Maximum run time {max(times):.5f}')


def basicTime():
    SETUP_CODE = '''
from numpy import random
'''

    RUN_CODE = '''
def func(n):
    i = 0
    ins = 0
    while i < n:
        x = random.uniform()
        y = random.uniform()
        if x**2 + y**2 <= 1:
            ins = ins + 1
        i = i + 1
    return ins


def calc(n):
    ins = func(n)
    pi = 4 * ins / n
    return pi

n = 1000000
print(f'pi = {calc(n)}')
'''
    times = timeit.repeat(setup=SETUP_CODE,
                          stmt=RUN_CODE,
                          repeat=3,
                          number=1)
    print(f'Minimum run time (func) {min(times):.5f}')
    print(f'Maximum run time {max(times):.5f}')


if __name__ == "__main__":
    timePi()
