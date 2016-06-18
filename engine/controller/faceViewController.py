import constants.color as CC
import constants.display as CD
import globals.view as GV
import pygame

def initialize ():
    GV.faceViewAbsoluteRect = pygame.Rect ((CD.RESOLUTION [0] - CD.FACE_VIEW_SIZE [0], 0, CD.FACE_VIEW_SIZE [0], CD.FACE_VIEW_SIZE [1]))
    GV.faceView = GV.mainView.subsurface (GV.faceViewAbsoluteRect)
    pygame.draw.rect (GV.faceView, CC.DARK_GREEN, (0, 0, CD.FACE_VIEW_SIZE [0] - 1, CD.FACE_VIEW_SIZE [1] - 1), 2)

def update ():
    pass
