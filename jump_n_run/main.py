import pygame
import Player
import plates


class Game:
    def __init__(self):
        pygame.init()
        self.window_widht = 800
        self.window_height = 400
        self.window = pygame.display.set_mode((self.window_widht, self.window_height))
        self.playerimage = pygame.image.load("Robot/Robot Standart.png")
        self.playerjumpimage = pygame.image.load("Robot/Jump.png")
        self.player = Player.Player(self, 350, 100, 100, 170, self.playerimage, self.playerjumpimage)
        self.background = pygame.image.load("Background/Hintergrund.png")
        self.background = pygame.transform.scale(self.background, (self.window_widht, self.window_height))
        self.klone = []
        self.plateimage = pygame.image.load("Plattform/Plattform.png")  # dein Platten-Bild
        self.game_map = plates.Plate(self, 128, 128, self.plateimage)
        self.run()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            self.window.blit(self.background, (0, 0))
            self.player.update()
 
            neuer_klon = self.game_map.klon(self.klone, 100)
            if neuer_klon:
                self.klone.append(neuer_klon)

            for klon in self.klone:
                klon.update()

            pygame.display.update()

        pygame.quit()

game = Game()