import pygame

class clickup:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def update(self):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.draw()

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)
    
    def draw(self):
        pygame.draw.circle(self.screen, self.color, self.rect.center, self.rect.width // 2)