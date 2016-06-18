class TimedAction:
    def __init__(self, function, parameter):
        self.function = function
        self.parameter = parameter

    def execute (self):
        self.function (self.parameter)