import numpy as np
from numpy import random
import matplotlib.pyplot as plt


class travel():
    ''''''
    def __init__(self):
        '''defaults for stops, cycles and gaussian parameters and more.'''
        self.stops = 6
        self.trials = 120
        self.cycles = 5
        self.range = 180
        self.walkmean = 22
        self.walkdev = 2
        self.busmean = 30
        self.busdev = 3
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
        bus = random.normal(self.busmean, self.busdev)
        i = 0
        while i < self.stops:
            if random.uniform() >= 0.8:
                bus = bus + 1
                i = i + 1
        self.bustime = bus
        return bus

    def time2work(self):
        '''calculates total time taken to get to work for n trials
        '''
        time = travel.walk2bus(self) + travel.wait4bus(self) + travel.bus2work(self)
        walk = self.walktime
        wait = self.waittime
        bus = self.bustime
        t = walk + wait + bus
        return time, t


journey = travel()
time, t = travel.time2work(journey)
print("time ", time, "\nt ", t)
