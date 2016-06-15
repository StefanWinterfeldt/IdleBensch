import constants.display as DC
import pygame
import sys

pygame.init ()

screen = pygame.display.set_mode (DC.RESOLUTION, pygame.FULLSCREEN|pygame.HWSURFACE)
screen.fill ((0, 0, 0))

while True:
    for event in pygame.event.get ():
        if event.type == pygame.QUIT: sys.exit ()

    pygame.display.flip ()
