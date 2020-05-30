import pygame
import sys
import settings


class PaintGame:
    def __init__(self):
        self.game_active = True
        self.settings = settings.Settings()
        self.screen_width = self.settings.WIDTH
        self.screen_height = self.settings.HEIGHT
        self.bg_color = self.settings.bg_color

        # initialize the screen
        self.screen = pygame.display.set_mode(
            (self.screen_width, self.screen_height))

    def on_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def on_loop(self):
        pass

    def on_render(self):
        # create screen
        self.screen.fill(self.bg_color)

        # update the screen with above changes
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        while True:
            self.on_event()
            self.on_loop()
            self.on_render()
        self.on_cleanup()


if __name__ == '__main__':
    p_game = PaintGame()
    p_game.on_execute()
