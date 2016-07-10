import engine.controller.upgradeViewController as upgradeViewController
import engine.util.upgrade as upgradeUtil
import globals.gameLogic as GL
import globals.gameState as GS
import pygame
import sys

def handleGameKeyEvent (event):
    if event.key == pygame.K_ESCAPE:
        GS.context = 'menu'
    elif event.key == pygame.K_v and GL.DEV_MODE:
        upgradeUtil.makeAllUpgradesVisible ()
        upgradeViewController.drawCategories ()
    elif event.key == pygame.K_c and GL.DEV_MODE:
        upgradeUtil.setAllCostsToZero ()

def handleMenuKeyEvent (event):
    if event.key == pygame.K_ESCAPE:
        GS.context = 'game'

def handleCreditsEvent (event):
    if event.key == pygame.K_ESCAPE:
        sys.exit ()

def handleKeyEvent (event):
    if GS.context == 'game':
        handleGameKeyEvent (event)
    elif GS.context == 'menu':
        handleMenuKeyEvent (event)
    elif GS.context == 'credits':
        handleCreditsEvent (event)
