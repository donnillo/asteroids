import pygame
import random
from asteroid import Asteroid
from constants import DEFAULT_SCREEN as SCREEN
from groups import Groupable, UPDATABLE


class AsteroidField(Groupable, pygame.sprite.Sprite, groups=(UPDATABLE,)):
    edges = [
        [
            pygame.math.Vector2(1, 0),
            lambda y: pygame.math.Vector2(
                -Asteroid.const.MAX_RADIUS, y * SCREEN.height
            ),
        ],
        [
            pygame.math.Vector2(-1, 0),
            lambda y: pygame.math.Vector2(
                SCREEN.width + Asteroid.const.MAX_RADIUS, y * SCREEN.height
            ),
        ],
        [
            pygame.math.Vector2(0, 1),
            lambda x: pygame.math.Vector2(
                x * SCREEN.width, -Asteroid.const.MAX_RADIUS
            ),
        ],
        [
            pygame.math.Vector2(0, -1),
            lambda x: pygame.math.Vector2(
                x * SCREEN.width, SCREEN.height + Asteroid.const.MAX_RADIUS
            ),
        ],
    ]

    def __init__(self):
        super().__init__(*self.__class__.containers)
        self.spawn_timer = 0.0

    def spawn(self, radius, position, velocity):
        asteroid = Asteroid(position, radius=radius)
        asteroid.velocity = velocity

    def update(self, dt):
        self.spawn_timer += dt
        if self.spawn_timer > Asteroid.const.SPAWN_RATE / 1000:
            self.spawn_timer = 0

            # spawn a new asteroid at a random edge
            edge = random.choice(self.edges)
            speed = random.randint(40, 100)
            velocity = edge[0] * speed
            velocity = velocity.rotate(random.randint(-30, 30))
            position = edge[1](random.uniform(0, 1))
            kind = random.randint(1, Asteroid.const.KINDS)
            self.spawn(Asteroid.const.MIN_RADIUS * kind, position, velocity)
