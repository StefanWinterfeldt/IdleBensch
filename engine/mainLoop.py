import constants.display as DC
import engine.service.keyHandler as keyHandler
import engine.service.mouseHandler as mouseHandler
import engine.controller.mainViewController as mainViewController
import globals.gameState as gameState
import pygame
import sys

def updateDisplay ():
    mainViewController.update ()
    pygame.display.flip ()

def handleEvents ():
    for event in pygame.event.get ():
        if event.type == pygame.QUIT: sys.exit ()
        if event.type == pygame.KEYDOWN: keyHandler.handleKeyEvent (event)
        if event.type == pygame.MOUSEBUTTONDOWN: mouseHandler.handleMouseEvent (event)

def loop ():
    while True:
        gameState.clock.tick (DC.FRAME_RATE)
        handleEvents ()
        updateDisplay ()
