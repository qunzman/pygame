import pygame

class clickup:
    def __init__(self, game, x, y, width, height, image):
        self.game = game
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = image
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def update(self):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.draw()

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)
    
    def draw(self):
        self.game.screen.blit(self.image, self.rect)
      