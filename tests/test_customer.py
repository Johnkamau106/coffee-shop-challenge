import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestCustomer(unittest.TestCase):

    def setUp(self):
        Order.all.clear()
        self.customer = Customer("Kamau")
        self.coffee = Coffee("Espresso")
        self.order = Order(self.customer, self.coffee, 5.0)

    def test_name_validation(self):
        with self.assertRaises(TypeError):
            Customer(123)
        with self.assertRaises(ValueError):
            Customer("")
        with self.assertRaises(ValueError):
            Customer("A" * 16)

    def test_orders_method(self):
        self.assertIn(self.order, self.customer.orders())

    def test_coffees_method(self):
        self.assertIn(self.coffee, self.customer.coffees())

    def test_create_order(self):
        new_order = self.customer.create_order(self.coffee, 4.0)
        self.assertIn(new_order, Order.all)
        self.assertEqual(new_order.customer, self.customer)
        self.assertEqual(new_order.coffee, self.coffee)

    def test_most_aficionado(self):
        c2 = Customer("John")
        Order(c2, self.coffee, 6.0)
        result = Customer.most_aficionado(self.coffee)
        self.assertEqual(result.name, "John")

if __name__ == "__main__":
    unittest.main()
