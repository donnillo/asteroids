import pygame

import constants
from constants import Color
from circleshape import CircleShape


class Player(CircleShape):
    const = constants.Player

    def __init__(self, x: float, y: float):
        super().__init__(x, y, self.const.RADIUS)
        self.rotation = 0

    @property
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(
            self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, Color.WHITE, self.triangle, 2)

    def rotate(self, dt: float):
        self.rotation += self.const.TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)

        if keys[pygame.K_d]:
            self.rotate(dt)
