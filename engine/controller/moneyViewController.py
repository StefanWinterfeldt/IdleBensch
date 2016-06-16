import constants.color as color
import constants.display as DC
import globals.view as view
import pygame

def initialize ():
    view.moneyView = view.mainView.subsurface ((0, DC.CLICKVIEWSIZE[1]-1, DC.MONEYVIEWSIZE [0], DC.MONEYVIEWSIZE [1]))

def update ():
    pygame.draw.rect (view.moneyView, color.DARKGREEN, (0, 0, DC.MONEYVIEWSIZE [0] - 1, DC.MONEYVIEWSIZE [1] - 1), 2)