import pygame
import settings


class Pen:
    """class to create a pen"""

    def __init__(self, p_game):
        self.settings = p_game.settings
        self.screen = p_game.screen
        self.screen_rect = self.screen.get_rect()
        # checking if mous is held down
        self.click = False

    def set_pen_color(self, color):
        pass

    def set_pen_size(self, size):
        pass

    def pen_draw(self):
        pass
