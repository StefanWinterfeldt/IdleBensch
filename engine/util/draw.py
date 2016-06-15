def calculateXOffset (source, dest):
    return (dest.get_width () / 2) - (source.get_width () / 2)

def calculateYOffset (source, dest):
    return (dest.get_height () / 2) - (source.get_height () / 2)

def drawCentered (source, dest):
    xOffset = calculateXOffset (source, dest)
    yOffset = calculateYOffset (source, dest)
    dest.blit (source, (xOffset, yOffset))

def drawXCentered (source, dest, y):
    xOffset = calculateXOffset (source, dest)
    dest.blit (source, (xOffset, y))
