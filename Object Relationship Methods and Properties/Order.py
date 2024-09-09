class Customer:
    def __init__(self, name):
        self.name = name

class Coffee:
    def __init__(self, type_of_coffee):
        self.type_of_coffee = type_of_coffee

class Order:
    def __init__(self, customer, coffee):
        self.customer = customer
        self.coffee = coffee

    # customer
    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, value):
        if not isinstance(value, Customer):
            raise TypeError("customer must be of type Customer")
        self._customer = value

    # coffee
    @property
    def coffee(self):
        return self._coffee
    
    @coffee.setter
    def coffee(self, value):
        if not isinstance(value, Coffee):
            raise TypeError("coffee must be of type Coffee")
        self._coffee = value

customer = Customer("Alice")
coffee = Coffee("Latte")
order = Order(customer, coffee)

print(order.customer.name)  
print(order.coffee.type_of_coffee)  