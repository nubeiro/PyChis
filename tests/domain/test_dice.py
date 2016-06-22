import unittest

from pychis.domain.dice import Dice


class DiceTest(unittest.TestCase):

    def test_throw_a_dice_returns_a_number_from_one_to_six(self):
        dice = Dice()

        for times in range(100):
            result = dice.throw()
            self.assertTrue(6 >= result >= 1)

