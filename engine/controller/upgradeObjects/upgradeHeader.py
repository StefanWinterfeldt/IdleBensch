import pygame

class UpgradeHeader:
    def __init__(self, imagePath, absoluteRect, hintText):
        self.image = pygame.image.load (imagePath)
        self.absoluteRect = absoluteRect
        self.hintText = hintText