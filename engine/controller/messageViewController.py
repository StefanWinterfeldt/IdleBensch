import constants.color as CC
import constants.control as CO
import constants.display as CD
import engine.util.draw as drawUtil
import engine.util.text as textUtil
import globals.messages as messages
import globals.view as GV
import pygame
import random


ticksSinceLastMessage = 0

def getAvailableMessages ():
    return [message for message in messages.messages if message.isAvailable ()]

def showRandomMessage ():
    GV.messageView.fill (CC.BLACK)
    pygame.draw.rect (GV.messageView, CC.DARK_GREEN, (0, 0, CD.MESSAGE_VIEW_SIZE [0] - 1, CD.MESSAGE_VIEW_SIZE [1] - 1), 2)
    availableMessages = getAvailableMessages ()
    if len (availableMessages) >= 1:
        chosenMessage = random.choice (availableMessages)
        drawUtil.drawCentered (textUtil.renderTextWithWordWrap (chosenMessage.text, CD.MESSAGE_VIEW_SIZE [0] - 10), GV.messageView)

def initialize ():
    GV.messageViewAbsoluteRect = pygame.Rect ((0 + CD.CLICK_VIEW_SIZE [0], 0, CD.MESSAGE_VIEW_SIZE [0], CD.MESSAGE_VIEW_SIZE [1]))
    GV.messageView = GV.gameView.subsurface (GV.messageViewAbsoluteRect)
    showRandomMessage ()

def update ():
    global ticksSinceLastMessage
    if ticksSinceLastMessage >= (CO.SECONDS_BETWEEN_MESSAGES * CD.FRAME_RATE):
        showRandomMessage ()
        ticksSinceLastMessage = 0
    ticksSinceLastMessage += 1
