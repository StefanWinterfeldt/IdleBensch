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

def getColorValueFromGradient (value1, value2, percentage):
    return max (0, min (255, (value1 + ((value2 - value1) * percentage))))

def getColorFromGradient (color1, color2, percentage):
    redValue = getColorValueFromGradient (color1 [0], color2 [0], percentage)
    greenValue = getColorValueFromGradient (color1 [1], color2 [1], percentage)
    blueValue = getColorValueFromGradient (color1 [2], color2 [2], percentage)
    return redValue, greenValue, blueValue

def invertColor (color):
    return abs (color [0] - 255), abs (color [1] - 255), abs (color [2] - 255)
