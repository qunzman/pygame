import pygame

class clickobj:
    def __init__(self, game, x, y, width, height):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.screen = game.screen
        self.color = (255, 196, 0) 
    
    def update(self):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.draw()

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)
    
    def draw(self):
        pygame.draw.circle(self.screen, self.color, self.rect.center, self.rect.width // 2)