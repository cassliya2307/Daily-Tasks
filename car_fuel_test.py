import unittest
from car_fuel import *

class MyTestCase(unittest.TestCase):
    def test_for_fuel_consumed(self):
        actual = get_car_fuel_consumed(30)
        expected    = 2.0
        self.assertEqual(actual, expected)

    def test_for_tank_refuel_1(self):
        actual = refuel_tank(30 , 20)
        expected = 50
        self.assertEqual(actual, expected)
    def test_for_tank_refuel_2(self):
        actual = refuel_tank(30 , 50)
        expected = "Tank overflow"
        self.assertEqual(actual, expected)




