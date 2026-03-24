import pygame

class upgrades:
    def __init__(self, game, y, width, height, image):
        self.game = game
        self.x = 700
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
      