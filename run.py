import pygame, sys
<<<<<<< HEAD
from rocket import Rocket

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
        self.player.tick()


    def draw(self):
        self.player.draw()



if __name__ == '__main__':
    Game()
=======

max_tps = 70

pygame.init()
screen = pygame.display.set_mode((1280,720))
box = pygame.Rect(10,10,50,50)
clock = pygame.time.Clock()
delta = 0.0

while True:
    #Handling events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            sys.exit(0)

    #Ticking
    delta += clock.tick()/1000.0
    while delta > 1/max_tps:
        delta -= 1/max_tps
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            box.x += 1
        if keys[pygame.K_s]:
            box.y += 1
        if keys[pygame.K_w]:
            box.y -= 1
        if keys[pygame.K_a]:
            box.x -= 1

    #Input


    #Drawing
    screen.fill((0,0,0))
    pygame.draw.rect(screen, (0,150,255), box)
    pygame.display.flip()
>>>>>>> master
