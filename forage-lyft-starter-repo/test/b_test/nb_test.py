import unittest
from battery.nubbinBattery import NubbinBattery
from datetime import date

#more than 4 years for true and less than 4 years for false
class TestNB(unittest.TestCase):
    def test_need_service_T(self):
        current_date= date.fromisoformat("2023-06-28")
        last_service_date= date.fromisoformat("2018-06-28")
        battery= NubbinBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())
        
    def test_need_service_F(self):
        current_date= date.fromisoformat("2023-06-28")
        last_service_date= date.fromisoformat("2021-06-28")
        battery= NubbinBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())