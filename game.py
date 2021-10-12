import pygame, sys
from os.path import exists

from pygame.locals import *
pygame.init()

if exists('data/background.png'):
    background_img = 'background.png'
else:
    print("Missing Background image")
    print("Reconfigure to black background")
    background_img = '#000000' # Black color

screen_width, screen_height = 800, 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Maniac Hive')
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            pygame.quit()
            sys.exit()

    screen.fill('#196985')

    pygame.display.update()
    clock.tick(60)
