import pygame

pygame.init()

screen = pygame.display.set_mode((1000, 800))
screen.fill((0,0,0))

class Button:

    def __init__(self, text, button_x, button_y, text_x, text_y, width, height):
        self.text = text
        self.button_x = button_x
        self.button_y = button_y
        self.text_x = text_x
        self.text_y = text_y
        self.width = width
        self.height = height
        self.mx, self.my = pygame.mouse.get_pos()
        self.text_position = (self.text_x, self.text_y)
        self.font = pygame.font.SysFont(None, 25)
        self.button_color = (255, 255, 255)
        self.text_color = (0,0,0)
        self.button = pygame.Rect(self.button_x, self.button_y, self.width, self.height)
        self.text_display = self.font.render(self.text, True, self.text_color)

    def blit_button_text_on_window(self):
        screen.blit(self.text_display, self.text_position)

    def draw_button_on_window(self):
        pygame.draw.rect(screen, self.button_color, self.button)

def main_game_loop():
    run = True

    while run:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False

            button_test = Button("Hey", 200, 200, 210, 210, 100, 100)
            button_test.draw_button_on_window()
            button_test.blit_button_text_on_window()
            pygame.display.update()

            if button_test.button.collidepoint((button_test.mx, button_test.my)) and event.type == pygame.MOUSEBUTTONDOWN:
                font = pygame.font.SysFont(None, 25)
                printed_text = font.render("Hey", True, (255,255,255))
                screen.blit(printed_text, (425,160))

    pygame.quit()

if __name__ == "__main__":
    main_game_loop()
