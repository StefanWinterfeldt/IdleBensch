import constants.color as CC
import constants.display as CD
import engine.controller.hintViewController as hintViewController
import engine.service.modifiedGameLogic as MGL
import engine.util.draw as drawUtil
import engine.util.event as eventUtil
import engine.util.text as textUtil
import globals.gameState as GGS
import globals.view as GV
import pygame


episodeSection = None
episodeSectionAbsoluteRect = None
episodeSectionAreaCode = 'MVES'
episodeSectionHintText = 'Folgen produzieren Views und Abonnenten.'
moneySection = None
moneySectionAbsoluteRect = None
moneySectionAreaCode = 'MVMS'
moneySectionHintText = 'Geld!Geld!Geld!Geld!Geld!Geld! -Mr. Krabs'
seasonSection = None
seasonSectionAbsoluteRect = None
seasonSectionAreaCode = 'MVSS'
seasonSectionHintText = 'Staffeln produzieren mehr Abonnenten.'
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

def drawMoneySection ():
    drawUtil.drawCentered (textUtil.renderLines (['Euro:', textUtil.convertToHumanReadableString (GGS.money, True)], True), moneySection)
    pygame.draw.rect (moneySection, CC.DARK_GREEN, moneySection.get_rect (), 1)

def drawSeasonSection ():
    drawUtil.drawCentered (textUtil.renderLines (['Staffeln:', str (GGS.seasons)], True), seasonSection)
    pygame.draw.rect (seasonSection, CC.DARK_GREEN, seasonSection.get_rect (), 1)

def drawStreamSection ():
    drawUtil.drawCentered (textUtil.renderLines (['Streams:', str (GGS.streams)], True), streamSection)
    pygame.draw.rect (streamSection, CC.DARK_GREEN, streamSection.get_rect (), 1)

def drawSubscriberSection ():
    drawUtil.drawCentered (textUtil.renderLines (['Abonnenten:', textUtil.convertToHumanReadableString (GGS.subscriber)], True), subscriberSection)
    pygame.draw.rect (subscriberSection, CC.DARK_GREEN, subscriberSection.get_rect (), 1)

def drawViewSection ():
    drawUtil.drawCentered (textUtil.renderLines (['Views:', textUtil.convertToHumanReadableString (GGS.views)], True), viewSection)
    pygame.draw.rect (viewSection, CC.DARK_GREEN, viewSection.get_rect (), 1)

def drawSections ():
    drawEpisodeSection ()
    drawSeasonSection ()
    drawStreamSection ()
    drawSubscriberSection ()
    drawViewSection ()
    drawMoneySection ()

def getVariableEpisodeHintText ():
    minSubs = textUtil.convertToHumanReadableString (MGL.getMinSubscribersPerEpisode ())
    maxSubs = textUtil.convertToHumanReadableString (MGL.getMaxSubscribersPerEpisode ())
    views = textUtil.convertToHumanReadableString (MGL.getViewsPerEpisode ())
    seconds = textUtil.convertToHumanReadableString (MGL.getSecondsToProcessEpisode ())
    return 'Momentan produziert eine Folge ' + views + ' Views und ' + minSubs + ' bis ' + maxSubs + ' Abonnenten ueber ' + seconds + ' Sekunden.'

def getVariableSeasonHintText ():
    minSubs = textUtil.convertToHumanReadableString (MGL.getMinSubscribersPerSeason ())
    maxSubs = textUtil.convertToHumanReadableString (MGL.getMaxSubscribersPerSeason ())
    seconds = textUtil.convertToHumanReadableString (MGL.getSecondsToProcessSeason ())
    return 'Momentan produziert eine Staffel ' + minSubs + ' bis ' + maxSubs + ' Abonnenten ueber ' + seconds + ' Sekunden.'

def getVariableStreamHintText ():
    subsPerSec = textUtil.convertToHumanReadableString (MGL.getSubscribersPerSecond (), True)
    donChancePerSec = textUtil.convertToHumanReadableString (MGL.getDonationChancePerStreamPerSecondInPercent (), True)
    minDon = textUtil.convertToHumanReadableString (MGL.getMinDonation (), True)
    maxDon = textUtil.convertToHumanReadableString (MGL.getMaxDonation (), True)
    return 'Momentan produzieren deine Streams zusammen ' + subsPerSec + ' Abonnenten pro Sekunde. Jeder Stream hat jede Sekunde eine ' + donChancePerSec + '% Chance eine Spende von ' + minDon + ' bis ' + maxDon + ' Euro zu erzeugen.'

def getVariableSubscriberHintText ():
    views = textUtil.convertToHumanReadableString (MGL.getSubscriberViewsPerEpisode (), True)
    purChancePerSec = textUtil.convertToHumanReadableString (MGL.getPurchaseChancePerSubscriberPerSecondInPercent (), True)
    minPur = textUtil.convertToHumanReadableString (MGL.getMinPurchase (), True)
    maxPur = textUtil.convertToHumanReadableString (MGL.getMaxPurchase (), True)
    return 'Momentan liefert jeder Abonnent ' + views + ' extra Views pro Folge. Jeder Abonnent hat jede Sekunde eine ' + purChancePerSec + '% Chance fuer ' + minPur + ' bis ' + maxPur + ' Euro Merchandise zu kaufen.'

def getVariableViewHintText ():
    money = textUtil.convertToHumanReadableString (MGL.getMoneyPerView (), True)
    return 'Momentan produziert jeder View ' + money + ' Euro.'

def handleEmptySectionMotion ():
    if GGS.currentMouseArea is not None:
        GGS.currentMouseArea = None
        hintViewController.clearText ()

def handleEpisodeSectionMotion ():
    if GGS.currentMouseArea != episodeSectionAreaCode:
        GGS.currentMouseArea = episodeSectionAreaCode
        hintViewController.showText (' '.join ([episodeSectionHintText, getVariableEpisodeHintText ()]))

def handleMoneySectionMotion ():
    if GGS.currentMouseArea != moneySectionAreaCode:
        GGS.currentMouseArea = moneySectionAreaCode
        hintViewController.showText (moneySectionHintText)

def handleSeasonSectionMotion ():
    if GGS.currentMouseArea != seasonSectionAreaCode:
        GGS.currentMouseArea = seasonSectionAreaCode
        hintViewController.showText (' '.join ([seasonSectionHintText, getVariableSeasonHintText ()]))

def handleStreamSectionMotion ():
    if GGS.currentMouseArea != streamSectionAreaCode:
        GGS.currentMouseArea = streamSectionAreaCode
        hintViewController.showText (' '.join ([streamSectionHintText, getVariableStreamHintText ()]))

def handleSubscriberSectionMotion ():
    if GGS.currentMouseArea != subscriberSectionAreaCode:
        GGS.currentMouseArea = subscriberSectionAreaCode
        hintViewController.showText (' '.join ([subscriberSectionHintText, getVariableSubscriberHintText ()]))

def handleViewSectionMotion ():
    if GGS.currentMouseArea != viewSectionAreaCode:
        GGS.currentMouseArea = viewSectionAreaCode
        hintViewController.showText (' '.join ([viewSectionHintText, getVariableViewHintText ()]))

def handleMotion (event):
    if eventUtil.eventHappenedInRect (event, episodeSectionAbsoluteRect):
        handleEpisodeSectionMotion ()
    elif eventUtil.eventHappenedInRect (event, moneySectionAbsoluteRect):
        handleMoneySectionMotion ()
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
    GV.moneyView = GV.gameView.subsurface (GV.moneyViewAbsoluteRect)
    initializeEpisodeSection ()
    initializeSeasonSection ()
    initializeStreamSection ()
    initializeSubscriberSection ()
    initializeViewSection ()
    initializeMoneySection ()
    pygame.draw.rect (GV.moneyView, CC.DARK_GREEN, (0, 0, CD.MONEY_VIEW_SIZE [0] - 1, CD.MONEY_VIEW_SIZE [1] - 1), 2)

def initializeEpisodeSection ():
    global episodeSectionAbsoluteRect
    global episodeSection
    episodeSectionAbsoluteRect = pygame.Rect (GV.moneyViewAbsoluteRect [0], GV.moneyViewAbsoluteRect [1], sectionSize [0], sectionSize [1])
    episodeSection = GV.moneyView.subsurface ((0, 0, sectionSize [0], sectionSize [1]))

def initializeSeasonSection ():
    global seasonSectionAbsoluteRect
    global seasonSection
    seasonSectionAbsoluteRect = pygame.Rect (GV.moneyViewAbsoluteRect [0], GV.moneyViewAbsoluteRect [1] + sectionSize [1], sectionSize [0], sectionSize [1])
    seasonSection = GV.moneyView.subsurface ((0, sectionSize [1], sectionSize [0], sectionSize [1]))

def initializeStreamSection ():
    global streamSectionAbsoluteRect
    global streamSection
    streamSectionAbsoluteRect = pygame.Rect (GV.moneyViewAbsoluteRect [0], GV.moneyViewAbsoluteRect [1] + (sectionSize [1] * 2), sectionSize [0], sectionSize [1])
    streamSection = GV.moneyView.subsurface ((0, (sectionSize [1] * 2), sectionSize [0], sectionSize [1]))

def initializeSubscriberSection ():
    global subscriberSectionAbsoluteRect
    global subscriberSection
    subscriberSectionAbsoluteRect = pygame.Rect (GV.moneyViewAbsoluteRect [0], GV.moneyViewAbsoluteRect [1] + (sectionSize [1] * 3), sectionSize [0], sectionSize [1])
    subscriberSection = GV.moneyView.subsurface ((0, (sectionSize [1] * 3), sectionSize [0], sectionSize [1]))

def initializeViewSection ():
    global viewSectionAbsoluteRect
    global viewSection
    viewSectionAbsoluteRect = pygame.Rect (GV.moneyViewAbsoluteRect [0], GV.moneyViewAbsoluteRect [1] + (sectionSize [1] * 4), sectionSize [0], sectionSize [1])
    viewSection = GV.moneyView.subsurface ((0, (sectionSize [1] * 4), sectionSize [0], sectionSize [1]))

def initializeMoneySection ():
    global moneySectionAbsoluteRect
    global moneySection
    moneySectionAbsoluteRect = pygame.Rect (GV.moneyViewAbsoluteRect [0], GV.moneyViewAbsoluteRect [1] + (sectionSize [1] * 5), sectionSize [0], sectionSize [1])
    moneySection = GV.moneyView.subsurface ((0, (sectionSize [1] * 5), sectionSize [0], sectionSize [1]))

def update ():
    GV.moneyView.fill (CC.BLACK)
    drawSections ()
    pygame.draw.rect (GV.moneyView, CC.DARK_GREEN, (0, 0, CD.MONEY_VIEW_SIZE [0] - 1, CD.MONEY_VIEW_SIZE [1] - 1), 2)
