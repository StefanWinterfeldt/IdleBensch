import constants.color as color
import globals.view as view

def initialize ():
    view.clickView = view.mainView.subsurface ((1559, 0, 360, 360))
    view.clickView.fill (color.RED)

def update ():
    pass