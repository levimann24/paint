import pygame


class Button:
    """class to create buttons for various settings"""

    def __init__(self, p_game, x, y):
        self.settings = p_game.settings
        self.screen = p_game.screen
        self.screen_rect = self.screen.get_rect()

        self.rect = pygame.Rect(
            x, y, self.settings.b_width, self.settings.b_height)
        self.color = (0, 0, 0)
        self.border_rect = pygame.Rect(
            x, y, self.settings.b_width, self.settings.b_height)
        self.border_col = (0, 0, 0)

    def set_color(self, color):
        selection = {
            'red': (255, 0, 0),
            'blue': (0, 0, 255),
            'green': (0, 255, 0),
            'black': (0, 0, 0),
            'white': (255, 255, 255),
        }
        self.color = selection[color]

    def draw_button(self):
        """Draw button to screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
        pygame.draw.rect(self.screen, self.border_col, self.border_rect, 3)
