def getColorValueFromGradient (value1, value2, percentage):
    return max (0, min (255, (value1 + ((value2 - value1) * percentage))))

def getColorFromGradient (color1, color2, percentage):
    redValue = getColorValueFromGradient (color1 [0], color2 [0], percentage)
    greenValue = getColorValueFromGradient (color1 [1], color2 [1], percentage)
    blueValue = getColorValueFromGradient (color1 [2], color2 [2], percentage)
    return redValue, greenValue, blueValue

def invertColor (color):
    return abs (color [0] - 255), abs (color [1] - 255), abs (color [2] - 255)
