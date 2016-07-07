import globals.gameState as GS

class Message:
    def __init__(self, minViews, maxViews, text):
        self.minViews = minViews
        self.maxViews = maxViews
        self.text = text

    def isAvailable (self):
        if self.minViews is None and self.maxViews is None:
            return True
        elif self.minViews is None:
            return GS.views <= self.maxViews
        elif self.maxViews is None:
            return GS.views >= self.minViews
        else:
            return self.minViews <= GS.views <= self.maxViews