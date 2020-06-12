import pygame
import sys
import settings
import buttons
import pen


class PaintGame:
    def __init__(self):
        """Initialize the settings"""
        self.game_active = True
        self.settings = settings.Settings()
        self.screen_width = self.settings.WIDTH
        self.screen_height = self.settings.HEIGHT
        self.bg_color = self.settings.bg_color
        self.click = False
        self.current_color = (0, 0, 0)
        self.current_size = 5

        # initialize the screen
        self.screen = pygame.display.set_mode(
            (self.screen_width, self.screen_height))
        pygame.display.set_caption("Paint!")

        # initialize different buttons
        self.color_buttons = []
        self.initialize_color_buttons()
        self.size_buttons = []
        self.initialize_size_buttons()
        self.eraser = buttons.Button(
            self, self.settings.WIDTH/2, self.settings.HEIGHT/2)
        self.eraser_on = False

        # initialize the pen
        self.drawings = pygame.sprite.Group()

    def on_event(self):
        """check for events"""
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
                # elif event.type == pygame.MOUSEMOTION:
                #     mouse_pos = event.pos
                    # self.draw_on_screen(mouse_pos)
                else:
                    self.click = True
                    # self.pen.pen_draw(mouse_pos[0], mouse_pos[1])
                    while self.click:
                        if self.eraser_on == False:
                            self.draw_on_screen(mouse_pos)
                        else:
                            self.eraser_collide(mouse_pos)
                        self.update_drawings()
                        self.key_up()
                        pygame.display.flip()
                        mouse_pos = pygame.mouse.get_pos()

    def key_up(self):
        """check for key up events"""
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                self.click = False

    def on_loop(self):
        pass

    def on_render(self):
        """send everything to the screen"""
        # create screen
        self.screen.fill(self.bg_color)
        # draw buttons
        self.draw_buttons()
        # draw an eraser
        self.eraser.draw_button()
        # update pen drawing
        self.update_drawings()
        # update the screen with above changes
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        """game loop"""
        while True:
            self.on_event()
            self.on_loop()
            self.on_render()
        self.on_cleanup()

# ----------------------------------------------
#  methods for excecution
# ----------------------------------------------
    def check_click(self, mouse_pos):
        """check if mouse clicks a button"""
        eraser_clicked = self.eraser.rect.collidepoint(mouse_pos)
        if eraser_clicked:
            self.eraser_on = True
        else:
            for button in self.color_buttons:
                button_clicked = button.rect.collidepoint(mouse_pos)
                if button_clicked:
                    self.eraser_on = False
                    self.current_color = button.get_color()
                    # might be inefficient, but trade off to change
                    # the color of the size button
                    for button in self.size_buttons:
                        button.set_color(self.current_color)
                    return True
            for button in self.size_buttons:
                button_clicked = button.border_rect.collidepoint(mouse_pos)
                if button_clicked:
                    self.current_size = button.get_size()
                    return True

        return False

# ----------------------------------------------

    def initialize_color_buttons(self):
        """initialize the color choice buttons"""
        colors = ['black', 'red', 'blue', 'green', 'white']
        for i in range(0, len(colors)):
            self.color_buttons.append(buttons.Button(
                self, self.screen_width/2 + (self.settings.b_width+5)*i, 3*self.screen_height/4))
            self.color_buttons[i].set_color(colors[i])

    def initialize_size_buttons(self):
        """Initializes the size choice buttons"""
        sizes = ['small', 'medium', 'large']
        for i in range(len(sizes)):
            self.size_buttons.append(buttons.Button(self, self.screen_width/2 + (
                self.settings.b_width+5)*i, 3*self.screen_height/4+self.settings.b_height+5))
            self.size_buttons[i].set_size(sizes[i], self)

    def draw_buttons(self):
        """draw the buttons on screen"""
        for button in self.color_buttons:
            button.draw_button()
        for button in self.size_buttons:
            button.draw_button()
        # self.b_red.draw_button()

# ----------------------------------------------

    # def get_color(self):
    def draw_on_screen(self, mouse_pos):
        """add new pen marks to drawing sprite array"""
        draw = pen.Pen(self)
        draw.set_pen_color(self.current_color)
        draw.set_pen_size(self.current_size)
        draw.pen_draw(mouse_pos[0], mouse_pos[1])
        # TODO: SET PEN SIZE draw.set_pen_size()
        self.drawings.add(draw)

    def update_drawings(self):
        """draw each of the pen marks in the sprite array"""
        for draw in self.drawings.sprites():
            draw.update_pen()

# -------------------------------------------------
    def eraser_collide(self, mouse_pos):
        """Check the collision of mouse when eraser is activated"""
        for draw in self.drawings.sprites():
            erased = draw.rect.collidepoint(mouse_pos)
            if erased:
                draw.kill()
                # self.drawings.remove(draw)


if __name__ == '__main__':
    p_game = PaintGame()
    p_game.on_execute()
