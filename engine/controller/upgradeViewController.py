import constants.color as CC
import constants.display as CD
import engine.controller.hintViewController as hintViewController
import engine.util.event as eventUtil
import globals.gameState as GGS
import globals.upgrade.categories as UC
import globals.view as GV
import pygame


categoriesInitialized = 0

def initializeCategories ():
    for category in UC.categories:
        initializeCategory (category)

def initializeCategory (category):
    global categoriesInitialized
    setCategoryHeaderAbsoluteRect (category)
    setCategoryHeaderRelativeRect (category)
    category.header.areaCode = categoriesInitialized
    categoriesInitialized += 1

def setCategoryHeaderAbsoluteRect (category):
    category.header.absoluteRect = pygame.Rect (
        GV.upgradeViewAbsoluteRect [0] + 10,
        GV.upgradeViewAbsoluteRect [1] + 10 + categoriesInitialized * (CD.UPGRADE_HEADER_SIZE [1] + 10),
        CD.UPGRADE_HEADER_SIZE [0],
        CD.UPGRADE_HEADER_SIZE [1]
    )

def setCategoryHeaderRelativeRect (category):
    category.header.relativeRect = pygame.Rect (
        10,
        10 + categoriesInitialized * (CD.UPGRADE_HEADER_SIZE [1] + 10),
        CD.UPGRADE_HEADER_SIZE [0],
        CD.UPGRADE_HEADER_SIZE [1]
    )

def handleMotion (event):
    motionWasHandled = False
    for header in [category.header for category in UC.categories]:
        if eventUtil.eventHappenedInRect (event, header.absoluteRect):
            handleMotionInHeader (header)
            motionWasHandled = True
            break
    if not motionWasHandled:
        GGS.currentMouseArea = None
        hintViewController.clearText ()

def handleMotionInHeader (header):
    if GGS.currentMouseArea != header.areaCode:
        GGS.currentMouseArea = header.areaCode
        hintViewController.showText (header.hintText)

def initialize ():
    GV.upgradeViewAbsoluteRect = pygame.Rect ((0 + CD.CLICK_VIEW_SIZE [0], CD.MESSAGE_VIEW_SIZE [1], CD.UPGRADE_VIEW_SIZE [0], CD.UPGRADE_VIEW_SIZE [1]))
    GV.upgradeView = GV.mainView.subsurface (GV.upgradeViewAbsoluteRect)
    initializeCategories ()

def update ():
    drawCategories ()
    pygame.draw.rect (GV.upgradeView, CC.DARK_GREEN, (0, 0, CD.UPGRADE_VIEW_SIZE [0] - 1, CD.UPGRADE_VIEW_SIZE [1] - 1), 2)

def drawCategories ():
    for category in UC.categories:
        drawCategory (category)

def drawCategory (category):
    GV.upgradeView.blit (category.header.image, category.header.relativeRect)
