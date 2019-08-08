from random import *


def flipper(x):
    # flips coin x times
    results = []
    for i in range(x):
        if random() > 0.5:
            results += [1]
        else:
            results += [0]
    return results

def counter:
     