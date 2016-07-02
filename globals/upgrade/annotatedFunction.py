class AnnotatedFunction:
    def __init__ (self, function, parameter, text = None, textFunction = None):
        self.function = function
        self.parameter = parameter
        self.text = text
        self.textFunction = textFunction

    def execute (self):
        return self.function (self.parameter)

    def getText (self):
        if self.text is not None:
            return self.text
        elif self.textFunction is not None:
            return self.textFunction (self.parameter)
        else:
            return None
