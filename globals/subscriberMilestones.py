from engine.controller.achievementObjects.subscriberMilestone import SubscriberMilestone


sortedMilestones = []
sortedMilestones.append (SubscriberMilestone ('TEST1', 10))
sortedMilestones.append (SubscriberMilestone ('TEST2', 30))
sortedMilestones.sort (key = lambda x: x.subscribersNeeded)

def getNextMilestone (milestone):
    nextMilestone = None
    for i in range (len (sortedMilestones)):
        if sortedMilestones [i].subscribersNeeded == milestone.subscribersNeeded and i < len (sortedMilestones) - 1:
            nextMilestone = sortedMilestones [i + 1]
            break
    return nextMilestone
