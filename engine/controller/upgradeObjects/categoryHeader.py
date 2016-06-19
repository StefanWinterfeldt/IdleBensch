import pygame

class CategoryHeader:

    absoluteRect = None
    areaCode = None
    relativeRect = None
    visible = True

    def __init__(self, imagePath, hintText):
        self.image = pygame.image.load (imagePath)
        self.hintText = hintText
