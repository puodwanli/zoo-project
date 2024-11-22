import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()

    def test_child_ticket(self):
        self.assertEqual(self.zoo.get_ticket_price(7), 50)  # อายุในช่วง 0-12

    def test_teen_ticket(self):
        self.assertEqual(self.zoo.get_ticket_price(15), 100)  # อายุในช่วง 13-20

    def test_adult_ticket(self):
        self.assertEqual(self.zoo.get_ticket_price(30), 150)  # อายุในช่วง 21-60

    def test_senior_ticket(self):
        self.assertEqual(self.zoo.get_ticket_price(70), 100)  # อายุ > 60

    def test_invalid_age(self):
        self.assertEqual(self.zoo.get_ticket_price(-1), "Invalid age")  # อายุไม่ถูกต้อง

    # ---------------------------
    # Additional Tests: Invalid Inputs
    # ---------------------------
    def test_invalid_inputs(self):
        self.assertEqual(self.zoo.get_ticket_price("twenty"), "Invalid age")  # String
        self.assertEqual(self.zoo.get_ticket_price(None), "Invalid age")      # None

if __name__ == "__main__":
    unittest.main()



