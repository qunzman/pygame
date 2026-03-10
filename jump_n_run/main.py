import pygame

class Game:
    def __init__(self):
        pygame.init()
        self.window_widht = 800
        self.window_height = 400
        self.window = pygame.display.set_mode((self.window_widht, self.window_height))
        self.run()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            self.window.fill((137, 207, 240))







            pygame.display.update()

        pygame.quit()

game = Game()