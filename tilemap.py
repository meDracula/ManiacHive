import pygame
from settings import *
from sprites import *

class Spawn:
    def __init__(self, x, y, tile):
        self.x = x
        self.y = y
        self.team = tile

class Map:
    def __init__(self, filename):
        with open(filename, 'rt') as rf:
            map_lenght_row = HEIGHT // TILESIZE
            map_lenght_column = (WIDTH // TILESIZE) + 1 # +1 is for \n
            data = [rf.read(map_lenght_column) for _ in range(0, map_lenght_row)]
        self.data = data

    def new(self, game):
        """
            Converts map data to objects
        """
        spawn_pool = []
        game.max_tiles = 0
        for row, tiles in enumerate(self.data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    Wall(game, col, row)
                elif tile == 'O':
                    Plane(game, col, row, game.team_orange)
                    spawn_pool.append(Spawn(col, row, tile))
                    #game.queen_orange = Queen(game, col, row, game.team_orange, game.team_blue)
                    game.max_tiles += 1
                elif tile == 'B':
                    Plane(game, col, row, game.team_blue)
                    spawn_pool.append(Spawn(col, row, tile))
                    game.max_tiles += 1
                elif tile == 'X':
                    game.max_tiles += 1
                    spawn_pool.append(Spawn(col, row, tile))
                elif tile == '.':
                    game.max_tiles += 1

        for spawn in spawn_pool:
            if spawn.team == "O":
                game.queen_orange = Queen(game, spawn.x, spawn.y, game.team_orange, game.team_blue)
            elif spawn.team == "B":
                game.queen_blue = Queen(game, spawn.x, spawn.y, game.team_blue, game.team_orange)
            elif spawn.team == "X":
                Blobs(game, spawn.x, spawn.y)

            del spawn 

