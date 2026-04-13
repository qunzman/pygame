import pygame
import clickobj
import Upgrades

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1000, 600))
        self.clock = pygame.time.Clock()
        self.running = True
        self.coinimg = pygame.image.load("img/coin.png")
        self.coinimage = pygame.transform.scale(self.coinimg, (70, 70))
        self.coinimage2 = pygame.transform.scale(self.coinimg, (30, 30))
        self.clickobj = clickobj.clickobj(self, 480, 300, 400, pygame.image.load("img/coin.png"))
        self.coins = 0
        self.font_coins = pygame.font.SysFont("Misc fixed", 64)
        self.font_costs1 = pygame.font.SysFont("Misc fixed", 28)
        self.font_farmdescr = pygame.font.SysFont("Misc fixed", 24)
        self.font_coinpersec = pygame.font.SysFont("Misc fixed", 18)
        self.font_farmstats = pygame.font.SysFont("Misc fixed", 26)
        self.clickup = Upgrades.upgrades(self, 50, 300, 50, pygame.image.load("img/Clickup.png"))
        self.coins_per_click = 1
        self.clickup_price = 10
        self.lemonadestand_price = 200
        self.icestand_price = 1000
        self.icestand_multiplier = 5
        self.click_multiplier = 1.15
        self.lemonade_stand = Upgrades.upgrades(self, 100, 300, 50, pygame.image.load("img/Lemonade_stand.png"))
        self.icestand = Upgrades.upgrades(self, 150, 300, 50, pygame.image.load("img/Lemonade_stand.png"))
        self.lemonadestands = 0
        self.icestands = 0
        self.lemonadestandmultiplier = 0.5
        self.icestand_price_multiplier = 0
        self.lemonadestand_price_multiplier = 0
        self.farmevent = pygame.USEREVENT + 1
        pygame.time.set_timer(self.farmevent, 1000)
        self.Coinspersec = 0
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
                        self.clickobj.animation()
                    if self.clickup.is_clicked(event.pos) and self.coins >= self.clickup_price:
                        self.coins_per_click *= self.click_multiplier
                        self.coins -= self.clickup_price
                        self.clickup_price = int(self.clickup_price * 2.5)
                    if self.lemonade_stand.is_clicked(event.pos) and self.coins >= self.lemonadestand_price:
                        self.Coinspersec += self.lemonadestandmultiplier
                        self.lemonadestand_price += self.lemonadestand_price_multiplier
                        self.lemonadestands += 1
                        self.coins -= self.lemonadestand_price
                        if self.lemonadestands == 20:
                            self.lemonadestandmultiplier = 1
                            self.lemonadestand_price_multiplier = 5
                    if self.icestand.is_clicked(event.pos) and self.coins >= self.icestand_price:
                        self.Coinspersec += self.icestand_multiplier
                        self.icestand_price += self.icestand_price_multiplier
                        self.icestands += 1
                        self.coins -= self.icestand_price
                        if self.icestands == 20:
                            self.icestand_multiplier = 1
                            self.icestand_price_multiplier = 5

                elif event.type == self.farmevent:
                    self.coins += self.Coinspersec
                        
            if self.coins_per_click >= 2:
                self.click_multiplier = 1.25

        

            self.screen.fill((0, 0, 0))
            self.clickobj.update()
            self.clickup.update()
            self.lemonade_stand.update()
            self.icestand.update()

            self.screen.blit(self.coinimage, (400, 35))
            self.screen.blit(self.coinimage2, (920, 107))
            self.screen.blit(self.coinimage2, (920, 57))
            self.screen.blit(self.coinimage2, (920, 157))
            
            
            if self.coins > 1000:
                self.coins1 = self.format_zahl(self.coins)
            else:
                self.coins1 = int(self.coins)
            self.coin_text = self.font_coins.render(f"{self.coins1}", True, (255, 255, 255))
            self.coin_rect = self.coin_text.get_rect(topleft=(470, 50))
            self.screen.blit(self.coin_text, self.coin_rect)

            self.clickup_price1 = self.format_zahl(self.clickup_price)
            if self.coins >= self.clickup_price:
                self.price_text = self.font_costs1.render(f"{self.clickup_price1}", True, (0, 0, 0))
            else:
                self.price_text = self.font_costs1.render(f"{self.clickup_price1}", True, (255, 0, 0))
            self.price_rect = self.price_text.get_rect(topleft=(950, 65))
            self.screen.blit(self.price_text, self.price_rect)


            self.coins_per_click_text = self.font_costs1.render(f"Coins per Click: {self.coins_per_click:.2f}".rstrip('0').rstrip('.'), True, (255, 255, 255))
            self.coins_per_click_rect = self.coins_per_click_text.get_rect(topleft=(20, 150))
            self.screen.blit(self.coins_per_click_text, self.coins_per_click_rect)
            self.click_farmdesc_text = self.font_farmdescr.render("Clicker", True, (255, 255, 255))
            self.click_farmdesc_rect = self.click_farmdesc_text.get_rect(topleft=(750, 60))
            self.screen.blit(self.click_farmdesc_text, self.click_farmdesc_rect)
            self.click_multiplier_text = self.font_coinpersec.render(f"Coins per Click * {self.click_multiplier:.2f}".rstrip('0').rstrip('.'), True, (255, 255, 255))
            self.click_multiplier_rect = self.click_multiplier_text.get_rect(topleft=(750, 75))
            self.screen.blit(self.click_multiplier_text, self.click_multiplier_rect)


            self.click_Coin_per_second_text = self.font_costs1.render(f"Coins per Second: {self.Coinspersec:.1f}".rstrip('0').rstrip('.'), True, (255, 255, 255))
            self.click_Coin_per_second_rect = self.click_Coin_per_second_text.get_rect(topleft=(20, 180))
            self.screen.blit(self.click_Coin_per_second_text, self.click_Coin_per_second_rect)


            self.click_farmdesc_text = self.font_farmdescr.render("Lemonade Stand", True, (255, 255, 255))
            self.click_farmdesc_rect = self.click_farmdesc_text.get_rect(topleft=(750, 110))
            self.screen.blit(self.click_farmdesc_text, self.click_farmdesc_rect)
            self.click_farmdesc_text = self.font_coinpersec.render("Coins per Second + 0.5", True, (255, 255, 255))
            self.click_farmdesc_rect = self.click_farmdesc_text.get_rect(topleft=(750, 125))
            self.screen.blit(self.click_farmdesc_text, self.click_farmdesc_rect)            
            self.lemonadestand_price1 = self.format_zahl(self.lemonadestand_price)
            if self.coins >= self.lemonadestand_price:
                self.lemonadestand_price_text = self.font_costs1.render(f"{self.lemonadestand_price1}", True, (0, 0, 0))
            else:
                self.lemonadestand_price_text = self.font_costs1.render(f"{self.lemonadestand_price1}", True, (255, 0, 0))
            self.lemonadestand_price_rect = self.lemonadestand_price_text.get_rect(topleft=(950, 115))
            self.screen.blit(self.lemonadestand_price_text, self.lemonadestand_price_rect)
            self.lemonadefarms_text = self.font_farmstats.render(f"Lemonade stands: {self.lemonadestands}", True, (255, 255, 255))
            self.lemonadefarms_rect = self.lemonadefarms_text.get_rect(topleft=(20, 210))
            self.screen.blit(self.lemonadefarms_text, self.lemonadefarms_rect)


            self.click_farmdesc_text = self.font_farmdescr.render("Icestand", True, (255, 255, 255))
            self.click_farmdesc_rect = self.click_farmdesc_text.get_rect(topleft=(750, 157))
            self.screen.blit(self.click_farmdesc_text, self.click_farmdesc_rect)
            self.icestand_farmdesc_text = self.font_coinpersec.render("Coins per Second + 1", True, (255, 255, 255))
            self.icestand_farmdesc_rect = self.icestand_farmdesc_text.get_rect(topleft=(750, 175))
            self.screen.blit(self.icestand_farmdesc_text, self.icestand_farmdesc_rect)           
            self.icestand_price1 = self.format_zahl(self.icestand_price)
            if self.coins >= self.icestand_price:
                self.icestand_price_text = self.font_costs1.render(f"{self.icestand_price1}", True, (0, 0, 0))
            else:
                self.icestand_price_text = self.font_costs1.render(f"{self.icestand_price1}", True, (255, 0, 0))
            self.icestand_price_rect = self.icestand_price_text.get_rect(topleft=(950, 165))
            self.screen.blit(self.icestand_price_text, self.icestand_price_rect)
            self.icestands_text = self.font_farmstats.render(f"Ice stands: {self.icestands}", True, (255, 255, 255))
            self.icestands_rect = self.icestands_text.get_rect(topleft=(20, 235))
            self.screen.blit(self.icestands_text, self.icestands_rect)

            pygame.display.update() 
            self.clock.tick(60)  
    

    pygame.quit()

game = Game()
        

