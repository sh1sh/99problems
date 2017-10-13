import pygame, sys

class Game(object):

    def __init__(self):
        # Configuration
        self.tps_max = 100.0

        # Initialization
        pygame.init()
        self.screen = pygame.display.set_mode((1280,720))
        self.tps_clock = pygame.time.Clock()
        self.tps_delta = 0.0

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
            pygame.display.flip()



    def tick(self):
        # Checking inputs
        keys = pygame.key.get_pressed()

    def draw(self):
        pygame.draw.rect(self.screen, (0, 150, 255), pygame.Rect(10,10,50,50))


if __name__ == '__main__':
    Game()