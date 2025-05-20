class Coffee:
    all = []
    
    def __init__(self, name):
        self.name = name
        Coffee.all.append(self)
    
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if len(name) < 3:
            raise ValueError("Name must be at least 3 characters long")
        if hasattr(self, '_name'):
            raise AttributeError("Coffee name cannot be changed after initialization")
        self._name = name

    
