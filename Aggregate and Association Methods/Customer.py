
class Customer:
    def __init__(self, name):
        self.name = name
        self.orders = []  

    def create_order(self, coffee, price):
        if not isinstance(coffee, Coffee):
            raise TypeError("coffee must be of type Coffee")
        if not isinstance(price, (int, float)) or price <= 0:
            raise ValueError("price must be a positive number")
        
        new_order = Order(self, coffee, price)
        self.orders.append(new_order)
        return new_order

class Coffee:
    def __init__(self, type_of_coffee):
        self.type_of_coffee = type_of_coffee

class Order:
    def __init__(self, customer, coffee, price):
        if not isinstance(customer, Customer):
            raise TypeError("customer must be of type Customer")
        if not isinstance(coffee, Coffee):
            raise TypeError("coffee must be of type Coffee")
        if not isinstance(price, (int, float)) or price <= 0:
            raise ValueError("price must be a positive number")
        
        self.customer = customer
        self.coffee = coffee
        self.price = price

customer1 = Customer("Alice")
coffee1 = Coffee("Latte")

order1 = customer1.create_order(coffee1, 4.5)

print(order1.customer.name)  
print(order1.coffee.type_of_coffee)  
print(order1.price)  

# Customer's orders:
print(len(customer1.orders))  