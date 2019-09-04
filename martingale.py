from random import randrange


class Martingale:
    def __init__(self, start):
        self.money = start

    def roll(self, bet):
        x = randrange(37)
        if x <= 18:
            self.money -= bet
            print(self.money)
        else:
            self.money += bet
            print(self.money)

    def martingale(self):
        print(self.money)
        while self.money < 110:
            self.roll(1)
        print(self.money)


a = Martingale(100)
a.martingale()

"""
looks like martingale, if it doesn't enter a hot streak early on and win
will go on a spiral down into negatives very fast, very aggressively 
because of the slightly negative expected value of the roulette table biasing
it downwards at large ranges

I do wonder how well this holds up with a neutral expected value with no biasing, 
and how comfortably you can do this in the real world
Conclusion is probably that realistically, you'll never hit a lose streak that bad
But you'll also not be able to roll enough times to keep yourself in the clear 

***I FORGOT TO INCLUDE THE DOUBLING OF LOSING BETS, MY BAD, will return later for that
"""