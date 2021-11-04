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
    def __init__(self, game, x, y, Team, opponent):
        self.groups = game.all_sprites, Team.objects
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.unit = 1
        self.game = game
        self.team = Team
        self.opponent_team = opponent
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(Team.color)
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

            #No collision
            if not self.sprite_collision(self.team.tiles):
                Plane(self.game, self.x, self.y, self.team)

            #Opponent tile collision
            if self.sprite_collision(self.opponent_team.tiles, True):
                Plane(self.game, self.x, self.y, self.team)

            #Capture blob
            self.sprite_collision(self.game.unknowns, capture=True)

            self.possible_dir = self.possible_moves()
        else:
            raise NameError('Invalid move in cardinal direction')

    def possible_moves(self) -> list:
        moves = []
        def close_obstructions(obstructions):
            for obs in obstructions:
                if (-2 < (obs.x - self.x) < 2) and (-2 < (obs.y - self.y) < 2):
                    yield ((obs.x - self.x), (obs.y - self.y))

        objects_list = self.game.walls.sprites() + self.opponent_team.objects.sprites()
        obstruction_list = [obstruction for obstruction in close_obstructions(objects_list)]
        for item in self.compas:
            dx, dy = self.compas[item]
            if not ((dx,dy) in obstruction_list):
                moves.append(item) 
        return moves

    def sprite_collision(self, sprites: list, destroy=False, capture=False):
        for sprite in sprites:
            if self.x == sprite.x and self.y == sprite.y:
                if destroy:
                    sprite.kill()
                elif capture:
                    self.team.objects.add(sprite)
                    sprite.opponent_team = self.opponent_team
                    self.game.unknowns.remove(sprite)
                return True
        return False

    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE

class Blobs(pygame.sprite.Sprite):
    _unit = 1
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.unknowns
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.unit = Blobs.assign_unit()

        self.game = game
        
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(MAGENTA)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y

        self.opponent_team = None
        self.compas = {'East':(-1,0), 'West':(1,0),'North':(0,-1), 'South': (0,1)}
        self.possible_dir = self.possible_moves()
        print(self.possible_dir)

    @classmethod
    def assign_unit(cls):
        cls._unit += 1
        return cls._unit

    def move(self, cardinal_dir):
        assert cardinal_dir in self.compas.keys(), 'NameError of cardinal direction'
        if cardinal_dir in self.possible_dir:
            dx, dy = self.compas[cardinal_dir]
            self.x += dx
            self.y += dy

            self.possible_dir = self.possible_moves()
        else:
            raise NameError('Invalid move in cardinal direction')

    def possible_moves(self) -> list:
        moves = []
        def close_obstructions(obstructions):
            for obs in obstructions:
                if (-2 < (obs.x - self.x) < 2) and (-2 < (obs.y - self.y) < 2):
                    yield ((obs.x - self.x), (obs.y - self.y))

        objects_list = self.game.walls.sprites() 
        if self.opponent_team != None:
            objects_list += self.opponent_team.objects.sprites()
        obstruction_list = [obstruction for obstruction in close_obstructions(objects_list)]
        for item in self.compas:
            dx, dy = self.compas[item]
            if not ((dx,dy) in obstruction_list):
                moves.append(item) 
        return moves

    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE

