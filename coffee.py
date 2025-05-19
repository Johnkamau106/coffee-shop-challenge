class Coffee:
    all = []
    
    def __init__(self, name):
        self.name = name
        Coffee.all.append(self)
