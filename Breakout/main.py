import pygame
import player

class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Break out")

        self.player = player.Player(self, 375, 550)

        self.run()


    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.fill((25, 25, 75))  # Fill the screen with light blue
            self.player.update()

            pygame.display.update()
        
        pygame.quit()
    
game = Game()