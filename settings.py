import pygame
import modules.path_to_file as m_p_file


class Settings:
    def __init__(self, x = 0, y = 0, name = None):
        self.X = x
        self.Y = y
        self.SCREEN_WIDTH = 600
        self.SCREEN_HEIGHT = 600
        self.IMG_WIDTH = 150
        self.IMG_HEIGHT = 150
        self.SCREEN_COLOR = (120, 150, 235)
        self.NAME_FILE = name
        self.IMG = None

    
    def load_file(self):
        load_file = pygame.image.load(m_p_file.path_file(self.NAME_FILE))
        self.IMG = pygame.transform.scale(load_file(self.IMG_WIDTH, self.IMG_HEIGHT))

    # def blit_sprite(self, screen_game):
        # screen_game.blit(self.IMG, (self.X, self.Y))


set = Settings()
