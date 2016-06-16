import constants.color as color
import constants.display as DC
import engine.service.idleGameNameGenerator as IGNG
import engine.util.color as colorUtil
import engine.util.draw as draw
import globals.view as view
import pygame
import random

def handleClick (position):
    randomize ()

def initialize ():
    view.clickView = view.mainView.subsurface ((0, 0, DC.CLICKVIEWSIZE [0], DC.CLICKVIEWSIZE [1]))
    randomize()

def randomize ():
    backgroundColor = random.choice (color.CLICKVIEWCOLORS)
    view.clickView.fill (backgroundColor)
    draw.drawCentered (IGNG.generateIdleGameName (colorUtil.invertColor(backgroundColor), backgroundColor), view.clickView)
    pygame.draw.rect (view.clickView, color.DARKGREEN, (0, 0, DC.CLICKVIEWSIZE [0] - 1, DC.CLICKVIEWSIZE [1] - 1), 2)

def update ():
   pass
