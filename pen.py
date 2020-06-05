import pygame
import pygame.sprite


class Pen(pygame.sprite.Sprite):
    """class to create a pen"""

    def __init__(self, p_game):
        # initialize parent sprite class
        super().__init__()

        self.settings = p_game.settings
        self.screen = p_game.screen
        self.screen_rect = self.screen.get_rect()
        # checking if mouse is held down
        self.click = False
        self.height = 5
        self.width = 5
        self.color = (0, 0, 0)
        self.draw = []

    def set_pen_color(self, color):
        """set the pen color"""
        self.color = color

    def set_pen_size(self, size):
        """set the pen size"""
        self.width = size
        self.height = size

    def pen_draw(self, x, y):
        """initialize the mark on the screen"""
        self.rect = pygame.Rect((x-self.width/2), (y -
                                                   self.height/2), self.width, self.height)

    def update_pen(self):
        """draw the mark to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
