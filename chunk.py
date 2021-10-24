import pygame, sys
import os

class SheetHandler:
    def __init__(self, file_sheet, sprite_size):
        self.sheet = pygame.image.load(file_sheet).convert_alpha()
        self.sprite_size = sprite_size

    def chunk_it(self, tiles_cordinate, size: tuple):
        for cord in tiles_cordinate:
            if cord == None: 
                center_x, center_y = cord
                center_x += (size[0] // 2)
                center_y += (size[1] // 2)
                yield None
                continue
            x, y = cord
            x *= self.sprite_size
            y *= self.sprite_size
            image = self.sheet.subsurface(pygame.Rect((x,y), (self.sprite_size, self.sprite_size)))
            image = pygame.transform.scale(image, (size[0], size[1]))
            yield image

