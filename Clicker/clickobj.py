import pygame

class clickobj:
    def __init__(self, game, x, y, width, img):
        self.game = game
        self.width = width
        self.height = width
        self.original_width = width
        self.x = x
        self.y = y
        self.img = img
        self.image = pygame.transform.scale(self.img, (self.width, self.height))
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.screen = game.screen
        self.color = (255, 196, 0)
        self.click_time = None
        self.is_animating = False
    
    def update(self):
        if self.click_time is not None and self.is_animating:
            if pygame.time.get_ticks() - self.click_time >= 150:
                self.width = self.original_width  
                self.height = self.original_width
                self.image = pygame.transform.scale(self.img, (self.width, self.height))
                self.rect = self.image.get_rect(center=(self.x, self.y))
                self.is_animating = False
                self.click_time = None
        self.draw()

    def is_clicked(self, pos):
        center_x, center_y = self.x, self.y
        radius = self.width // 2
        return (pos[0] - center_x) ** 2 + (pos[1] - center_y) ** 2 <= radius ** 2

    def animation(self):
        if not self.is_animating:
            self.is_animating = True
            self.click_time = pygame.time.get_ticks()
            self.width -= 10
            self.height -= 10
            self.image = pygame.transform.scale(self.img, (self.width, self.height))
            self.rect = self.image.get_rect(center=(self.x, self.y))
       

    def draw(self):
        self.game.screen.blit(self.image, self.rect)
      