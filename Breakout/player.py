import pygame

class Player:
    def __init__(self, game, x, y):
        self.game = game
        self.x = x
        self.y = y
        self.width = 150
        self.height = 20
        self.color = (255, 255, 255)  # White color
        self.screen = pygame.display.get_surface()

    def draw(self):
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))

    def update(self):
        self.draw()
        self.movement()

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if self.x > 0:
                self.x -= 5
        if keys[pygame.K_RIGHT]:
            if self.x < self.screen.get_width() - self.width:
                self.x += 5
       
     