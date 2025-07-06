import pygame
from pygame import Color

from constants import Screen
from player import Player


def main():
    screen = pygame.display.set_mode((Screen.WIDTH, Screen.HEIGHT))
    clock = pygame.time.Clock()
    player = Player(Screen.WIDTH / 2, Screen.HEIGHT / 2)

    while True:
        screen.fill(Color("black"))
        player.draw(screen)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
