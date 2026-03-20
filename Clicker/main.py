import pygame
import clickobj

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1000, 600))
        self.clock = pygame.time.Clock()
        self.running = True
        self.clickobj = clickobj.clickobj(self, 100, 150, 300, 300)
        self.coins = 0
        self.font = pygame.font.SysFont("Misc fixed", 64)
        self.run()

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.clickobj.is_clicked(event.pos):
                        self.coins += 1
                        
                        

            self.screen.fill((0, 0, 0))
            self.clickobj.update()
            self.coin_text = self.font.render(f"coins: {self.coins}", True, (255, 255, 255))
            self.coin_rect = self.coin_text.get_rect(topleft=(175, 50))
            self.screen.blit(self.coin_text, self.coin_rect)




            pygame.display.update()
    

    pygame.quit()

game = Game()
        

