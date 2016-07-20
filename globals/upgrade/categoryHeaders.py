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

from engine.controller.upgradeObjects.categoryHeader import CategoryHeader
import os


benschHeader = CategoryHeader (
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'bensch', 'benschHeader.png'),
    hintText = 'Selbstverbesserung durch Konsum! Das sind die Bensch Upgrades.',
    visible = True
)

computerHeader = CategoryHeader (
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'computer', 'computerHeader.png'),
    hintText = 'Stecke Geld in deinen Computer - es wird ihn schneller machen!'
)

merchHeader = CategoryHeader (
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'merch', 'merchHeader.png'),
    hintText = 'Merchandise! Kauf meinen Scheiss!'
)

occultHeader = CategoryHeader (
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'occult', 'occultHeader.png'),
    hintText = 'Das Okkulte - schliesse Vertraege mit den Wesen der Unterwelt und erweitere deine Fanbase.'
)

techHeader = CategoryHeader (
    imagePath = os.path.join ('resources', 'ingame', 'upgrade', 'tech', 'techHeader.png'),
    hintText = 'Der grosse Spass fuer Langweiler! Bauen Sie sich ihr eigenes Vogelhaeuschen!'
)
