import pygame
from settings import *
from sprites import *

class Map:
    def __init__(self, filename):
        #TODO remove +1 and not read \n and ensure it only reads the decide row and column lenght
        with open(filename, 'rt') as rf:
            map_lenght_row = HEIGHT // TILESIZE
            map_lenght_column = (WIDTH // TILESIZE) + 1 # +1 is for \n
            data = [rf.read(map_lenght_column) for _ in range(0, map_lenght_row)]
        self.data = data

    def new(self, game):
        """
            Converts map data to objects
        """
        for row, tiles in enumerate(self.data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    Wall(game, col, row)
                elif tile == 'O':
                    game.queen = Queen(game, col, row, game.team_orange)
                elif tile == 'B':
                    game.queen = Queen(game, col, row, game.team_blue)
                elif tile == 'X':
                    game.blob = Blobs(game, col, row)