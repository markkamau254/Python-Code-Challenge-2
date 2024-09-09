class Customer:
    def __init__(self, name):
        self.name = name

class Coffee:
    def __init__(self, type_of_coffee):
        self.type_of_coffee = type_of_coffee
        self._orders = []

    def add_order(self, order):
        if isinstance(order, Order):
            self._orders.append(order)
        else:
            raise TypeError("Orders must be of type Order")

    def orders(self):
        return self._orders

    def customers(self):
        unique_customers = {order.customer for order in self._orders}
        return list(unique_customers)

class Order:
    def __init__(self, customer, coffee):

        if not isinstance(customer, Customer):
            raise TypeError("Customer must be of type Customer")

        
        self.customer = customer
        self.coffee = coffee
        
        coffee.add_order(self)


customer1 = Customer("Alice")
customer2 = Customer("Bob")
coffee1 = Coffee("Latte")
coffee2 = Coffee("Espresso")


order1 = Order(customer1, coffee1)
order2 = Order(customer2, coffee1)
order3 = Order(customer1, coffee2)

# Orders for coffee1 
print([order.customer.name for order in coffee1.orders()])  

# Customers who ordered coffee1 
print([customer.name for customer in coffee1.customers()])  

# Orders for coffee2 
print([customer.name for customer in coffee2.customers()])  