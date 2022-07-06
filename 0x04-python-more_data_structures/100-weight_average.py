#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None:
        return 0

    numerator = 0
    denominator = 0
    for tuple in my_list:
        denominator += tuple[-1]
        mult = 1
        for i in tuple:
            mult *= i
        numerator += mult

    return numerator / denominator
