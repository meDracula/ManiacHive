import pygame
import sys
from os import path, listdir
import settings
from tilemap import Map
from teams import Blue, Orange
from interact import PlayerHandler


class Game:
    def __init__(self):
        self.start_setup()
        print("Starting...")

        pygame.init()
        self.screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
        pygame.display.set_caption(settings.TITLE)
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

        # Teams
        self.team_orange = Orange()
        self.team_blue = Blue()
        self.unknowns = pygame.sprite.Group()

        # Generate map
        self.map.new(self)

        # Time event & SETUP: player file
        self.handler = PlayerHandler(self)

    def run(self):
        # Game loop - set self.playing = False to end the game
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(settings.FPS) / 1000
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
        for x in range(0, settings.WIDTH, settings.TILESIZE):
            pygame.draw.line(self.screen, settings.LIGHTGREY, (x, 0), (x, settings.HEIGHT))
        for y in range(0, settings.HEIGHT, settings.TILESIZE):
            pygame.draw.line(self.screen, settings.LIGHTGREY, (0, y), (settings.WIDTH, y))

    def draw(self):
        self.screen.fill(settings.BGCOLOR)
        self.draw_grid()
        self.all_sprites.draw(self.screen)
        pygame.display.flip()

    def win(self, score):
        percentage = round(score / self.max_tiles, 2)
        if percentage >= settings.WIN_PERCENTAGE:
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

    def setup_file_conditions(self, player, listfile: list, script_dir: str):
        x_1 = player.isdigit()
        x_2 = 0 < int(player) <= len(listfile)
        x_3 = path.exists(script_dir + "/" + listfile[int(player)-1])
        x_4 = listfile[int(player)-1].endswith(".py")
        return all([x_1, x_2, x_3, x_4])

    def start_setup(self):
        print("<" + "="*5 + "SETUP" + "="*5 + ">")
        script_dir = path.join(path.dirname(__file__), settings.DIRECTORY)
        while True:
            print("ID: File")
            listfile = listdir(script_dir)
            for file_id, file in enumerate(listfile):
                print(f"{file_id+1}: {file}")

            player1 = input("Enter Player 1 id file: ")

            if self.setup_file_conditions(player1, listfile, script_dir):
                self.player1 = script_dir + "/" + listfile[int(player1)-1]
            else:
                continue

            player2 = input("Enter Player 2 id file: ")

            if self.setup_file_conditions(player2, listfile, script_dir):
                self.player2 = script_dir + "/" + listfile[int(player2)-1]
            else:
                continue

            print("<" + "="*5 + f"{settings.TITLE}" + "="*5 + ">")
            break

    def show_start_screen(self):
        # For the future development
        pass

    def show_go_screen(self):
        # For the future development
        pass


def main():
    # Create the game Instance
    g = Game()
    g.show_start_screen()
    while True:
        g.new()
        g.run()
        g.show_go_screen()


if __name__ == '__main__':
    main()
