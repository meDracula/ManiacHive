import pygame, sys
from os.path import exists
from settings import ORANGE, PLANE_ORANGE, BLUE, PLANE_BLUE 
import pexpect

class TeamHandler:
    def __init__(self, color, plane_color):
        self.color = color
        self.plane_color = plane_color
        self.file_path = None
        self.file = None

    @property
    def script(self):
        full_file = "{}/{}".format(self.file_path, self.file)
        if exists(full_file): 
            return full_file
        else: 
            raise FileNotFoundError("Player Orange File NO LONGER EXISTS")

    @script.setter
    def script(self, newfile):
        if exists(newfile):
            self.file_path, self.file = newfile.rsplit("/", 1)
        else:
            raise FileNotFoundError("File apperas to no longer exists")

    def spawn(self, file):
        self.child = pexpect.spawn(f"{sys.executable} {file}")

    def run_init(self, command):
        self.child.expect('')
        self.child.sendline(command)
        self.child.readline()

    def run(self, command):
        self.child.expect('')
        self.child.sendline(command)

        self.child.expect('stdout:')
        player_out = self.child.readline().decode('utf-8')
        return player_out.strip() 

    def kill_child(self):
        self.child.close(force=True)

class Orange(TeamHandler):
    def __init__(self):
        super().__init__(ORANGE, PLANE_ORANGE)
        self.objects = pygame.sprite.Group()
        self.tiles = pygame.sprite.Group()

    @property
    def score(self):
        return len(self.tiles.sprites()) 

class Blue(TeamHandler):
    def __init__(self):
        super().__init__(BLUE, PLANE_BLUE)
        self.objects = pygame.sprite.Group()
        self.tiles = pygame.sprite.Group()

    @property
    def score(self):
        return len(self.tiles.sprites())

