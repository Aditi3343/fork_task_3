import unittest
from engine.sternman_engine import SternmanEngine

#true when warning indicator is on
class TestCE(unittest.TestCase):
    def test_needs_service_T(self):
        warning_light_is_on=True
        engine= SternmanEngine(warning_light_is_on)
        self.assertTrue(engine.needs_service())

    def test_needs_service_F(self):
        warning_light_is_on= False
        engine= SternmanEngine(warning_light_is_on)
        self.assertFalse(engine.needs_service())