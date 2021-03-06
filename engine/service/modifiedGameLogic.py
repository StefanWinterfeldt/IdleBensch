#Copyright 2016 Stefan Winterfeldt
#This file is part of Idle Bensch.
#
#Idle Bensch is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#Idle Bensch is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with Idle Bensch.  If not, see <http://www.gnu.org/licenses/>.

import constants.display as CD
import globals.gameLogic as CGL
import globals.gameState as GGS

def getClicksPerSecond ():
    return CGL.BASE_CLICKS_PER_SECOND

def getClicksPerTick ():
    return CGL.BASE_CLICKS_PER_SECOND / float (CD.FRAME_RATE)

def getDonationChancePerStreamPerSecondInPercent ():
    return CGL.BASE_DONATION_CHANCE_PER_STREAM_PER_SECOND * 100

def getDonationChancePerStreamPerSecond ():
    return CGL.BASE_DONATION_CHANCE_PER_STREAM_PER_SECOND

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

def getPurchaseChancePerSubscriberPerSecondInPercent ():
    return CGL.BASE_PURCHASE_CHANCE_PER_SUBSCRIBER_PER_SECOND * 100.0

def getPurchaseChancePerSubscriberPerSecond ():
    return CGL.BASE_PURCHASE_CHANCE_PER_SUBSCRIBER_PER_SECOND

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
