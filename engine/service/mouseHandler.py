import engine.controller.clickViewController as clickViewController
import globals.view as globalViews
import pygame

def dispatchClickToView (event):
    if globalViews.clickView.get_rect ().collidepoint (event.pos):
        clickViewController.handleClick (event.pos)

def dispatchMotionToView (event):
    pass

def handleMouseEvent (event):
    if event.type == pygame.MOUSEBUTTONDOWN: dispatchClickToView (event)
    elif event.type == pygame.MOUSEMOTION: dispatchMotionToView (event)
