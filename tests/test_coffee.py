import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestCoffee(unittest.TestCase):

    def setUp(self):
        Order.all.clear()
        self.customer = Customer("Kamau")
        self.coffee = Coffee("Latte")
        self.order = Order(self.customer, self.coffee, 6.0)

    def test_name_validation(self):
        with self.assertRaises(TypeError):
            Coffee(123)
        with self.assertRaises(ValueError):
            Coffee("Hi")

    def test_name_immutable(self):
        with self.assertRaises(AttributeError):
            self.coffee.name = "Mocha"

    def test_orders_method(self):
        self.assertIn(self.order, self.coffee.orders())

    def test_customers_method(self):
        self.assertIn(self.customer, self.coffee.customers())

    def test_num_orders(self):
        self.assertEqual(self.coffee.num_orders(), 1)

    def test_average_price(self):
        Order(self.customer, self.coffee, 4.0)
        self.assertAlmostEqual(self.coffee.average_price(), 5.0)

if __name__ == "__main__":
    unittest.main()
