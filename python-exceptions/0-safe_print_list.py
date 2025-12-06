#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    s = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end ="")
            s += 1
        except IndexError:
            break
    print()
    return s

my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list(my_list, 2)
print("nb_print: {:d}".format(nb_print))