import engine.controller.upgradeViewController as upgradeViewController
import engine.util.upgrade as upgradeUtil
import globals.gameLogic as GL
import pygame
import sys

def handleKeyEvent (event):
    if event.key == pygame.K_ESCAPE:
        sys.exit ()
    elif event.key == pygame.K_v and GL.DEV_MODE:
        upgradeUtil.makeAllUpgradesVisible ()
        upgradeViewController.drawCategories ()
    elif event.key == pygame.K_c and GL.DEV_MODE:
        upgradeUtil.setAllCostsToZero ()
