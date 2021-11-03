import pygame
from settings import STARTING_TEAM, DIRECTORY

class PlayerHandler:
    def __init__(self, game):
        self.action_timer = pygame.USEREVENT + 1
        pygame.time.set_timer(self.action_timer, 1000) #event, x milliseconds
        self.team_turn = STARTING_TEAM #Starting team  set from settings
        self.teams = ['orange', 'blue'] #Assumes that lenght is 2 and only to teams playing
        self.setup_spawn(game.player1, game.team_orange, game.queen_orange)
        self.setup_spawn(game.player2, game.team_blue, game.queen_blue)

    def setup_spawn(self, file, team, queen):
        print(file)
        team.script = file
        team.spawn(team.script)
        stdin_queen = "{} {}".format(int(queen.x), int(queen.y))
        print(stdin_queen)
        team.run_init(stdin_queen)

    def player_turn(self, game):
        if self.team_turn == self.teams[0]:
            print("<===Orange===>")
            direction = self.handler_dump(game, game.queen_orange)
            self.move(game.max_tiles, game.queen_orange, direction)
            self.team_turn = self.teams[1]
        else:
            print("<===Blue===>")
            direction = self.handler_dump(game, game.queen_blue)
            self.move(game.max_tiles, game.queen_blue, direction)
            self.team_turn = self.teams[0]

    def handler_dump(self, game, queen):
        stdin_queen = " ".join(queen.possible_dir)
        print(stdin_queen)
        return queen.team.run(stdin_queen)

    def move(self, max_tiles, queen, direction):
        print("Move:", direction)
        queen.move(direction)
        print(f"Score: {round(queen.team.score/max_tiles, 2)*100}% : {queen.team.score}/{max_tiles}")

    def quit(self, game):
        game.team_orange.kill_child()
        game.team_blue.kill_child()

