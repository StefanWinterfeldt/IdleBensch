import engine.view.clickView as clickView
import globals.view as globalViews

def dispatchToView (event):
    if globalViews.clickView.get_rect ().collidepoint (event.pos):
        clickView.handleClick (event.pos)

def handleMouseEvent (event):
    dispatchToView (event)
