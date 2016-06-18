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
subscriberSection = None
subscriberSectionAbsoluteRect = None
subscriberSectionAreaCode = 'MVSUS'
subscriberSectionHintText = 'Abonnenten produzieren staendig Views und Geld durch Merchandise.'
viewSection = None
viewSectionAbsoluteRect = None
viewSectionAreaCode = 'MVVS'
viewSectionHintText = 'Views produzieren Geld durch Werbung.'

def drawEpisodeSection ():
    drawUtil.drawCentered (textUtil.renderLines (['Folgen:', str (GGS.episodes)], True), episodeSection)
    pygame.draw.rect (episodeSection, CC.DARK_GREEN, episodeSection.get_rect (), 1)

def drawSeasonSection ():
    drawUtil.drawCentered (textUtil.renderLines (['Staffeln:', str (GGS.seasons)], True), seasonSection)
    pygame.draw.rect (seasonSection, CC.DARK_GREEN, seasonSection.get_rect (), 1)

def drawStreamSection ():
    drawUtil.drawCentered (textUtil.renderLines (['Streams:', str (GGS.streams)], True), streamSection)
    pygame.draw.rect (streamSection, CC.DARK_GREEN, streamSection.get_rect (), 1)

def drawSubscriberSection ():
    drawUtil.drawCentered (textUtil.renderLines (['Abonnenten:', str (GGS.subscriber)], True), subscriberSection)
    pygame.draw.rect (subscriberSection, CC.DARK_GREEN, subscriberSection.get_rect (), 1)

def drawViewSection ():
    drawUtil.drawCentered (textUtil.renderLines (['Views:', str (GGS.views)], True), viewSection)
    pygame.draw.rect (viewSection, CC.DARK_GREEN, viewSection.get_rect (), 1)

def drawSections ():
    if episodeSection in activeSections:
        drawEpisodeSection ()
    if seasonSection in activeSections:
        drawSeasonSection ()
    if streamSection in activeSections:
        drawStreamSection ()
    if subscriberSection in activeSections:
        drawSubscriberSection ()
    if viewSection in activeSections:
        drawViewSection ()

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

def handleSubscriberSectionMotion ():
    if GGS.currentMouseArea != subscriberSectionAreaCode:
        GGS.currentMouseArea = subscriberSectionAreaCode
        hintViewController.showText (subscriberSectionHintText)

def handleViewSectionMotion ():
    if GGS.currentMouseArea != viewSectionAreaCode:
        GGS.currentMouseArea = viewSectionAreaCode
        hintViewController.showText (viewSectionHintText)

def handleMotion (event):
    if eventUtil.eventHappenedInRect (event, episodeSectionAbsoluteRect):
        handleEpisodeSectionMotion ()
    elif eventUtil.eventHappenedInRect (event, seasonSectionAbsoluteRect):
        handleSeasonSectionMotion ()
    elif eventUtil.eventHappenedInRect (event, streamSectionAbsoluteRect):
        handleStreamSectionMotion ()
    elif eventUtil.eventHappenedInRect (event, subscriberSectionAbsoluteRect):
        handleSubscriberSectionMotion ()
    elif eventUtil.eventHappenedInRect (event, viewSectionAbsoluteRect):
        handleViewSectionMotion ()
    else:
        handleEmptySectionMotion ()

def initialize ():
    GV.moneyViewAbsoluteRect = pygame.Rect ((0, CD.CLICK_VIEW_SIZE [1] - 1, CD.MONEY_VIEW_SIZE [0], CD.MONEY_VIEW_SIZE [1]))
    GV.moneyView = GV.mainView.subsurface (GV.moneyViewAbsoluteRect)
    initializeEpisodeSection ()
    initializeSeasonSection ()
    initializeStreamSection ()
    initializeSubscriberSection ()
    initializeViewSection ()
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
    streamSectionAbsoluteRect = pygame.Rect (GV.moneyViewAbsoluteRect [0], GV.moneyViewAbsoluteRect [1] + (sectionSize [1] * 2), sectionSize [0], sectionSize [1])
    streamSection = GV.moneyView.subsurface ((0, (sectionSize [1] * 2), sectionSize [0], sectionSize [1]))
    activeSections.append (streamSection)

def initializeSubscriberSection ():
    global activeSections
    global subscriberSectionAbsoluteRect
    global subscriberSection
    subscriberSectionAbsoluteRect = pygame.Rect (GV.moneyViewAbsoluteRect [0], GV.moneyViewAbsoluteRect [1] + (sectionSize [1] * 3), sectionSize [0], sectionSize [1])
    subscriberSection = GV.moneyView.subsurface ((0, (sectionSize [1] * 3), sectionSize [0], sectionSize [1]))
    activeSections.append (subscriberSection)

def initializeViewSection ():
    global activeSections
    global viewSectionAbsoluteRect
    global viewSection
    viewSectionAbsoluteRect = pygame.Rect (GV.moneyViewAbsoluteRect [0], GV.moneyViewAbsoluteRect [1] + (sectionSize [1] * 4), sectionSize [0], sectionSize [1])
    viewSection = GV.moneyView.subsurface ((0, (sectionSize [1] * 4), sectionSize [0], sectionSize [1]))
    activeSections.append (viewSection)

def update ():
    GV.moneyView.fill (CC.BLACK)
    drawSections ()
    pygame.draw.rect (GV.moneyView, CC.DARK_GREEN, (0, 0, CD.MONEY_VIEW_SIZE [0] - 1, CD.MONEY_VIEW_SIZE [1] - 1), 2)
