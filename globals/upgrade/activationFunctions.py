import globals.gameLogic as CGL
from globals.upgrade.annotatedFunction import AnnotatedFunction

def increaseEpisodesPerClickByPercentage (percentage):
    CGL.BASE_EPISODES_PER_CLICK *= ((100 + percentage) / 100.0)

def getIncreaseEpisodesPerClickByPercentageFunction (percentage):
    return AnnotatedFunction (
        text = 'Du produzierst ' + str(percentage) + '% mehr Folgen pro Klick.',
        function = increaseEpisodesPerClickByPercentage,
        parameter = percentage
    )