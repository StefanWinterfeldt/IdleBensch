import engine.controller.clickViewController as clickViewController
import globals.view as globalViews

def dispatchToView (event):
    if globalViews.clickView.get_rect ().collidepoint (event.pos):
        clickViewController.handleClick (event.pos)

def handleMouseEvent (event):
    dispatchToView (event)
