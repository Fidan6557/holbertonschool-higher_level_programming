#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """Return list of True/False for numbers divisible by 2."""
    result = []

    for n in my_list:
        if n % 2 == 0:
            result.append(True)
        else:
            result.append(False)

    return result
