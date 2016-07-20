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