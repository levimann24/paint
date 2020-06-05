import pygame


class Button:
    """class to create buttons for various settings"""

    def __init__(self, p_game, x, y):
        self.settings = p_game.settings
        self.screen = p_game.screen
        self.screen_rect = self.screen.get_rect()
        self.width = self.settings.b_width
        self.height = self.settings.b_height
        self.x = x
        self.y = y

        self.rect = pygame.Rect(
            self.x, self.y, self.width, self.height)
        self.color = (0, 0, 0)
        self.border_rect = pygame.Rect(
            self.x, self.y, self.settings.b_width, self.settings.b_height)
        self.border_col = (0, 0, 0)

    def set_color(self, color):
        """set the color of the button"""
        selection = {
            'red': (255, 0, 0),
            'blue': (0, 0, 255),
            'green': (0, 255, 0),
            'black': (0, 0, 0),
            'white': (255, 255, 255),
        }
        if color in selection:
            self.color = selection[color]
        else:
            self.color = color

    def draw_button(self):
        """Draw button to screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
        pygame.draw.rect(self.screen, self.border_col, self.border_rect, 3)

    def set_size(self, size, p_game):
        """set the size of the pixel for the pen options"""
        selection = {
            'small': 5,
            'medium': 10,
            'large': 20
        }
        self.width = selection[size]
        self.height = selection[size]
        if self.width < self.settings.b_width:
            correction_x = self.x + self.settings.b_width/2 - self.width/2
            correction_y = self.y + self.settings.b_height/2 - self.height/2
        else:
            correction = self.x + self.width - self.settings.b_widt
        self.rect = pygame.Rect(
            correction_x, correction_y, self.width, self.height)
        self.color = p_game.current_color

    def get_color(self):
        """return the color of the button pressed"""
        return self.color

    def get_size(self):
        """ return current size """
        return self.width
