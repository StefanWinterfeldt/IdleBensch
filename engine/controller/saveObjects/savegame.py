class SaveGame:
    episodes = None
    money = None
    seasons = None
    streams = None
    subscriber = None
    views = None

    BASE_CLICKS_PER_SECOND = None
    BASE_DONATION_CHANCE_PER_STREAM_PER_SECOND = None
    BASE_PURCHASE_CHANCE_PER_SUBSCRIBER_PER_SECOND = None
    BASE_EPISODES_PER_CLICK = None
    BASE_EPISODES_PER_SEASON = None
    BASE_MAX_DONATION = None
    BASE_MAX_PURCHASE = None
    BASE_MAX_SUBSCRIBERS_PER_EPISODE = None
    BASE_MAX_SUBSCRIBERS_PER_SEASON = None
    BASE_MIN_DONATION = None
    BASE_MIN_PURCHASE = None
    BASE_MIN_SUBSCRIBERS_PER_EPISODE = None
    BASE_MIN_SUBSCRIBERS_PER_SEASON = None
    BASE_MONEY_PER_VIEW = None
    BASE_SUBSCRIBER_VIEWS_PER_EPISODE = None
    BASE_SUBSCRIBERS_PER_STREAM_PER_SECOND = None
    BASE_SECONDS_TO_PROCESS_EPISODE = None
    BASE_SECONDS_TO_PROCESS_SEASON = None
    BASE_VIEWS_PER_EPISODE = None

    activeUpgradeIds = []

    lastFullEpisodes = None
    lastFullSeasons = None
    lastFullViews = None

    timeSlots = []

    ticksSinceLastProcess = 0
    currentAutoClicks = 0
    currentSubscribers = 0

    episodeCompletion = 0
    seasonCompletion = 0

    currentMilestone = None
    lastMilestone = None

    def __init__ (self):
        pass
