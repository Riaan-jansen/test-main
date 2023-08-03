""" Unpacks a list from (x0, y0, ... , xn, yn) into (x0, ... , xn) ... """

def unpacker(list):
    list_odd = list[0::2]
    list_even = list[1::2]
    if len(list_odd) != len(list_even):
        return 'Error', 'Bad'
    else:
        return list_odd, list_even
