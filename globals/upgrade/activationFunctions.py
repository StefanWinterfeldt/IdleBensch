import globals.gameLogic as GL
import globals.gameState as GS
from globals.upgrade.annotatedFunction import AnnotatedFunction

def activateAutoClicking (params):
    GL.BASE_CLICKS_PER_SECOND = 0.1

def activateStream (param):
    GS.streams = 1

def increaseEpisodesPerClickByPercentage (percentage):
    GL.BASE_EPISODES_PER_CLICK *= ((100 + percentage) / 100.0)

def increaseMaxSubscribersPerEpisode (value):
    GL.BASE_MAX_SUBSCRIBERS_PER_EPISODE += value

def getActivateAutoClickFunction ():
    return AnnotatedFunction (
        text = 'Du beginnst automatisch zu klicken.',
        function = activateAutoClicking,
        parameter = None
    )

def getActivateStreamFunction ():
    return AnnotatedFunction (
        text = 'Schaltet deinen ersten Stream live.',
        function = activateStream,
        parameter = None
    )

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