import constants.gameLogic as CGL
import globals.gameState as GGS

def getViewsPerEpisode ():
    return CGL.BASE_VIEWS_PER_EPISODE + (GGS.subscriber * CGL.BASE_SUBSCRIBER_VIEWS_PER_EPISODE)