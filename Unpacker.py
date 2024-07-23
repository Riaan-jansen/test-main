# file for functions
import argparse
import re


class Class():
    def __init__(self):
        self.cycles = 5

    def loop(self):
        for i in range(1, self.cycles):
            print(i)


def unpacker(list):
    """ Unpacks a list from (x0, y0, ... , xn, yn) into
    (x0, ... , xn) ... """

    list_odd = list[0::2]
    list_even = list[1::2]
    if len(list_odd) != len(list_even):

        return 'Error', 'Put in pairs'
    else:

        return list_odd, list_even


def text_reader(fname):
    """ opens a file and returns contents """
    f = open(fname)
    lines = []
    for line in f:
        print(line.strip())
        lines.append(line)
    f.seek(0)

    return lines


def line_checker(fname):
    """ takes a file and checks for lines over 80 chars and tabs"""
    clist = []
    tlist = []
    scan = []
    f = open(fname)
    n = sum(1 for line in f)
    f.seek(0)

    for line in f:
        if len(line) >= 81:
            clist.append(1)
        else:
            clist.append(0)

    for i in range(n):
        if clist[i] == 1:
            print('line', i+1, 'is overfull.')
    f.seek(0)

    lines = text_reader('text.txt')

    for i in range(n):
        scan.append(re.search('\t', lines[i]))
    for i in range(n):
        if scan[i] is not None:
            tlist.append(i)
            print('line', i+1, 'has a tab.')

    return clist, tlist


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="""take an input file name
                                    and will print out the line numbers of
                                    lines more than 80 characters long,
                                    and lines with tabs""")
    parser.add_argument("filepath", nargs='?', type=str)
    args = parser.parse_args()
