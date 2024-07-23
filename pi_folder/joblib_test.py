import numpy as np
import time
import random
import Unpacker as up
import matplotlib.pyplot as plt
import asyncio


# Run time test
start = time.time()

n = 100000
r = 1


def background(f):
    def wrapped(*args, **kwargs):
        return asyncio.get_event_loop().run_in_executor(
                                        None, f, *args, **kwargs)

    return wrapped


@background
def inside_out(radius, n):
    """ All points outside circle get added to one list,
    within the circle another. """
    inside = []
    outside = []

    # initialised empty sets for iterating over. Using 'prange' for parallel.
    for _ in range(n):    
        xs = random.uniform(-radius, radius)
        ys = random.uniform(-radius, radius)
        if xs**2 + ys**2 >= radius**2:
            outside.extend([xs, ys])
        else:
            inside.extend([xs, ys])
    return inside, outside


def pi_calc(inside, outside):
    """ Using number of points as proportional to area calculates pi."""
    circle_area = len(inside)
    square_area = len(outside) + len(inside)
    guess_pi = 4 * (circle_area / square_area)
    return guess_pi


loop = asyncio.get_event_loop()

looper = asyncio.gather(*[inside_out(r, n) in range(1, 4)])
results = loop.run_until_complete(looper)

inside, outside = inside_out(r, n)
in_x, in_y = up.unpacker(inside)
out_x, out_y = up.unpacker(outside)

print(pi_calc(in_x, out_x))


def plotting_pi(x:list[float], y:list[float], inside_x:list[float], inside_y:list[float]):
    """ Scatter plot of points. 'Circle' points are pink, outside that blue."""
    plt.scatter(x, y, label='Outside circle')
    plt.scatter(inside_x, inside_y, color='magenta', label='Circle')
    plt.legend()
    plt.grid()
    plt.title('Monte Carlo Method of Calculating Pi')
    plt.show()


plotting_pi(out_x, out_y, in_x, in_y)


end = time.time()
elapsed = end - start
print('<<< Run time =', elapsed, '>>>')
