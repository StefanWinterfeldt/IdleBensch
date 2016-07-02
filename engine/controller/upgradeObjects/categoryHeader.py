import pygame

class CategoryHeader:

    absoluteRect = None
    areaCode = None
    relativeRect = None

    def __init__(self, imagePath, hintText, visible = False):
        self.image = pygame.image.load (imagePath)
        self.hintText = hintText
        self.visible = visible

    def getHintText (self):
        return self.hintText