import pygame
from settings import STARTING_TEAM, DIRECTORY, ORANGE, BLUE
from semantic import SemanticHandler

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
        stdin_queen = "{} {} {}".format(queen.unit, int(queen.x), int(queen.y))
        team.run_init(stdin_queen)

    def player_turn(self, game):
        if self.team_turn == self.teams[0]:
            print("<===Orange===>")
            self.action(game.team_orange, game.queen_blue, game.max_tiles)
            self.team_turn = self.teams[1]
        else:
            print("<===Blue===>")
            self.action(game.team_blue, game.queen_orange, game.max_tiles)
            self.team_turn = self.teams[0]

    def stdin_sample(self, sprites_info):
        possible_dir = [" ".join(value[1]) for value in sprites_info.values()]
        sample = " ".join([f"{key} {value}" for key, value in zip(sprites_info.keys(), possible_dir)])
        print(sample)
        return sample

    def opponent_queen(self, queen):
        return f"{1} {queen.x} {queen.y}"

    def action(self, team, enemy_queen, max_tiles):
        command = self.stdin_sample(team.sprites_info)
        stdout = team.run(command, self.opponent_queen(enemy_queen), 10)
        commands = SemanticHandler.syntax(stdout, team.sprites_info) #return {id: dir}
        for key in commands:
            self.move(team.sprites_info[key][0], commands[key]) 
        print(f"Score: {round(team.score/max_tiles, 2)*100}% : {team.score}/{max_tiles}")

    def move(self, sprite, direction):
        sprite.move(direction)
        print("Move:", direction)

    def quit(self, game):
        game.team_orange.kill_child()
        game.team_blue.kill_child()

