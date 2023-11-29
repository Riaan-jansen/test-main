import numpy
import matplotlib.pyplot as plt


def reader():
    skip_list = []

    file = input('Type filename')
    open(file, 'r')

    for i, line in enumerate(file):
        line = line.split()
        if line[0] == '#':
            skip_list.append(i)
    for i, line in enumerate(file):
        if i not in skip_list:
            line = line.split(' ')
            print(line)

reader()