import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestOrder(unittest.TestCase):

    def setUp(self):
        Order.all.clear()
        self.customer = Customer("Jane")
        self.coffee = Coffee("Flat White")
        self.order = Order(self.customer, self.coffee, 5.5)

    def test_init_values(self):
        self.assertEqual(self.order.customer, self.customer)
        self.assertEqual(self.order.coffee, self.coffee)
        self.assertEqual(self.order.price, 5.5)

    def test_invalid_price_type(self):
        with self.assertRaises(TypeError):
            Order(self.customer, self.coffee, "5.0")

    def test_invalid_price_range(self):
        with self.assertRaises(ValueError):
            Order(self.customer, self.coffee, 0.5)

    def test_immutable_price(self):
        with self.assertRaises(AttributeError):
            self.order.price = 6.0

    def test_invalid_customer_type(self):
        with self.assertRaises(TypeError):
            Order("NotACustomer", self.coffee, 5.0)

    def test_invalid_coffee_type(self):
        with self.assertRaises(TypeError):
            Order(self.customer, "NotACoffee", 5.0)

if __name__ == "__main__":
    unittest.main()
