from battery.battery import Battery
from utility import add_years_to_date

class NubbinBattery(Battery):
    def __init__(self, current_date, last_service_date):
        self.current_date=current_date
        self.last_service_date=last_service_date  
    def needs_service(self):
        date_which_battery_should_b_serviced=add_years_to_date  
        if date_which_battery_should_b_serviced < self.current_date:
            return True
        else:
            return False