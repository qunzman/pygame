import pygame
import clickobj
import clickup
import lemonade_stand

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1000, 600))
        self.clock = pygame.time.Clock()
        self.running = True
        self.clickobj = clickobj.clickobj(self, 480, 300, 300)
        self.coins = 0
        self.font_coins = pygame.font.SysFont("Misc fixed", 64)
        self.font_costs1 = pygame.font.SysFont("Misc fixed", 28)
        self.clickup = clickup.clickup(self, 700, 50, 300, 50, pygame.image.load("img/Clickup.png"))
        self.coins_per_click = 1
        self.price = 10
        self.click_multiplier = 1.15
        self.lemonade_stand = lemonade_stand.LemonadeStand(self, 700, 100, 300, 50, pygame.image.load("img/Lemonade_stand.png"))
        self.run()

    def format_zahl(self, n):
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
                        self.coins_per_click *= self.click_multiplier
                        self.coins -= self.price
                        self.price = int(self.price * 2.5)

            if self.coins_per_click >= 2:
                self.click_multiplier = 1.25

            self.screen.fill((0, 0, 0))
            self.clickobj.update()
            self.clickup.update()
            self.lemonade_stand.update()
            if self.coins > 1000:
                self.coins1 = self.format_zahl(self.coins)
            else:
                self.coins1 = int(self.coins)
            self.coin_text = self.font_coins.render(f"Coins: {self.coins1}", True, (255, 255, 255))
            self.coin_rect = self.coin_text.get_rect(topleft=(330, 50))
            self.screen.blit(self.coin_text, self.coin_rect)
            self.price1 = self.format_zahl(self.price)
            if self.coins >= self.price:
                self.price_text = self.font_costs1.render(f"{self.price1}", True, (0, 0, 0))
            else:
                self.price_text = self.font_costs1.render(f"{self.price1}", True, (255, 0, 0))
            self.price_rect = self.price_text.get_rect(topleft=(950, 65))
            self.screen.blit(self.price_text, self.price_rect)
            self.coins_per_click_text = self.font_costs1.render(f"Coins per Click: {self.coins_per_click:.2f}".rstrip('0').rstrip('.'), True, (255, 255, 255))
            self.coins_per_click_rect = self.coins_per_click_text.get_rect(topleft=(20, 150))
            self.screen.blit(self.coins_per_click_text, self.coins_per_click_rect)
            self.click_multiplier_text = self.font_costs1.render(f"Coins/Click * {self.click_multiplier:.2f}".rstrip('0').rstrip('.'), True, (255, 255, 255))
            self.click_multiplier_rect = self.click_multiplier_text.get_rect(topleft=(750, 65))
            self.screen.blit(self.click_multiplier_text, self.click_multiplier_rect)




            pygame.display.update()
    

    pygame.quit()

game = Game()
        

