import pygame

import shapes
import constants
from constants import Color
from groups import UPDATABLE, DRAWABLE
from shot import Shot


class Player(shapes.Circle, groups=(UPDATABLE, DRAWABLE)):
    const = constants.Player

    def __init__(self, at):
        super().__init__(at, radius=self.const.RADIUS)
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

    def move(self, dt: float):
        movement = pygame.math.Vector2(0, 1).rotate(self.rotation)
        self.position += movement * self.const.SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)

        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_s]:
            self.move(-dt)

        if keys[pygame.K_w]:
            self.move(dt)

        if keys[pygame.K_SPACE]:
            self.shoot()

    def shoot(self):
        shot_velocity = pygame.math.Vector2(0, 1).rotate(self.rotation)
        shot_velocity *= self.const.SHOT_SPEED
        shot = Shot(self.position, velocity=shot_velocity)
