import pygame
import clickobj
import clickup

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1000, 600))
        self.clock = pygame.time.Clock()
        self.running = True
        self.clickobj = clickobj.clickobj(self, 100, 150, 300, 300)
        self.coins = 0
        self.font_coins = pygame.font.SysFont("Misc fixed", 64)
        self.font_costs = pygame.font.SysFont("Misc fixed", 32)
        self.clickup = clickup.clickup(self, 700, 50, 275, 50, pygame.image.load("img/Clickup.png"))
        self.coins_per_click = 1
        self.price = 10
        self.run()

    def format_zahl(n):
        if n >= 1_000_000_000:
            wert = n / 1_000_000_000
            suffix = "B"
        elif n >= 1_000_000:
            wert = n / 1_000_000
            suffix = "M"
        elif n >= 1_000:
            wert = n / 1_000
            suffix = "k"
        else:
            return str(n)
    
    # Zeigt .1 nur wenn nötig
        if wert == int(wert):
            return f"{int(wert)}{suffix}"
        else:
            return f"{wert:.1f}{suffix}"
  
    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.clickobj.is_clicked(event.pos):
                        self.coins += self.coins_per_click
                    if self.clickup.is_clicked(event.pos) and self.coins >= self.price:
                        self.coins_per_click += self.coins_per_click * 1.15
                        self.coins -= self.price
                        self.price = int(self.price * 1.5)

            self.screen.fill((0, 0, 0))
            self.clickobj.update()
            self.clickup.update()
            self.coin_text = self.font_coins.render(f"coins: {int(self.coins)}", True, (255, 255, 255))
            self.coin_rect = self.coin_text.get_rect(topleft=(175, 50))
            self.screen.blit(self.coin_text, self.coin_rect)
            self.price1 = self.format_zahl(self.price)
            self.price_text = self.font_costs.render(f"{self.price1}", True, (255, 255, 255))
            self.price_rect = self.price_text.get_rect(topleft=(930, 60))
            self.screen.blit(self.price_text, self.price_rect)




            pygame.display.update()
    

    pygame.quit()

game = Game()
        

