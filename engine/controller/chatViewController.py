import constants.color as CC
import constants.display as CD
import globals.view as GV
import pygame

def initialize ():
    GV.chatViewAbsoluteRect = pygame.Rect ((CD.RESOLUTION [0] - CD.CHAT_VIEW_SIZE [0], CD.FACE_VIEW_SIZE [1], CD.CHAT_VIEW_SIZE [0], CD.CHAT_VIEW_SIZE [1]))
    GV.chatView = GV.mainView.subsurface (GV.chatViewAbsoluteRect)
    pygame.draw.rect (GV.chatView, CC.DARK_GREEN, (0, 0, CD.CHAT_VIEW_SIZE [0] - 1, CD.CHAT_VIEW_SIZE [1] - 1), 2)

def update ():
    pass
