import unittest
from math import ceil
from settings import WIN_PERCENTAGE
from main import Game

class TestWinning(unittest.TestCase):
    def test_win(self):
        """
            Win percentage = 65%
            Suppose max_tiles = 100 then 0.65*100 = 
        """
        self.max_tiles = 100
        score = int(ceil(WIN_PERCENTAGE*100))
        Game.win(self, score)

