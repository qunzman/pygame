import pygame
import random


class Plate:
    def __init__(self, game, width, height, image):
        self.x = 800
        self.y = 200
        self.game = game
        self.image = image
        self.image = pygame.transform.scale(self.image, (width, height))
        self.width = width
        self.height = height
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def klon(self, klone, mindestabstand):
        rny = random.randint(0, 100 - self.height)

        # Prüfe ob der zuletzt gespawnte Klon weit genug weg ist
        if klone:  # nur wenn schon Klone existieren
            letzter = klone[-1]  # der zuletzt hinzugefügte Klon
            if letzter.rect.x > (800 - mindestabstand):
                return None  # letzter Klon noch zu nah am rechten Rand
        
        neuer = Plate(self.game, self.width, self.height, self.image)
        neuer.rect.y = rny
        return neuer

    def update(self):
        self.draw()
        self.movement()

    def draw(self):
        self.game.window.blit(self.image, (self.rect.x, self.rect.y))
    
    def movement(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.rect.x += 5
        if keys[pygame.K_RIGHT]:
            self.rect.x -= 5