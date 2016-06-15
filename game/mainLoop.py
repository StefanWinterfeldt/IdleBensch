import pygame
import sys


def loop ():
    while True:
        for event in pygame.event.get ():
            if event.type == pygame.QUIT: sys.exit ()

        pygame.display.flip ()
