import pygame
import sys
import settings
import buttons


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
        pygame.display.set_caption("Paint!")

        # initialize different buttons
        self.initialize_buttons()

    def on_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:  # see if user quit game
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()  # get position of mouse to evaluate click
                self.check_click(mouse_pos)

    def on_loop(self):
        pass

    def on_render(self):
        # create screen
        self.screen.fill(self.bg_color)
        # draw buttons
        self.draw_buttons()
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

# ----------------------------------------------
#  methods for excecution
# ----------------------------------------------
    def check_click(self, mouse_pos):
        button_clicked = self.b_red.rect.collidepoint(mouse_pos)
        if button_clicked:
            print("Red button clicked!!!")


# ----------------------------------------------

    def initialize_buttons(self):
        self.b_red = buttons.Button(
            self, self.screen_width/2, self.screen_height/2)
        self.b_red.set_color('red')

    def draw_buttons(self):
        self.b_red.draw_button()

# ----------------------------------------------


if __name__ == '__main__':
    p_game = PaintGame()
    p_game.on_execute()
