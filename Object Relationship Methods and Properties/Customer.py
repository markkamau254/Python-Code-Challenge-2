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

class Coffee:
    def __init__(self, type_of_coffee):
        self.type_of_coffee = type_of_coffee

    def __repr__(self):
        return f"Coffee({self.type_of_coffee})"

class Order:
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        
        self.customer.add_order(self)

    def __repr__(self):
        return f"Order(Customer: {self.customer.name}, Coffee: {self.coffee.type_of_coffee}, Price: {self.price})"

customer = Customer("John Doe")
coffee_1 = Coffee("Espresso")
coffee_2 = Coffee("Latte")

order_1 = Order(customer, coffee_1, 5.0)
order_2 = Order(customer, coffee_2, 4.5)

print(customer.orders())  
print(customer.coffees())  