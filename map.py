import pygame, sys
from chunk import SheetHandler

# (x, y) len: 13
game_map =[[(4,0), (1,2), (1,2), (2,2), None, None, None, None, None, (0,2), (1,2), (1,2), (5,0)],
           [(2,1), None, None, None, None, (3,0), None, (3,0), None, None, None, None, (0,1)],
           [(2,2), None, (0,3), (2,3), None, (3,2), None, (3,2), None, (0,3), (2,3), None, (0,2)],
           [ None, None, None, None, None, None, None, None, None, None, None, None, None ],
           [(2,4), (2,3), None, (0,3), (2,3), None, (3,3), None, (0,3), (2,3), None, (0,3), (3,4)],
           [(2,1), None, None, None, None, None, None, None, None, None, None, None, (0,1)],
           [(4,1), (1,0), (2,0), None, (0,3), (2,3), None, (0,3), (2,3), None, (0,0), (1,0), (5,1)],
           [(1,1), (1,1), (2,1), None, None, None, None, None, None, None, (0,1), (1,1), (1,1)]]

class Map(pygame.sprite.Sprite):
    def __init__(self, tile_map):
        file_img = 'TileSet.png'
        handler = SheetHandler(file_img, 512)
        self.chunk_it = handler.chunk_it
        self.tile_map = tile_map

    def construct_map(self, window_width, window_height):
        tile_size_w = window_width // len(self.tile_map[0])
        tile_size_h = window_height // len(self.tile_map)
        self.tile_size = (tile_size_w, tile_size_h)
        self.sheet_map = [[surf for surf in self.chunk_it(tiles, self.tile_size)] for tiles in self.tile_map]

        self.map = []
        for row in range(len(self.sheet_map)):
            column = []
            for col in range(len(self.sheet_map[row])):
                surf = self.sheet_map[row][col]
                if surf == None:
                    #The construction of game tiles
                    surf = pygame.Surface((self.tile_size[0], self.tile_size[1]))
                    surf.fill('#676666')
                rect = surf.get_rect(topleft = (col * self.tile_size[0], row * self.tile_size[1]))
                column.append((surf, rect))
            self.map.append(column)

pygame.init()
screen_width, screen_height = 1300, 1000
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

platform = Map(game_map)
platform.construct_map(screen_width, screen_height)
#platform_group = pygame.sprite.Group()
#platform_group.add(platform)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()

    screen.fill('#196985')

    for tiles in platform.map:
        for tile in tiles:
            surf, rect = tile
            screen.blit(surf, rect)

    pygame.display.update()
    clock.tick(60) 

