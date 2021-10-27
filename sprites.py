import pygame
from settings import *

class Wall(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class Plane(pygame.sprite.Sprite):
    def __init__(self, game, x, y, team):
        self.groups = game.all_sprites, team
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        color = PLANE_ORANGE if self.game.team_orange == team else PLANE_BLUE
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class Queen(pygame.sprite.Sprite):
    def __init__(self, game, x, y, team):
        self.groups = game.all_sprites, team
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.team = team
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        color = BLUE if team == game.team_blue else ORANGE
        self.image.fill(color)
        self.rect = self.image.get_rect()
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
            Plane(self.game, self.x, self.y, self.team)
            self.possible_dir = self.possible_moves()
        else:
            raise NameError('Invalid move in cardinal direction')

    def possible_moves(self) -> list:
        moves = []
        for item in self.compas:
            dx, dy = self.compas[item]
            ax, ay = dx + self.x, dy + self.y
            #print(dx, dy ,item, ax, ay)
            if not self.rect.collidepoint(ax, ay):
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
