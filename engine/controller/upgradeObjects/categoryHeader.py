import pygame

class CategoryHeader:

    absoluteRect = None
    areaCode = None
    relativeRect = None

    def __init__(self, imagePath, hintText):
        self.image = pygame.image.load (imagePath)
        self.hintText = hintText

    def isVisible (self):
        return True
