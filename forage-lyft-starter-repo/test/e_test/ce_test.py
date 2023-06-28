import unittest
from engine.capulet_engine import CapuletEngine

#true for more than 30000 miles else false
class TestCE(unittest.TestCase):
    def test_needs_service_T(self):
        current_mileage=35000
        last_service_mileage=0
        engine= CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_needs_service_F(self):
        current_mileage=25000
        last_service_mileage=0
        engine= CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())