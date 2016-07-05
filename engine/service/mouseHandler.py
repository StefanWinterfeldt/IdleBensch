import engine.controller.clickViewController as clickViewController
import engine.controller.faceViewController as faceViewController
import engine.controller.hintViewController as hintViewController
import engine.controller.moneyViewController as moneyViewController
import engine.controller.upgradeViewController as upgradeViewController
import engine.util.event as eventUtil
import globals.gameState as GGS
import globals.view as GV
import pygame

def dispatchClickToView (event):
    if eventUtil.eventHappenedInRect (event, GV.clickViewAbsoluteRect):
        clickViewController.handleClick (event)
    elif eventUtil.eventHappenedInRect (event, GV.upgradeViewAbsoluteRect):
        upgradeViewController.handleClick (event)

def dispatchMotionToView (event):
    if eventUtil.eventHappenedInRect (event, GV.clickViewAbsoluteRect):
        clickViewController.handleMotion (event)
    elif eventUtil.eventHappenedInRect (event, GV.moneyViewAbsoluteRect):
        moneyViewController.handleMotion (event)
    elif eventUtil.eventHappenedInRect (event, GV.hintViewAbsoluteRect):
        hintViewController.handleMotion (event)
    elif eventUtil.eventHappenedInRect (event, GV.faceViewAbsoluteRect):
        faceViewController.handleMotion (event)
    elif eventUtil.eventHappenedInRect (event, GV.upgradeViewAbsoluteRect):
        upgradeViewController.handleMotion (event)
    else:
        if GGS.currentMouseArea is not None:
            GGS.currentMouseArea = None
            hintViewController.clearText ()

def handleGameMouseEvent (event):
    if event.type == pygame.MOUSEBUTTONDOWN:
        dispatchClickToView (event)
    elif event.type == pygame.MOUSEMOTION:
        dispatchMotionToView (event)

def handleMenuMouseEvent (event):
    pass

def handleMouseEvent (event):
    if GGS.context == 'game':
        handleGameMouseEvent (event)
    elif GGS.context == 'menu':
        handleMenuMouseEvent (event)
