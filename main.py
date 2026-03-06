import pygame
import player
import coin
import random

class Game:
    def __init__(self):
        pygame.init()
        self.window_widht = 800
        self.window_height = 600
        self.window = pygame.display.set_mode((self.window_widht, self.window_height))
        pygame.display.set_caption("Coin Collector")
        self.clock = pygame.time.Clock()
        self.score = 0
        self.font = pygame.font.SysFont("Misc fixed", 32)
        self.player = [player.Player(self, 32, 32)]
        self.coins = []
        self.run()

    def run(self, ):
        SPAWN_INTERVAL = 3000
        last_spawn = 0
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    running = False

            self.delta_time = self.clock.tick(60) / 1000
            self.window.fill((25, 25, 50))
            self.score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
            self.score_rect = self.score_text.get_rect(topleft=(10, 10))
            self.window.blit(self.score_text, self.score_rect)
            for player in self.player:
                player.update()
                if self.coins:
                    pass
                else:
                    self.player.remove(player)
            now = pygame.time.get_ticks()
            if now - last_spawn >= SPAWN_INTERVAL:
                x = random.randint(0, self.window_widht)
                y = random.randint(0, self.window_height)
                self.coins += coin.coin(self, x, y)
            
            for coin in self.coins:
                coin.update()
                if coin.is_destroyed:
                    self.coins.remove(coin)
                    self.score += 1

           
                

            pygame.display.update()


    pygame.quit()

game = Game()
