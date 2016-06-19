import pygame

class UpgradeHeader:

    absoluteRect = None
    relativeRect = None
    areaCode = None

    def __init__(self, imagePath, hintText):
        self.image = pygame.image.load (imagePath)
        self.hintText = hintText
