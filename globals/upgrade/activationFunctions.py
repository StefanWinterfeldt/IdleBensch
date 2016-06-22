import globals.gameLogic as CGL
from globals.upgrade.annotatedFunction import AnnotatedFunction

def increaseEpisodesPerClickByPercentage (percentage):
    CGL.BASE_EPISODES_PER_CLICK *= ((100 + percentage) / 100.0)

def increaseMaxSubscribersPerEpisode (value):
    CGL.BASE_MAX_SUBSCRIBERS_PER_EPISODE += value

def getIncreaseEpisodesPerClickByPercentageFunction (percentage):
    return AnnotatedFunction (
        text = 'Du produzierst ' + str(percentage) + '% mehr Folgen pro Klick.',
        function = increaseEpisodesPerClickByPercentage,
        parameter = percentage
    )

def getIncreaseMaxSubscribersPerEpisode (value):
    return AnnotatedFunction (
        text = 'Die maximale Anzahl an Abonnenten pro Folge erhoeht sich um ' + str(value),
        function = increaseMaxSubscribersPerEpisode,
        parameter = value
    )

def getPassiveFunction (text):
    return AnnotatedFunction (
        text = text,
        function = lambda x: None,
        parameter = None
    )