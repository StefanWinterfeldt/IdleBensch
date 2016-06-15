import constants.color as color
import constants.display as DC
import engine.service.idleGameNameGenerator as IGNG
import engine.util.draw as draw
import globals.view as view
import pygame

def initialize ():
    view.clickView = view.mainView.subsurface ((DC.RESOLUTION [0] - 1 - DC.CLICKVIEWSIZE [0], 0, DC.CLICKVIEWSIZE [0], DC.CLICKVIEWSIZE [1]))
    draw.drawCentered (IGNG.generateIdleGameName (), view.clickView)

def update ():
    pygame.draw.rect (view.clickView, color.DARKGREEN, (0, 0, DC.CLICKVIEWSIZE [0] - 1, DC.CLICKVIEWSIZE [1] - 1), 2)
