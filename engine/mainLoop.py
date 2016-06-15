import constants.display as DC
import engine.view.mainView as mainView
import engine.keyHandler as keyHandler
import globals.gameState as gameState
import pygame
import sys

def updateDisplay ():
    mainView.update ()
    pygame.display.flip ()

def handleEvents ():
    for event in pygame.event.get ():
        if event.type == pygame.QUIT: sys.exit ()
        if event.type == pygame.KEYDOWN: keyHandler.handleKeyEvent (event)

def loop ():
    while True:
        gameState.clock.tick (DC.FRAMERATE)
        handleEvents ()
        updateDisplay ()
