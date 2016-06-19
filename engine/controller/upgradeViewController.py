import constants.color as CC
import constants.display as CD
import engine.controller.hintViewController as hintViewController
import engine.util.event as eventUtil
import globals.gameState as GGS
import globals.upgrade.categories as UC
import globals.view as GV
import pygame


allMotionObjects = []
categoriesInitialized = 0

def initializeCategories ():
    for category in UC.categories:
        initializeCategory (category)

def initializeCategory (category):
    global allMotionObjects
    global categoriesInitialized
    setCategoryHeaderAbsoluteRect (category)
    setCategoryHeaderRelativeRect (category)
    category.header.areaCode = 'H' + str (categoriesInitialized)
    allMotionObjects.append (category.header)
    initializeUpgrades (category)
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

def initializeUpgrades (category):
    global allMotionObjects
    for i in range (len (category.upgrades)):
        setUpgradeAbsoluteRect (category.upgrades [i], i)
        setUpgradeRelativeRect (category.upgrades [i], i)
        category.upgrades [i].areaCode = 'U' + str (i * (categoriesInitialized + 1))
        allMotionObjects.append (category.upgrades [i])

def setUpgradeAbsoluteRect (upgrade, upgradeNumber):
    upgrade.absoluteRect = pygame.Rect (
        CD.UPGRADE_HEADER_SIZE [0] + 20 + (upgradeNumber % CD.UPGRADES_IN_A_ROW) * CD.UPGRADE_SIZE [0] + GV.upgradeViewAbsoluteRect [0],
        10 + categoriesInitialized * (CD.UPGRADE_HEADER_SIZE [1] + 10) + (upgradeNumber / CD.UPGRADES_IN_A_ROW) * CD.UPGRADE_SIZE [1] + GV.upgradeViewAbsoluteRect [1],
        CD.UPGRADE_SIZE [0],
        CD.UPGRADE_SIZE [1]
    )

def setUpgradeRelativeRect (upgrade, upgradeNumber):
    upgrade.relativeRect = pygame.Rect (
        CD.UPGRADE_HEADER_SIZE [0] + 20 + (upgradeNumber % CD.UPGRADES_IN_A_ROW) * CD.UPGRADE_SIZE [0],
        10 + categoriesInitialized * (CD.UPGRADE_HEADER_SIZE [1] + 10) + (upgradeNumber / CD.UPGRADES_IN_A_ROW) * CD.UPGRADE_SIZE [1],
        CD.UPGRADE_SIZE [0],
        CD.UPGRADE_SIZE [1]
    )

def handleMotion (event):
    motionWasHandled = False
    for motionObject in allMotionObjects:
        if eventUtil.eventHappenedInRect (event, motionObject.absoluteRect):
            handleMotionOnObject (motionObject)
            motionWasHandled = True
            break
    if not motionWasHandled:
        GGS.currentMouseArea = None
        hintViewController.clearText ()

def handleMotionOnObject (motionObject):
    if GGS.currentMouseArea != motionObject.areaCode:
        GGS.currentMouseArea = motionObject.areaCode
        hintViewController.showText (motionObject.hintText)

def initialize ():
    GV.upgradeViewAbsoluteRect = pygame.Rect ((0 + CD.CLICK_VIEW_SIZE [0], CD.MESSAGE_VIEW_SIZE [1], CD.UPGRADE_VIEW_SIZE [0], CD.UPGRADE_VIEW_SIZE [1]))
    GV.upgradeView = GV.mainView.subsurface (GV.upgradeViewAbsoluteRect)
    initializeCategories ()
    drawCategories ()
    pygame.draw.rect (GV.upgradeView, CC.DARK_GREEN, (0, 0, CD.UPGRADE_VIEW_SIZE [0] - 1, CD.UPGRADE_VIEW_SIZE [1] - 1), 2)

def update ():
    pass

def drawCategories ():
    for category in UC.categories:
        drawCategory (category)

def drawCategory (category):
    GV.upgradeView.blit (category.header.image, category.header.relativeRect)
    for upgrade in category.upgrades:
        GV.upgradeView.blit (upgrade.image, upgrade.relativeRect)
