import pygame
from settings import *

class Wall(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class Plane(pygame.sprite.Sprite):
    def __init__(self, game, x, y, Team):
        self.groups = game.all_sprites, Team.tiles
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.rect = self.image.get_rect()
        self.image.set_alpha(60)
        pygame.draw.rect(self.image, Team.plane_color, self.rect, TILESIZE_OFFSET)

        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class Queen(pygame.sprite.Sprite):
    def __init__(self, game, x, y, Team):
        self.groups = game.all_sprites, Team.objects
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.team = Team
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(Team.color)
        self.rect = pygame.rect.Rect((x + TILESIZE_OFFSET, y + TILESIZE_OFFSET), (TILESIZE - TILESIZE_OFFSET, TILESIZE - TILESIZE_OFFSET))
        #self.rect = self.image.get_rect()
        self.x = x 
        self.y = y

        self.compas = {'East':(-1,0), 'West':(1,0),'North':(0,-1), 'South': (0,1)}
        self.possible_dir = self.possible_moves()
    
    def move(self, cardinal_dir):
        assert cardinal_dir in self.compas.keys(), 'NameError of cardinal direction'
        if cardinal_dir in self.possible_dir:
            dx, dy = self.compas[cardinal_dir]
            self.x += dx
            self.y += dy

            collision_team =  pygame.sprite.spritecollide(self, self.team.tiles, False)
            print("collision team: ", collision_team)
            if pygame.sprite.spritecollide(self, self.team.tiles, False):
                pass
            else:
                print("Creating Plane...")
                Plane(self.game, self.x, self.y, self.team)
            self.possible_dir = self.possible_moves()
        else:
            raise NameError('Invalid move in cardinal direction')

    def possible_moves(self) -> list:
        moves = []
        def close_wall(walls):
            for wall in self.game.walls:
                if (-2 < (wall.x - self.x) < 2) and (-2 < (wall.y - self.y) < 2):
                    yield ((wall.x - self.x), (wall.y - self.y))

        walls_list = [wall for wall in close_wall(self.game.walls)]
        for item in self.compas:
            dx, dy = self.compas[item]
            if not ((dx,dy) in walls_list):
                moves.append(item) 
        return moves

    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE

class Blobs(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.unknowns
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(MAGENTA)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y

    def captured(self):
        pass

    def move(self, dx=0, dy=0):
        self.x += dx
        self.y += dy

    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE
