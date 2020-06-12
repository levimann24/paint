import pygame


class Eraser:
    """Class to erase what is on the screen"""

    def __init__(self, p_game):
        self.screen = p_game.screen
        self.screen_rect = self.screen.get_rect()
        self.width = 5
        self.height = 5
        self.color = (255, 255, 255)
