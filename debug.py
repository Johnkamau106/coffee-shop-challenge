from customer import Customer
from coffee import Coffee
from order import Order

# Sample data for testing
if __name__ == "__main__":
    customer1 = Customer("Kamau")
    customer2 = Customer("John")
    
    coffee1 = Coffee("Cappuccino")
    coffee2 = Coffee("Mocha")
    
    order1 = Order(customer1, coffee1, 5.0)
    order2 = Order(customer1, coffee2, 3.5)
    order3 = Order(customer2, coffee1, 4.0)
    
    print(f"{customer1.name}'s orders: {[order.price for order in customer1.orders()]}")
    print(f"{customer1.name}'s coffees: {[cof.name for coffee in customer1.coffees()]}")
    print(f"{coffee1.name}'s orders: {coffee1.num_orders()}")
    print(f"{coffee1.name}'s average price: {coffee1.average_price()}")
    print(f"Most aficionado for {coffee1.name}: {Customer.most_aficionado(coffee1).name}")