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

from engine.controller.achievementObjects.subscriberMilestone import SubscriberMilestone


sortedMilestones = []
sortedMilestones.append (SubscriberMilestone ('Deine Mudda', 10))
sortedMilestones.append (SubscriberMilestone ('WTFKrake', 50))
sortedMilestones.append (SubscriberMilestone ('LurchiNRW', 200))
sortedMilestones.append (SubscriberMilestone ('Horst vom Bau', 500))
sortedMilestones.append (SubscriberMilestone ('SchneckenhagelLP', 1000))
sortedMilestones.append (SubscriberMilestone ('Haribo Unboxing', 2000))
sortedMilestones.append (SubscriberMilestone ('Dr. Hodenschrot', 3500))
sortedMilestones.append (SubscriberMilestone ('Du selbst', 5600))
sortedMilestones.append (SubscriberMilestone ('K.T. Goodwinters Pastetchen', 8000))
sortedMilestones.append (SubscriberMilestone ('Der Alte', 10000))
sortedMilestones.append (SubscriberMilestone ('XXLPuempel24.de', 25000))
sortedMilestones.append (SubscriberMilestone ('Helloween4545', 48000))
sortedMilestones.append (SubscriberMilestone ('Jordan Underneath', 82000))
sortedMilestones.append (SubscriberMilestone ('m00sician', 121000))
sortedMilestones.append (SubscriberMilestone ('Fynn Kliemann', 200000))
sortedMilestones.append (SubscriberMilestone ('Neo Magazin Royale', 305000))
sortedMilestones.append (SubscriberMilestone ('theclavinover', 450000))
sortedMilestones.append (SubscriberMilestone ('Channel Awesome', 600000))
sortedMilestones.append (SubscriberMilestone ('Space Frogs', 730000))
sortedMilestones.append (SubscriberMilestone ('Boyinaband', 800000))
sortedMilestones.append (SubscriberMilestone ('Franz die Wurst', 1000000))
sortedMilestones.append (SubscriberMilestone ('Chicken Gourmet', 1200000))
sortedMilestones.append (SubscriberMilestone ('Kettensaegen im Weltall', 1500000))
sortedMilestones.append (SubscriberMilestone ('Primitive Technology', 1900000))
sortedMilestones.append (SubscriberMilestone ('Leckt es Ludger?', 2400000))
sortedMilestones.append (SubscriberMilestone ('LeFloid', 2900000))
sortedMilestones.append (SubscriberMilestone ('Apple', 3400000))
sortedMilestones.append (SubscriberMilestone ('Steve-O', 3600000))
sortedMilestones.append (SubscriberMilestone ('Google', 4050000))
sortedMilestones.append (SubscriberMilestone ('Gronkh', 4200000))
sortedMilestones.append (SubscriberMilestone ('PlayStation', 4800000))
sortedMilestones.append (SubscriberMilestone ('Slivki Show', 5200000))
sortedMilestones.append (SubscriberMilestone ('Cinema Sins', 6000000))
sortedMilestones.append (SubscriberMilestone ('Linkin Park', 6400000))
sortedMilestones.append (SubscriberMilestone ('Lady Gaga', 7000000))
sortedMilestones.append (SubscriberMilestone ('IGN', 7500000))
sortedMilestones.append (SubscriberMilestone ('The Slow Mo Guys', 9000000))
sortedMilestones.append (SubscriberMilestone ('Ray William Johnson', 11000000))
sortedMilestones.append (SubscriberMilestone ('Skrillex', 14000000))
sortedMilestones.append (SubscriberMilestone ('Eminem', 19000000))
sortedMilestones.append (SubscriberMilestone ('One Direction', 21000000))
sortedMilestones.append (SubscriberMilestone ('Justin Bieber', 23000000))
sortedMilestones.append (SubscriberMilestone ('PewDiePie', 47000000))
sortedMilestones.append (SubscriberMilestone ('Gabba-Gandalf', 100000000))
sortedMilestones.append (SubscriberMilestone ('Dr. Adolph Engelborg', 200000000))
sortedMilestones.sort (key = lambda x: x.subscribersNeeded)

def getNextMilestone (milestone):
    nextMilestone = None
    for i in range (len (sortedMilestones)):
        if sortedMilestones [i].subscribersNeeded == milestone.subscribersNeeded and i < len (sortedMilestones) - 1:
            nextMilestone = sortedMilestones [i + 1]
            break
    return nextMilestone
