import globals.gameLogic as GL
import globals.gameState as GS
from globals.upgrade.annotatedFunction import AnnotatedFunction
import importlib

def activateAutoClicking (params):
    GL.BASE_CLICKS_PER_SECOND = 1.0

def activateComputerCategory (params):
    CH = importlib.import_module('globals.upgrade.categoryHeaders')
    CU = importlib.import_module('globals.upgrade.computerUpgrades')
    CH.computerHeader.visible = True
    CU.schulPC.visible = True

def activateMerchCategory (params):
    CH = importlib.import_module('globals.upgrade.categoryHeaders')
    MU = importlib.import_module('globals.upgrade.merchUpgrades')
    CH.merchHeader.visible = True
    MU.shirt.visible = True

def activateOccultCategory (params):
    CH = importlib.import_module ('globals.upgrade.categoryHeaders')
    OU = importlib.import_module ('globals.upgrade.occultUpgrades')
    CH.occultHeader.visible = True
    OU.zombiePact.visible = True

def activateTechCategory (params):
    CH = importlib.import_module ('globals.upgrade.categoryHeaders')
    TU = importlib.import_module ('globals.upgrade.techUpgrades')
    CH.techHeader.visible = True
    TU.kaffeeMaschine.visible = True

def activateStream (param):
    GS.streams = 1
    GL.BASE_SUBSCRIBERS_PER_STREAM_PER_SECOND = 0.05

def increaseClicksPerSecondByPercentage (percentage):
    GL.BASE_CLICKS_PER_SECOND *= ((100 + percentage) / 100.0)

def increaseEpisodesPerClickByPercentage (percentage):
    GL.BASE_EPISODES_PER_CLICK *= ((100 + percentage) / 100.0)

def increaseMaxSubscribersPerEpisode (value):
    GL.BASE_MAX_SUBSCRIBERS_PER_EPISODE += value

def increaseMinSubscribersPerEpisode (value):
    GL.BASE_MIN_SUBSCRIBERS_PER_EPISODE += value

def increaseNumberOfStreams (value):
    GS.streams += value

def increaseViewsPerEpisodeByPercentage (percentage):
    GL.BASE_VIEWS_PER_EPISODE *= ((100 + percentage) / 100.0)

def increaseSubscribersPerStreamPerSecondByPercentage (percentage):
    GL.BASE_SUBSCRIBERS_PER_STREAM_PER_SECOND *= ((100 + percentage) / 100.0)

def increaseSubscriberViewsPerEpisodeByPercentage (percentage):
    GL.BASE_SUBSCRIBER_VIEWS_PER_EPISODE *= ((100 + percentage) / 100.0)

def getActivateAutoClickFunction ():
    return AnnotatedFunction (
        text = 'Du beginnst automatisch zu klicken.',
        function = activateAutoClicking,
        parameter = None
    )

def getActivateComputerCategory ():
    return AnnotatedFunction (
        text = 'Da deine grundlegende Koffein-Versorgung sicher gestellt ist kannst du dich jetzt um deinen PC kuemmern. Aktiviert Computer Upgrades.',
        function = activateComputerCategory,
        parameter = None
    )

def getActivateMerchCategory ():
    return AnnotatedFunction (
        text = 'Der Rechner ist schnell genug um einen Web-Shop zu erstellen. Aktiviert Merchandise Upgrades.',
        function = activateMerchCategory,
        parameter = None
    )

def getActivateOccultCategory ():
    return AnnotatedFunction (
        text = 'Aktiviert ausserweltliche Upgrades.',
        function = activateOccultCategory,
        parameter = None
    )

def getActivateTechCategory ():
    return AnnotatedFunction (
        text = 'Der Rechner ist schnell genug um damit zu forschen. Aktiviert Technologie Upgrades.',
        function = activateTechCategory,
        parameter = None
    )

def getActivateStreamFunction ():
    return AnnotatedFunction (
        text = 'Schaltet deinen ersten Stream live.',
        function = activateStream,
        parameter = None
    )

def getIncreaseClicksPerSecondByPercentageFunction (percentage):
    return AnnotatedFunction (
        text = 'Du klickst ' + str (percentage) + '% oefter automatisch',
        function = increaseClicksPerSecondByPercentage,
        parameter = percentage
    )

def getIncreaseEpisodesPerClickByPercentageFunction (percentage):
    return AnnotatedFunction (
        text = 'Du produzierst ' + str (percentage) + '% mehr Folgen pro Klick.',
        function = increaseEpisodesPerClickByPercentage,
        parameter = percentage
    )

def getIncreaseMaxSubscribersPerEpisode (value):
    return AnnotatedFunction (
        text = 'Die maximale Anzahl an Abonnenten pro Folge erhoeht sich um ' + str (value),
        function = increaseMaxSubscribersPerEpisode,
        parameter = value
    )

def getIncreaseMinSubscribersPerEpisode (value):
    return AnnotatedFunction (
        text = 'Die minimale Anzahl an Abonnenten pro Folge erhoeht sich um ' + str (value),
        function = increaseMinSubscribersPerEpisode,
        parameter = value
    )

def getIncreaseNumberOfStreamsByOne ():
    return AnnotatedFunction (
        text = 'Du erhaeltst einen zusaetzlichen Stream.',
        function = increaseNumberOfStreams,
        parameter = 1
    )

def getIncreaseViewsPerEpisodeByPercentage (percentage):
    return AnnotatedFunction (
        text = 'Du erhaeltst ' + str (percentage) + '% mehr Views pro Folge.',
        function = increaseViewsPerEpisodeByPercentage,
        parameter = percentage
    )

def getIncreaseSubscribersPerStreamPerSecondByPercentage (percentage):
    return AnnotatedFunction (
        text = 'Du erhaeltst ' + str (percentage) + '% mehr Abonnenten pro Stream pro Sekunde.',
        function = increaseSubscribersPerStreamPerSecondByPercentage,
        parameter = percentage
    )

def getIncreaseSubscriberViewsPerEpisodeByPercentage (percentage):
    return AnnotatedFunction (
        text = 'Du erhaeltst ' + str (percentage) + '% mehr Views pro Folge von deinen Abonnenten.',
        function = increaseViewsPerEpisodeByPercentage,
        parameter = percentage
    )

def getPassiveFunction (text):
    return AnnotatedFunction (
        text = text,
        function = lambda x: None,
        parameter = None
    )
