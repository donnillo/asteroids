import pygame
from pygame import Color

from constants import Screen


def main():
    screen = pygame.display.set_mode((Screen.WIDTH, Screen.HEIGHT))
    while True:
        screen.fill(Color("black"))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


if __name__ == "__main__":
    main()
