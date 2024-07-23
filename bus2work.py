import time
import numpy as np
from numpy import random
import matplotlib.pyplot as plt


class travel():
    '''class contains functions to calculate: walk to bus, wait for bus, and
    bus to work times.'''
    def __init__(self):
        '''defaults for stops, mean and standard deviations and times.'''
        self.stops = 8
        self.walkmean = 22
        self.walkdev = 6
        self.busmean = 30
        self.busdev = 5
        self.walktime = 0
        self.waittime = 0
        self.bustime = 0

    def gauss(x, *params):
        ''''''
        y = np.empty_like(x, dtype=float)
        for i in range(0, len(params), 3):
            mean = params[i]
            amp = params[i+1]
            dev = params[i+2]
            y = amp * np.exp(-0.5 * ((x - mean) / dev)**2)
        return y

    def walk2bus(self):
        '''returns time to walk to bus stop, as a random value from normal
        distribution. input self object.'''
        walk = random.normal(self.walkmean, self.walkdev)
        self.walktime = walk
        return walk

    def wait4bus(self):
        ''''''
        wait = 0
        walk = self.walktime
        if walk >= 26:  # if walk is too long bus leaves!
            wait = wait + 25
        if random.uniform() >= 0.5:
            wait = wait + random.normal(5, 1)  # too many values in self
        self.waittime = wait
        return wait

    def bus2work(self):
        '''input self object. samples value from normal distribution.
        chance to add time on for every bus stop.'''
        bus = random.normal(self.busmean, self.busdev)
        i = 0
        while i < self.stops:
            if random.uniform() >= 0.8:
                bus = bus + 1
                i = i + 1
        self.bustime = bus
        return bus

    def time2work(self):
        '''calculates total time taken to get to work. one iteration'''
        travel.walk2bus(self)
        travel.wait4bus(self)
        travel.bus2work(self)
        walk = self.walktime
        wait = self.waittime
        bus = self.bustime
        total = walk + wait + bus
        return total


class getTime():
    '''class contains calculations of total time to work and iterations.
    calcTravel(self) and calcCycles(self).'''
    def __init__(self):
        '''defaults for number of trials and cycles.'''
        self.trials = 100
        self.cycles = 10

    def calcTravel(self):
        '''one cycle of n trials.'''
        bus = travel()
        n = self.trials
        times = np.empty(n, dtype=float)
        for i in range(n):
            times[i] = travel.time2work(bus)
        ntrial = times.mean()
        return ntrial

    def calcCycles(self):
        '''calls calcTravel for every m cycle.'''
        m = self.cycles
        cycles = np.empty(m, dtype=float)
        for i in range(m):
            cycles[i] = getTime.calcTravel(self)
        mu = cycles.mean()
        reg = 0
        for i in cycles:
            r = float(i - mu)
            reg = reg + r**2
        stdv = np.sqrt((reg**2) / len(cycles))
        print(f"result time = {mu:.2f} +/- {stdv}")
        return cycles, stdv

    def plotTimes(self):
        '''plots times, the results of cycles.'''
        cycles, stdv = getTime.calcCycles(self)
        err = np.ones_like(cycles) * stdv
        fig, axs = plt.subplots()
        axs.hist(cycles)
        plt.show()


gettime = getTime()
getTime.calcTravel(gettime)
cycles = getTime.calcCycles(gettime)
getTime.plotTimes(gettime)
