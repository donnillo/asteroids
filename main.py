import pygame

from constants import Screen
from constants import Color
from player import Player


def main():
    screen = pygame.display.set_mode(Screen.size)
    clock = pygame.time.Clock()
    player = Player(*Screen.center)

    while True:
        screen.fill(Color.BLACK)
        player.draw(screen)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60) / 1000
        player.update(dt)


if __name__ == "__main__":
    main()
