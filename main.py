import pygame
import sys
from os import path, listdir
from settings import *
from sprites import *
from tilemap import Map
from teams import Blue, Orange
from interact import PlayerHandler

class Game:
    def __init__(self):
        self.start_setup()
        print("Starting...")

        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.load_data()

    def load_data(self):
        assets_dir = path.join(path.dirname(__file__), 'assets')
        map_file = path.join(assets_dir, 'map.txt')
        self.map = Map(map_file)

    def new(self):
        # initialize all variables and do all the setup for a new game
        self.all_sprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()

        #Teams
        self.team_orange = Orange()
        self.team_blue = Blue()
        self.unknowns = pygame.sprite.Group()

        #Generate map
        self.map.new(self)

        #Time event & SETUP: player file
        self.handler = PlayerHandler(self)

    def run(self):
        # Game loop - set self.playing = False to end the game
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

    def quit(self):
        self.handler.quit(self)
        pygame.quit()
        sys.exit()
    
    def update(self):
        # Update portion of the game loop
        self.all_sprites.update()
        self.team_orange.update()
        self.team_blue.update()

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

    def win(self, score):
        percentage = round(score / self.max_tiles, 2)
        if percentage > WIN_PERCENTAGE:
            return True
        return False

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.quit()

            if event.type == self.handler.action_timer:
                self.team_orange.update_direction()
                self.team_blue.update_direction()
                self.handler.player_turn(self)

        if self.win(self.team_orange.score) or self.win(self.team_blue.score):
            self.quit()

    def start_setup(self):
        print("<" + "="*5 + f"SETUP" + "="*5 + ">")
        script_dir = path.join(path.dirname(__file__), DIRECTORY)
        while True:
            print("ID: File")
            listfile = listdir(script_dir)
            for file_id, file in enumerate(listfile):
                print(f"{file_id+1}: {file}")

            player1 = input("Enter Player 1 id file: ")

            condition = lambda cond: all([cond.isdigit(), 
                                        0 < int(cond) <= len(listfile), 
                                        path.exists(script_dir + "/" + listfile[int(cond)-1]), 
                                        listfile[int(cond)-1].endswith(".py")])

            if condition(player1):
                self.player1 = script_dir + "/" + listfile[int(player1)-1]
            else:
                continue 

            player2 = input("Enter Player 2 id file: ")

            if condition(player2):
                self.player2 = script_dir + "/" + listfile[int(player2)-1]
            else:
                continue 

            print("<" + "="*5 + f"{TITLE}" + "="*5 + ">")
            break

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

