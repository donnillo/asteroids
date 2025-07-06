import pygame
from pygame import Color

import constants as const
from circleshape import CircleShape


class Player(CircleShape):
    def __init__(self, x: float, y: float):
        super().__init__(x, y, const.Player.RADIUS)
        self.rotation = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(
            self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, Color("white"), self.triangle(), 2)
