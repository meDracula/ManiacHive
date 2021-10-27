import pygame
import random

class PlayerHandler:
    def __init__(self):
        self.action_timer = pygame.USEREVENT + 1
        pygame.time.set_timer(self.action_timer, 1000) #event, x milliseconds

    def move(self, game):
        direction = random.choice(game.queen_orange.possible_dir)
        game.queen_orange.move(direction)
        print(game.queen_orange.x,game.queen_orange.y, direction)

