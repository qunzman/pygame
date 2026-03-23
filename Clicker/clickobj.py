import pygame

class clickobj:
    def __init__(self, game, x, y, width):
        self.width = width
        self.x = x
        self.y = y
        self.screen = game.screen
        self.color = (255, 196, 0) 
    
    def update(self):
        self.draw()

    def is_clicked(self, pos):
        center_x, center_y = self.x, self.y
        radius = self.width // 2
        return (pos[0] - center_x) ** 2 + (pos[1] - center_y) ** 2 <= radius ** 2
    
    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.width // 2)