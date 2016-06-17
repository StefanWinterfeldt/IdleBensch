def eventHappenedInRect (event, rect):
    return rect.collidepoint (event.pos)