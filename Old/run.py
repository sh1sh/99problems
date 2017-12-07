import pygame
import sys
from background import Background

from Old.rocket import Rocket


class Game(object):

    def __init__(self):
        # Configuration
        self.tps_max = 100.0

        # Initialization
        pygame.init()
        self.screen = pygame.display.set_mode((1280,720))
        self.tps_clock = pygame.time.Clock()
        self.tps_delta = 0.0

        self.player = Rocket(self)
        self.backgroung = Background(self)

        while True:
            # Handling events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    sys.exit(0)

            # Ticking
            self.tps_delta += self.tps_clock.tick() / 1000.0
            while self.tps_delta > 1 / self.tps_max:
                self.tick()
                self.tps_delta -= 1 / self.tps_max

            # Drawing
            self.screen.fill((0, 0, 0))
            self.draw()
            #self.backgroung.draw()
            pygame.display.flip()



    def tick(self):
        self.player.tick()
        self.backgroung.tick()


    def draw(self):
        self.player.draw()
        self.backgroung.draw()



if __name__ == '__main__':
    Game()