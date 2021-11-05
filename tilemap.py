import settings
import sprites


class Spawn:
    def __init__(self, x, y, tile):
        self.x = x
        self.y = y
        self.team = tile


class Map:
    def __init__(self, filename):
        with open(filename, 'rt') as rf:
            map_lenght_row = settings.HEIGHT // settings.TILESIZE
            map_lenght_column = (settings.WIDTH // settings.TILESIZE) + 1
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
                    sprites.Wall(game, col, row)
                elif tile == 'O':
                    sprites.Plane(game, col, row, game.team_orange)
                    spawn_pool.append(Spawn(col, row, tile))
                    game.max_tiles += 1
                elif tile == 'B':
                    sprites.Plane(game, col, row, game.team_blue)
                    spawn_pool.append(Spawn(col, row, tile))
                    game.max_tiles += 1
                elif tile == 'X':
                    game.max_tiles += 1
                    spawn_pool.append(Spawn(col, row, tile))
                elif tile == '.':
                    game.max_tiles += 1

        for spawn in spawn_pool:
            if spawn.team == "O":
                game.queen_orange = sprites.Queen(game, spawn.x, spawn.y, game.team_orange, game.team_blue)
            elif spawn.team == "B":
                game.queen_blue = sprites.Queen(game, spawn.x, spawn.y, game.team_blue, game.team_orange)
            elif spawn.team == "X":
                sprites.Blobs(game, spawn.x, spawn.y)

            del spawn
