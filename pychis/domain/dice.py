import random

class Dice(object):

    def throw(self):
        return random.randint(1, 6)

