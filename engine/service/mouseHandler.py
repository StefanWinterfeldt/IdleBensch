import engine.controller.clickViewController as clickViewController
import engine.controller.hintViewController as hintViewController
import globals.gameState as GGS
import globals.view as globalViews
import pygame

def dispatchClickToView (event):
    if globalViews.clickView.get_rect ().collidepoint (event.pos): clickViewController.handleClick (event.pos)

def dispatchMotionToView (event):
    if globalViews.clickView.get_rect ().collidepoint (event.pos): clickViewController.handleMotion (event.pos)
    else:
        GGS.currentMouseArea = None
        hintViewController.clearText ()

def handleMouseEvent (event):
    if event.type == pygame.MOUSEBUTTONDOWN: dispatchClickToView (event)
    elif event.type == pygame.MOUSEMOTION: dispatchMotionToView (event)
