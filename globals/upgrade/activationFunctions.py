import globals.gameLogic as GL
import globals.gameState as GS
from globals.upgrade.annotatedFunction import AnnotatedFunction
import importlib

def activateAutoClicking (params):
    GL.BASE_CLICKS_PER_SECOND = 1.0

def activateComputerCategory (params):
    CH = importlib.import_module ('globals.upgrade.categoryHeaders')
    CU = importlib.import_module ('globals.upgrade.computerUpgrades')
    CH.computerHeader.visible = True
    CU.schulPC.visible = True

def activateMerchCategory (params):
    CH = importlib.import_module ('globals.upgrade.categoryHeaders')
    MU = importlib.import_module ('globals.upgrade.merchUpgrades')
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

def activateDonations (params):
    GL.BASE_DONATION_CHANCE_PER_STREAM_PER_SECOND = 0.01
    GL.BASE_MIN_DONATION = 1.0
    GL.BASE_MAX_DONATION = 2.0

def activatePurchases (params):
    GL.BASE_PURCHASE_CHANCE_PER_SUBSCRIBER_PER_SECOND = 0.0001
    GL.BASE_MIN_PURCHASE = 0.50
    GL.BASE_MAX_PURCHASE = 5.0

def activateStream (param):
    GS.streams = 1
    GL.BASE_SUBSCRIBERS_PER_STREAM_PER_SECOND = 0.05

def increaseClicksPerSecondByPercentage (percentage):
    GL.BASE_CLICKS_PER_SECOND *= ((100 + percentage) / 100.0)

def increaseEpisodesPerClickByPercentage (percentage):
    GL.BASE_EPISODES_PER_CLICK *= ((100 + percentage) / 100.0)

def increaseMaxPurchaseAmountByPercentage (percentage):
    GL.BASE_MAX_PURCHASE *= ((100 + percentage) / 100.0)

def increaseMaxDonationByValue (value):
    GL.BASE_MAX_DONATION += value

def increaseMaxSubscribersPerEpisode (value):
    GL.BASE_MAX_SUBSCRIBERS_PER_EPISODE += value

def increaseMinSubscribersPerEpisode (value):
    GL.BASE_MIN_SUBSCRIBERS_PER_EPISODE += value

def increaseNumberOfStreams (value):
    GS.streams += value

def increaseDonationChanceByPercentage (percentage):
    GL.BASE_DONATION_CHANCE_PER_STREAM_PER_SECOND *= ((100 + percentage) / 100.0)

def increasePurchaseChanceByPercentage (percentage):
    GL.BASE_PURCHASE_CHANCE_PER_SUBSCRIBER_PER_SECOND *= ((100 + percentage) / 100.0)

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

def getActivateDonationsFunction ():
    return AnnotatedFunction (
        text = 'Abonnenten koennen dir jetzt im Stream direkt Geld spenden.',
        function = activateDonations,
        parameter = None
    )

def getActivatePurchasesFunction ():
    return AnnotatedFunction (
        text = 'Abonnenten koennen jetzt bei dir einkaufen.',
        function = activatePurchases,
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

def getIncreaseMaxDonationAmount (value):
    return AnnotatedFunction (
        text = 'Erhoeht die maximale Spendengroesse um ' + str(value) + ' Euro.',
        function = increaseMaxDonationByValue,
        parameter = value
    )

def getIncreaseMaxPurchaseAmountByPercentage (percentage):
    return AnnotatedFunction (
        text = 'Erhoeht den maximalen Merchandise Einkaufswert um ' + str (percentage) + '%.',
        function = increaseMaxPurchaseAmountByPercentage,
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

def getIncreaseDonationChanceByPercentage (percentage):
    return AnnotatedFunction (
        text = 'Die Chance, dass dir beim Streamen Geld gespendet wird steigt um ' + str(percentage) + '%.',
        function = increaseDonationChanceByPercentage,
        parameter = percentage
    )

def getIncreasePurchaseChanceByPercentage (percentage):
    return AnnotatedFunction (
        text = 'Die Chance, dass Abonnenten etwas bei dir kaufen steigt um ' + str(percentage) + '%.',
        function = increasePurchaseChanceByPercentage,
        parameter = percentage
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
