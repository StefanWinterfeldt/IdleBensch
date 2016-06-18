import constants.color as CC
import constants.display as CD
import engine.controller.hintViewController as hintViewController
import engine.util.draw as drawUtil
import engine.util.event as eventUtil
import engine.util.text as textUtil
import globals.gameState as GGS
import globals.view as GV
import pygame


activeSections = []
episodeSection = None
episodeSectionAbsoluteRect = None
episodeSectionAreaCode = 'MVES'
episodeSectionHintText = 'Folgen produzieren Views und mit einer gewissen Chance auch Abonnenten.'
seasonSection = None
seasonSectionAbsoluteRect = None
seasonSectionAreaCode = 'MVSS'
seasonSectionHintText = 'Staffeln produzieren eine garantiere Anzahl von Abonnenten.'
sectionSize = (360, 60)
streamSection = None
streamSectionAbsoluteRect = None
streamSectionAreaCode = 'MVSTS'
streamSectionHintText = 'Streams produzieren Abonnenten und Geld durch Spenden.'

def drawEpisodeSection ():
    drawUtil.drawCentered (textUtil.renderLines (['Folgen:', str (GGS.episodes)], True), episodeSection)
    pygame.draw.rect (episodeSection, CC.DARK_GREEN, episodeSection.get_rect (), 1)

def drawSeasonSection ():
    drawUtil.drawCentered (textUtil.renderLines (['Staffeln:', str (GGS.seasons)], True), seasonSection)
    pygame.draw.rect (seasonSection, CC.DARK_GREEN, seasonSection.get_rect (), 1)

def drawStreamSection ():
    drawUtil.drawCentered (textUtil.renderLines (['Streams:', str (GGS.streams)], True), streamSection)
    pygame.draw.rect (streamSection, CC.DARK_GREEN, streamSection.get_rect (), 1)

def drawSections ():
    if episodeSection in activeSections:
        drawEpisodeSection ()
    if seasonSection in activeSections:
        drawSeasonSection ()
    if streamSection in activeSections:
        drawStreamSection ()

def handleEmptySectionMotion ():
    if GGS.currentMouseArea is not None:
        GGS.currentMouseArea = None
        hintViewController.clearText ()

def handleEpisodeSectionMotion ():
    if GGS.currentMouseArea != episodeSectionAreaCode:
        GGS.currentMouseArea = episodeSectionAreaCode
        hintViewController.showText (episodeSectionHintText)

def handleSeasonSectionMotion ():
    if GGS.currentMouseArea != seasonSectionAreaCode:
        GGS.currentMouseArea = seasonSectionAreaCode
        hintViewController.showText (seasonSectionHintText)

def handleStreamSectionMotion ():
    if GGS.currentMouseArea != streamSectionAreaCode:
        GGS.currentMouseArea = streamSectionAreaCode
        hintViewController.showText (streamSectionHintText)

def handleMotion (event):
    if eventUtil.eventHappenedInRect (event, episodeSectionAbsoluteRect):
        handleEpisodeSectionMotion ()
    elif eventUtil.eventHappenedInRect (event, seasonSectionAbsoluteRect):
        handleSeasonSectionMotion ()
    elif eventUtil.eventHappenedInRect (event, streamSectionAbsoluteRect):
        handleStreamSectionMotion ()
    else:
        handleEmptySectionMotion ()

def initialize ():
    GV.moneyViewAbsoluteRect = pygame.Rect ((0, CD.CLICK_VIEW_SIZE [1] - 1, CD.MONEY_VIEW_SIZE [0], CD.MONEY_VIEW_SIZE [1]))
    GV.moneyView = GV.mainView.subsurface (GV.moneyViewAbsoluteRect)
    initializeEpisodeSection ()
    initializeSeasonSection ()
    initializeStreamSection ()
    pygame.draw.rect (GV.moneyView, CC.DARK_GREEN, (0, 0, CD.MONEY_VIEW_SIZE [0] - 1, CD.MONEY_VIEW_SIZE [1] - 1), 2)

def initializeEpisodeSection ():
    global activeSections
    global episodeSectionAbsoluteRect
    global episodeSection
    episodeSectionAbsoluteRect = pygame.Rect (GV.moneyViewAbsoluteRect [0], GV.moneyViewAbsoluteRect [1], sectionSize [0], sectionSize [1])
    episodeSection = GV.moneyView.subsurface ((0, 0, sectionSize [0], sectionSize [1]))
    activeSections.append (episodeSection)

def initializeSeasonSection ():
    global activeSections
    global seasonSectionAbsoluteRect
    global seasonSection
    seasonSectionAbsoluteRect = pygame.Rect (GV.moneyViewAbsoluteRect [0], GV.moneyViewAbsoluteRect [1] + sectionSize [1], sectionSize [0], sectionSize [1])
    seasonSection = GV.moneyView.subsurface ((0, sectionSize [1], sectionSize [0], sectionSize [1]))
    activeSections.append (seasonSection)
    
def initializeStreamSection ():
    global activeSections
    global streamSectionAbsoluteRect
    global streamSection
    streamSectionAbsoluteRect = pygame.Rect (GV.moneyViewAbsoluteRect [0], GV.moneyViewAbsoluteRect [1] + (sectionSize [1]*2), sectionSize [0], sectionSize [1])
    streamSection = GV.moneyView.subsurface ((0, (sectionSize [1]*2), sectionSize [0], sectionSize [1]))
    activeSections.append (streamSection)

def update ():
    GV.moneyView.fill (CC.BLACK)
    drawSections ()
    pygame.draw.rect (GV.moneyView, CC.DARK_GREEN, (0, 0, CD.MONEY_VIEW_SIZE [0] - 1, CD.MONEY_VIEW_SIZE [1] - 1), 2)
