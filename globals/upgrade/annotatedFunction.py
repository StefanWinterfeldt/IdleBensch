class AnnotatedFunction:
    def __init__(self, text, function, parameter):
        self.function = function
        self.parameter = parameter
        self.text = text

    def execute (self):
        return self.function (self.parameter)