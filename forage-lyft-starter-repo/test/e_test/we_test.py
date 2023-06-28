import unittest
from engine.willoughby_engine import WilloughbyEngine

#true for more than 60000 miles else false
class TestCE(unittest.TestCase):
    def test_needs_service_T(self):
        current_mileage=65000
        last_service_mileage=0
        engine= WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_needs_service_F(self):
        current_mileage=25000
        last_service_mileage=0
        engine= WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())