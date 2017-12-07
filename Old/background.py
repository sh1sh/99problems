import pygame, random
from pygame.math import Vector2

class Background(object):

    def __init__(self, game):
        self.game = game
        self.speed = 2.0
        self.gravity = 1

        size = self.game.screen.get_size()

        self.pos = Vector2(size[0] / 2, size[1] / 2)
        self.poz = Vector2(0, 0)
        self.acc = Vector2(0, 0)

        self.poz = [(random.randrange(0, 1280)), 0]

    def tick(self):
        # Physics
        #self.poz *= 0.8
        self.poz -= Vector2(0,-self.gravity)

        self.poz += self.acc
        self.pos += self.poz
        self.acc *= 0

        self.poz -= Vector2(0, -self.gravity)

    def draw(self):
        self.dd = random.randrange(0, 1280)
        #points = [Vector2(0, -10), Vector2(5, 5)]
        # Fix y axis
        #points = [Vector2(p.x,p.y*-1) for p in points]

        # Add current position
        #points = [Vector2(self.pos+p*2) for p in points]

        # Draw circle
        pygame.draw.circle(self.game.screen,(255,255,255),(self.dd,0),5)
        #pygame.draw.rect(self.game.screen,(255,255,255),self.poz)