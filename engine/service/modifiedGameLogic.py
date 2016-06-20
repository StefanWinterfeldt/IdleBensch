import constants.gameLogic as CGL
import globals.gameState as GGS

def getEpisodesPerClick ():
    return CGL.BASE_EPISODES_PER_CLICK

def getEpisodesPerSeason ():
    return CGL.BASE_EPISODES_PER_SEASON

def getMinSubscribersPerEpisode ():
    return CGL.BASE_MIN_SUBSCRIBERS_PER_EPISODE

def getMaxSubscribersPerEpisode ():
    return CGL.BASE_MAX_SUBSCRIBERS_PER_EPISODE

def getMinSubscribersPerSeason ():
    return CGL.BASE_MIN_SUBSCRIBERS_PER_SEASON

def getMaxSubscribersPerSeason ():
    return CGL.BASE_MAX_SUBSCRIBERS_PER_SEASON

def getMoneyPerView ():
    return CGL.BASE_MONEY_PER_VIEW

def getSubscriberViewsPerEpisode ():
    return CGL.BASE_SUBSCRIBER_VIEWS_PER_EPISODE

def getTicksToProcessEpisode ():
    return CGL.BASE_TICKS_TO_PROCESS_EPISODE

def getTicksToProcessSeason ():
    return CGL.BASE_TICKS_TO_PROCESS_SEASON

def getViewsPerEpisode ():
    return CGL.BASE_VIEWS_PER_EPISODE + (GGS.subscriber * getSubscriberViewsPerEpisode ())
