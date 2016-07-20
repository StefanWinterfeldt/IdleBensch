#Copyright 2016 Stefan Winterfeldt
#This file is part of Idle Bensch.
#
#Idle Bensch is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#Idle Bensch is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with Idle Bensch.  If not, see <http://www.gnu.org/licenses/>.

import engine.util.text as textUtil
import globals.gameState as GGS
import pygame

class Upgrade:
    absoluteRect = None
    active = False
    areaCode = None
    relativeRect = None

    def __init__ (self, id, name, cost, hintText, imagePath, unlockFunction, activationFunction, visible = False):
        self.activationFunction = activationFunction
        self.cost = cost
        self.hintText = hintText
        self.id = id
        self.image = pygame.image.load (imagePath)
        self.name = name
        self.unlockFunction = unlockFunction
        self.visible = visible

    def activate (self):
        GGS.money -= self.cost
        self.active = True
        self.activationFunction.execute ()

    def getHintText (self):
        lines = [self.name, 'Kosten: ' + textUtil.convertToHumanReadableString (self.cost, True)]
        unlockText = self.unlockFunction.getText ()
        if unlockText is not None: lines.append (unlockText)
        lines.append (self.activationFunction.getText ())
        return lines + self.hintText

    def isUnlocked (self):
        return self.unlockFunction.execute ()
