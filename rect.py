import pygame
from modules.data_base import list_square
import modules.data_base as m_data

pygame.init()

class Square:
    def __init__(self, x, y, width = 150, height = 150):
        self.X = x
        self.Y = y
        self.WIDTH = width
        self.HEIGHT = height
        self.COLOR = (75, 70, 240)    

    def create_table(self):
        x = self.X
        y = self.Y
        for row in range(3):
            for column in range(3):
                new_square = pygame.Rect(x, y, self.WIDTH, self.HEIGHT)
                list_square.append(new_square)
                x += 175
            x = self.X
            y += 175

        
    def draw_square(self, screem_game):
        for el in list_square:
            pygame.draw.rect(surface = screem_game, color = self.COLOR, rect = el, width = 0)

square = Square(x = 50, y = 50)
square.create_table()



    
    
        