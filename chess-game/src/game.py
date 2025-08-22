import pygame
from const import *

class Game:

    def __init__(self):
        pass


    def show_bg(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                if (row + col) % 2 == 0:
                    colour = (115, 31, 122)
                else:
                    colour = (200, 101, 140)

                rect = (col * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE)

                pygame.draw.rect(surface, colour, rect)



