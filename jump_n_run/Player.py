import pygame

class Player:
    def __init__(self, game, x, y, width, height, stanpicture, jumpicture):
        self.game = game
        self.width = width
        self.height = height
        self.stand_picture = pygame.transform.scale(stanpicture, (self.width, self.height))
        self.jump_picture = pygame.transform.scale(jumpicture, (self.width, self.height))
        self.xpicture = self.stand_picture

        self.vel_y = 0          # 0 statt -8, kein automatischer Sprung!
        self.gravity = 1.0      
        self.on_ground = False  
        self.ground_y = self.game.window_height - self.height
        self.rect = pygame.Rect(x, y, self.width, self.height)
        
    def update(self):
        self.movement()
        self.draw()

    def draw(self):
        self.game.window.blit(self.xpicture, (self.rect.x, self.rect.y))

    def movement(self):
        keys = pygame.key.get_pressed()

        # Springen (nur wenn auf dem Boden)
        if keys[pygame.K_UP] and self.on_ground:
            self.vel_y = -15
            self.xpicture = self.jump_picture

        # Gravity anwenden
        self.vel_y += self.gravity
        self.rect.y += self.vel_y

        # Boden-Kollision
        if self.rect.y >= self.ground_y:
            self.rect.y = self.ground_y
            self.vel_y = 0
            self.on_ground = True
            self.xpicture = self.stand_picture
        else:
            self.on_ground = False
