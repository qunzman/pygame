import pygame

class clickobj:
    def __init__(self, game, x, y, width):
        self.game = game
        self.width = width
        self.original_width = width
        self.x = x
        self.y = y
        self.screen = game.screen
        self.color = (255, 196, 0)
        self.click_time = None
        self.is_animating = False
    
    def update(self):
        self.draw()
        if self.click_time is None or not self.is_animating:
            return

        if pygame.time.get_ticks() - self.click_time >= 150:
            self.width = self.original_width  
            self.is_animating = False
            self.click_time = None

    def is_clicked(self, pos):
        center_x, center_y = self.x, self.y
        radius = self.width // 2
        return (pos[0] - center_x) ** 2 + (pos[1] - center_y) ** 2 <= radius ** 2

    def animation(self):

        if not self.is_animating:
            self.is_animating = True
            self.click_time = pygame.time.get_ticks()
            self.width -= 10
       

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.width // 2)