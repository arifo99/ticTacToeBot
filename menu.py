import pygame

class Menu:

    def __init__(self, title, buttons):
        self.buttons = buttons
        pygame.font.init()
        my_font = pygame.font.SysFont('Comic Sans MS', 30)
        self.title = my_font.render(title, False, (0, 0, 0))

    def draw(self, screen):
        screen.blit(self.title, (0, 0))
        for button in self.buttons:
            button.draw(screen)

    def update(self, clicked):
        for button in self.buttons:
            button.update(clicked)
    
