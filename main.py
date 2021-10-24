import pygame, sys
from os import path
from settings import *
from sprites import *

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.load_data()

    def load_data(self):
        game_directory = path.dirname(__file__)
        with open(path.join(game_directory, 'map.txt'), 'rt') as rf:
            map_lenght_row = HEIGHT // TILESIZE
            map_lenght_column = (WIDTH // TILESIZE) + 1 # +1 is for \n
            self.map_data = [rf.read(map_lenght_column) for _ in range(0, map_lenght_row)]

    def new(self):
        # initialize all variables and do all the setup for a new game
        self.all_sprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()

        #Team Groups
        self.team_orange = pygame.sprite.Group()
        self.team_blue = pygame.sprite.Group()
        self.unknowns = pygame.sprite.Group()

        for row, tiles in enumerate(self.map_data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    Wall(self, col, row)
                elif tile == 'O':
                    self.queen = Queen(self, col, row, self.team_orange)
                elif tile == 'B':
                    self.queen = Queen(self, col, row, self.team_blue)
                elif tile == 'X':
                    self.blob = Blobs(self, col, row)

    def run(self):
        # Game loop - set self.playing = False to end the game
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pygame.quit()
        sys.exit()
    
    def update(self):
        # Update portion of the game loop
        self.all_sprites.update()

    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pygame.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pygame.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def draw(self):
        self.screen.fill(BGCOLOR)
        self.draw_grid()
        self.all_sprites.draw(self.screen)
        pygame.display.flip()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.quit()
            
            #to move Queen self.queen.move(dx=1) 

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass

#Create the game Instance
g = Game()
g.show_start_screen()
while True:
    g.new()
    g.run()
    g.show_go_screen()

