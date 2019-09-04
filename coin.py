from random import *


class Coin:
    def __init__(self):
        self.results = []
        self.dict = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0}

    def flipper(self, x):
        # flips coin x times
        results = []
        for i in range(x):
            if random() > 0.5:
                results += [1]
            else:
                results += [0]
            self.results = results
        return results

    def count(self):
        def count_helper(array):
            counter = 0
            base = array[0]
            for i in array[1:]:
                return 5

        count_helper(self.results)

