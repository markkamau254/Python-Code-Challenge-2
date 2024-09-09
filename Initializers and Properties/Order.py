class Order:
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Price must be a number")

        if not (1.0 <= value <= 10.0):
            raise ValueError("Price must be a number between 1.0 and 10.0, inclusive")
        self._price = value

order = Order("John Doe", "Espresso", 3.5)
print(order.price)
