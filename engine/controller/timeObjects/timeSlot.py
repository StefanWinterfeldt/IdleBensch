class TimeSlot:
    def __init__(self):
        self.actions = []

    def addAction (self, action):
        self.actions.append (action)

    def executeActions (self):
        for action in self.actions:
            action.execute ()