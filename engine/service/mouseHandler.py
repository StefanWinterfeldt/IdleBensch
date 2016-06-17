import engine.controller.clickViewController as clickViewController
import engine.controller.hintViewController as hintViewController
import globals.gameState as GGS
import globals.view as GV
import pygame

def dispatchClickToView (event):
    if eventHappenedInRect (event, GV.clickViewAbsoluteRect): clickViewController.handleClick (event.pos)

def dispatchMotionToView (event):
    if eventHappenedInRect (event, GV.clickViewAbsoluteRect):
        clickViewController.handleMotion (event.pos)
    elif eventHappenedInRect (event, GV.hintViewAbsoluteRect):
        hintViewController.handleMotion (event.pos)
    else:
        if GGS.currentMouseArea is not None:
            GGS.currentMouseArea = None
            hintViewController.clearText ()

def eventHappenedInRect (event, rect):
    return rect.collidepoint (event.pos)

def handleMouseEvent (event):
    if event.type == pygame.MOUSEBUTTONDOWN:
        dispatchClickToView (event)
    elif event.type == pygame.MOUSEMOTION:
        dispatchMotionToView (event)
