class Coffee:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")

        if len(value) < 3:
            raise ValueError("Name must be at least 3 characters long")
        self._name = value


coffee = Coffee("Espresso")
print(coffee.name)