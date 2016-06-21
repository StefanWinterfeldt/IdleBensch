from globals.upgrade.annotatedFunction import AnnotatedFunction

def getAlwaysUnlockedFunction ():
    return AnnotatedFunction (
        text = None,
        function = lambda x: True,
        parameter = None
    )
