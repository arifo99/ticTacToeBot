import pygame
pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
my_font = pygame.font.SysFont('Comic Sans MS', 30)
class Button:

    def __init__(self, text, x, y, onClick, width=100, height=50):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.color = (120, 120, 120)
        self.onClick = onClick

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        screen.blit(my_font.render(self.text, False, (255, 255, 255)), (self.rect.x, self.rect.y))

    def update(self, clicked):
        x, y = pygame.mouse.get_pos()
        if(self.rect.collidepoint((x, y))):
            self.color = (60, 60, 60)
            if(clicked):
                self.onClick()
        else:
            self.color = (120, 120, 120)
    
