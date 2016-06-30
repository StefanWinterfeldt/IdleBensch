import constants.display as CD
import globals.gameLogic as CGL
import globals.gameState as GGS

def getClicksPerSecond ():
    return CGL.BASE_CLICKS_PER_SECOND

def getClicksPerTick ():
    return CGL.BASE_CLICKS_PER_SECOND / float (CD.FRAME_RATE)

def getDonationChancePerStreamPerSecondInPercent ():
    return CGL.BASE_DONATION_CHANCE_PER_STREAM_PER_SECOND * 100

def getDonationChancePerStreamPerTick ():
    return CGL.BASE_DONATION_CHANCE_PER_STREAM_PER_SECOND / float (CD.FRAME_RATE)

def getEpisodesPerClick ():
    return CGL.BASE_EPISODES_PER_CLICK

def getEpisodesPerSeason ():
    return CGL.BASE_EPISODES_PER_SEASON

def getMinDonation ():
    return CGL.BASE_MIN_DONATION

def getMinPurchase ():
    return CGL.BASE_MIN_PURCHASE

def getMinSubscribersPerEpisode ():
    return CGL.BASE_MIN_SUBSCRIBERS_PER_EPISODE

def getMaxDonation ():
    return CGL.BASE_MAX_DONATION

def getMaxPurchase ():
    return CGL.BASE_MAX_PURCHASE

def getMaxSubscribersPerEpisode ():
    return CGL.BASE_MAX_SUBSCRIBERS_PER_EPISODE

def getMinSubscribersPerSeason ():
    return CGL.BASE_MIN_SUBSCRIBERS_PER_SEASON

def getMaxSubscribersPerSeason ():
    return CGL.BASE_MAX_SUBSCRIBERS_PER_SEASON

def getMoneyPerView ():
    return CGL.BASE_MONEY_PER_VIEW

def getPurchaseChancePerSubscriberPerTick ():
    return CGL.BASE_PURCHASE_CHANCE_PER_SUBSCRIBER_PER_SECOND / float (CD.FRAME_RATE)

def getSubscribersPerSecond ():
    return GGS.streams * CGL.BASE_SUBSCRIBERS_PER_STREAM_PER_SECOND

def getSubscribersPerTick ():
    return GGS.streams * CGL.BASE_SUBSCRIBERS_PER_STREAM_PER_SECOND / float (CD.FRAME_RATE)

def getSubscriberViewsPerEpisode ():
    return CGL.BASE_SUBSCRIBER_VIEWS_PER_EPISODE

def getSecondsToProcessEpisode ():
    return CGL.BASE_SECONDS_TO_PROCESS_EPISODE

def getSecondsToProcessSeason ():
    return CGL.BASE_SECONDS_TO_PROCESS_SEASON

def getTicksToProcessEpisode ():
    return int (CGL.BASE_SECONDS_TO_PROCESS_EPISODE * float (CD.FRAME_RATE))

def getTicksToProcessSeason ():
    return int (CGL.BASE_SECONDS_TO_PROCESS_SEASON * float (CD.FRAME_RATE))

def getViewsPerEpisode ():
    return CGL.BASE_VIEWS_PER_EPISODE + (GGS.subscriber * getSubscriberViewsPerEpisode ())
