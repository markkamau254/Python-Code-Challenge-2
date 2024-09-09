class Customer:
    _all_customers = []

    def __init__(self, name):
        self.name = name
        self.orders = [] 
        Customer._all_customers.append(self)  

    def create_order(self, coffee, price):
        if not isinstance(coffee, Coffee):
            raise TypeError("coffee must be of type Coffee")
        if not isinstance(price, (int, float)) or price <= 0:
            raise ValueError("price must be a positive number")
        
        new_order = Order(self, coffee, price)
        self.orders.append(new_order)
        return new_order

    @classmethod
    def most_aficionado(cls, coffee):
        max_spent = 0
        top_customer = None

        for customer in cls._all_customers:
            total_spent = sum(order.price for order in customer.orders if order.coffee == coffee)
            if total_spent > max_spent:
                max_spent = total_spent
                top_customer = customer

        return top_customer 

class Coffee:
    def __init__(self, type_of_coffee):
        self.type_of_coffee = type_of_coffee
        self._orders = []

    def add_order(self, order):
        if isinstance(order, Order):
            self._orders.append(order)
        else:
            raise TypeError("Orders must be of type Order")

class Order:
    def __init__(self, customer, coffee, price):
        if not isinstance(customer, Customer):
            raise TypeError("Customer must be of type Customer")
        if not isinstance(coffee, Coffee):
            raise TypeError("Coffee must be of type Coffee")
        if not isinstance(price, (int, float)) or price <= 0:
            raise ValueError("Price must be a positive number")
        
        self.customer = customer
        self.coffee = coffee
        self.price = price
        
        coffee.add_order(self)

customer1 = Customer("Alice")
customer2 = Customer("Bob")
coffee1 = Coffee("Latte")

order1 = customer1.create_order(coffee1, 5.0)
order2 = customer2.create_order(coffee1, 7.5)
order3 = customer1.create_order(coffee1, 3.0)

top_spender = Customer.most_aficionado(coffee1)
if top_spender:
    print(f"{top_spender.name} made the most orders for {coffee1.type_of_coffee}")
else:
    print(f"No orders for {coffee1.type_of_coffee}")
