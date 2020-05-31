import pygame
import sys
import settings
import buttons
import pen


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
        self.color_buttons = []
        self.initialize_color_buttons()

        # initialize the pen
        self.drawings = pygame.sprite.Group()

        self.click = False
        self.current_color = (0, 0, 0)

    def on_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:  # see if user quit game
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()  # get position of mouse to evaluate click
                if self.check_click(mouse_pos):
                    pass
                elif event.type == pygame.MOUSEMOTION:
                    mouse_pos = event.pos
                    self.draw_on_screen(mouse_pos)
                else:
                    self.click = True
                    # self.pen.pen_draw(mouse_pos[0], mouse_pos[1])
                    while self.click:
                        self.draw_on_screen(mouse_pos)
                        self.update_drawings()
                        self.key_up()
                        pygame.display.flip()
                        mouse_pos = pygame.mouse.get_pos()

    def key_up(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                self.click = False

    def on_loop(self):
        pass

    def on_render(self):
        # create screen
        self.screen.fill(self.bg_color)
        # draw buttons
        self.draw_buttons()
        # update pen drawing
        self.update_drawings()
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
        for button in self.color_buttons:
            button_clicked = button.rect.collidepoint(mouse_pos)
            if button_clicked:
                self.current_color = button.get_color()
                return True
        return False

# ----------------------------------------------

    def initialize_color_buttons(self):
        colors = ['black', 'red', 'blue', 'green', 'white']
        for i in range(0, len(colors)):
            self.color_buttons.append(buttons.Button(
                self, self.screen_width/2 + (self.settings.b_width+5)*i, 3*self.screen_height/4))
            self.color_buttons[i].set_color(colors[i])
        # self.b_red = buttons.Button(
        #     self, self.screen_width/2, 3*self.screen_height/4)
        # self.b_red.set_color('red')

    def draw_buttons(self):
        for button in self.color_buttons:
            button.draw_button()
        # self.b_red.draw_button()

# ----------------------------------------------

    # def get_color(self):
    def draw_on_screen(self, mouse_pos):
        draw = pen.Pen(self)
        draw.set_pen_color(self.current_color)
        draw.pen_draw(mouse_pos[0], mouse_pos[1])
        # TODO: SET PEN SIZE draw.set_pen_size()
        self.drawings.add(draw)

    def update_drawings(self):
        for draw in self.drawings.sprites():
            draw.update_pen()

    def continuous_draw(self):
        pass


if __name__ == '__main__':
    p_game = PaintGame()
    p_game.on_execute()
