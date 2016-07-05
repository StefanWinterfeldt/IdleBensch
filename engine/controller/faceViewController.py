import constants.color as CC
import constants.display as CD
import engine.controller.hintViewController as hintViewController
import engine.util.draw as drawUtil
import engine.util.text as textUtil
import globals.gameState as GGS
import globals.view as GV
import pygame

areaCode = 'FV'
hintText = 'Hier ist Platz fuer deine Face-Cam.'

def handleMotion (event):
    if GGS.currentMouseArea != areaCode:
        GGS.currentMouseArea = areaCode
        hintViewController.showText (hintText)

def initialize ():
    GV.faceViewAbsoluteRect = pygame.Rect ((CD.RESOLUTION [0] - CD.FACE_VIEW_SIZE [0], 0, CD.FACE_VIEW_SIZE [0], CD.FACE_VIEW_SIZE [1]))
    GV.faceView = GV.gameView.subsurface (GV.faceViewAbsoluteRect)
    drawUtil.drawCentered (textUtil.renderLines(['A Place', 'For Your Face'], True, CD.FACE_VIEW_FONT_SIZE), GV.faceView)
    pygame.draw.rect (GV.faceView, CC.DARK_GREEN, (0, 0, CD.FACE_VIEW_SIZE [0] - 1, CD.FACE_VIEW_SIZE [1] - 1), 2)

def update ():
    pass
