import unittest
from main import Game
from sprites import Queen

class PlayerTest(unittest.TestCase):
    def testTeamOrangeQueen(self):
        team_orange = game.team_orange
        print("We are the world")
        print(team_orange.sprites)

if __name__ == '__main__':
    unittest.main()
