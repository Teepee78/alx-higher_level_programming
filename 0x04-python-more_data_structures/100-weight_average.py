#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None:
        return 0

    numerator = None
    denominator = None
    for tuple in my_list:
        if denominator is None:
            denominator = tuple[-1]
        else:
            denominator += tuple[-1]

        mult = 1
        for i in tuple:
            mult *= i

        if numerator is None:
            numerator = mult
        else:
            numerator += mult

    return numerator / denominator

my_list = [(1, 2), (2, 1), (3, 10), (4, 2)]
# = ((1 * 2) + (2 * 1) + (3 * 10) + (4 * 2)) / (2 + 1 + 10 + 2)
result = weight_average(my_list)
print("Average: {:0.2f}".format(result))
