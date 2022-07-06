#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None:
        return None

    keys = [key for key in a_dictionary]

    for i, key in enumerate(keys):
        if i == 0:
            bestScore = key
        else:
            if a_dictionary[key] > a_dictionary[bestScore]:
                bestScore = key
    return bestScore
