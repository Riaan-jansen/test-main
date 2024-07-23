import random
import numpy as np

x = random.uniform(0, 1)

print(x)

# test Game A
total = 1000
range = np.arange(0, 1000000, 1)


for i in range:
    if random.uniform(0, 1) <= 0.49:
        total = total + 1
    else:
        total = total - 1
i = i + 1

print(total)

# Game B
t = 1000

for i in range:
    if t % 3 == 0:
        if random.uniform(0, 1) <= 0.09:
            t = t + 1
        else:
            t = t - 1
    else:
        if random.uniform(0, 1) <= 0.74:
            t = t + 1
        else:
            t = t - 1
i = i + 1

print(t)

x = np.random.randint(0, 10, 10)

splice_x = x[3:5]
print(x)
print(splice_x)

sum = np.sum(splice_x)
print(sum)
