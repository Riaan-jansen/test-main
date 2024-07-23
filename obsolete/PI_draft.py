import numpy as np
import random
import matplotlib.pyplot as plt
import time

# Run time test
start = time.time()

# no of iterations
# strn = input('Input no of tries: ')
# n = int(strn)

n = 1000
r = 1

# initialise empty sets
x = []
y = []
inside_x = []
inside_y = []

# all points outside circle get added to one list, within the circle another.
for i in range(n):    
    xs = random.uniform(-r,r)
    ys = random.uniform(-r,r)
    if xs**2 + ys**2 >= r**2:
        x.append(xs)
        y.append(ys)
    else:
        inside_x.append(xs)
        inside_y.append(ys)


# def circle(t):
#     y = np.cos(t)
#     x = np.sin(t)
#     return (x,y)
# theta = np.arange(0, 2*np.pi, 0.001)
# xc, yc = circle(theta)

# Using number of points as proportional to area
circle_area = len(inside_x)
square_area = len(x) + len(inside_x)

guess_pi = 4 * (circle_area / square_area)
print('\n --- pi = ', guess_pi)

def stdev(val, n):
    err = ((val - np.pi)**2 / n-1)**0.5
    return err

# Scatter plot of points. 'Circle' points are pink, outside that blue.
plt.scatter(x, y)
plt.scatter(inside_x, inside_y, color='magenta')
#plt.plot(xc, yc, color='r', ls='--')
plt.grid()
plt.title('Monte Carlo Method of Calculating Pi')
print('Pi = ', guess_pi, ' +/- ', stdev(guess_pi, n))
plt.show()


end = time.time()
elapsed = end - start
print('<<< Run time =', elapsed, '>>>')
