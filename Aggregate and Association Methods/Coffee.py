class Customer:
    def __init__(self, name):
        self.name = name
        self._orders = []
    
    def add_order(self, order):
        if isinstance(order, Order):
            self._orders.append(order)
        else:
            raise TypeError("Orders must be of type Order")
    
    def orders(self):
        return self._orders
    
    def coffees(self):
        unique_coffees = {order.coffee for order in self._orders}
        return list(unique_coffees)
    
    def __str__(self):
        return f"Customer: {self.name}, Orders: {len(self._orders)}"

class Coffee:
    def __init__(self, type_of_coffee):
        self.type_of_coffee = type_of_coffee

    def __str__(self):
        return f"Coffee: {self.type_of_coffee}"

class Order:
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
    
    def __str__(self):
        return f"Order: {self.customer.name}, Coffee: {self.coffee.type_of_coffee}, Price: ${self.price}"


customer = Customer("John Doe")
coffee1 = Coffee("Espresso")
coffee2 = Coffee("Latte")

order1 = Order(customer, coffee1, 2.5)
order2 = Order(customer, coffee2, 3.0)

customer.add_order(order1)
customer.add_order(order2)

print(customer)  
print(order1)    
print(coffee1)    
