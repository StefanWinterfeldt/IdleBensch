import constants.color as CC
import constants.display as CD
import engine.util.color as colorUtil
import engine.util.draw as drawUtil
import engine.util.text as textUtil
import globals.gameState as GS
import globals.subscriberMilestones as milestones
import globals.view as GV
import pygame


currentMilestone = None
lastMilestone = None
progressSurface = None
textSurface = None

def switchMilestonesIfPossible ():
    global currentMilestone
    global lastMilestone
    if currentMilestone is not None:
        if GS.subscriber > currentMilestone.subscribersNeeded:
            lastMilestone = currentMilestone
            currentMilestone = milestones.getNextMilestone (currentMilestone)
            drawText ()

def getProgressPercentage ():
    start = 0 if lastMilestone is None else lastMilestone.subscribersNeeded
    end = currentMilestone.subscribersNeeded
    return (GS.subscriber - start) / (end - start)

def drawText ():
    if lastMilestone is not None:
        textSurface.fill (CC.BLACK)
        drawUtil.drawCentered(textUtil.renderLines (['Du hast mehr Subscriber als: ' + lastMilestone.name], False, 32), textSurface)

def drawProgress ():
    progressSurface.fill (CC.BLACK)
    if currentMilestone is not None:
        progressPercentage = getProgressPercentage ()
        progressMeterWidth = progressSurface.get_width () * progressPercentage
        pygame.draw.rect (progressSurface, colorUtil.getColorFromGradient (CC.RED, CC.GREEN, progressPercentage), (0, (progressSurface.get_height () / 2) - 30, progressMeterWidth, 60))

def initializeMilestones ():
    global currentMilestone
    currentMilestone = milestones.sortedMilestones [0]

def initialize ():
    global progressSurface
    global textSurface
    GV.achievementViewAbsoluteRect = pygame.Rect ((0 + CD.CLICK_VIEW_SIZE [0], CD.MESSAGE_VIEW_SIZE [1] + CD.UPGRADE_VIEW_SIZE [1], CD.ACHIEVEMENT_VIEW_SIZE [0], CD.ACHIEVEMENT_VIEW_SIZE [1]))
    GV.achievementView = GV.gameView.subsurface (GV.achievementViewAbsoluteRect)
    textSurface = GV.achievementView.subsurface ((0, 0, GV.achievementView.get_width (), GV.achievementView.get_height () / 2))
    progressSurface = GV.achievementView.subsurface ((0, GV.achievementView.get_height () / 2, GV.achievementView.get_width (), GV.achievementView.get_height () / 2))
    initializeMilestones ()
    pygame.draw.rect (GV.achievementView, CC.DARK_GREEN, (0, 0, CD.ACHIEVEMENT_VIEW_SIZE [0] - 1, CD.ACHIEVEMENT_VIEW_SIZE [1] - 1), 2)

def update ():
    switchMilestonesIfPossible()
    drawProgress()
    pygame.draw.rect (GV.achievementView, CC.DARK_GREEN, (0, 0, CD.ACHIEVEMENT_VIEW_SIZE [0] - 1, CD.ACHIEVEMENT_VIEW_SIZE [1] - 1), 2)
