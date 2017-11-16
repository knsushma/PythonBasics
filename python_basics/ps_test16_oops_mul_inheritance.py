class Alpha:
    def __init__(self):
        print("I am Alpha")
    def pprint(self):
        print("Alpha")

class Beta:
    def __init__(self):
        print("I am Beta")
    def pprint(self):
        print("Beta")

class Gamma(Alpha,Beta):
    def __init__(self):
        super().__init__()
        super().pprint()

Gamma() # prints Alpha -> order of inheritance matter