import datetime
import random

from property_files.prop_reader import property_reader


class Ticket:
    def __init__(self, property_name):
        prop = property_reader(property_name)
        self.get_info = []
        self.get_round_info = []
        self.price = None
        self.round_price = None

        self.range = prop.get("range")
        self.days_to = prop.get("departureDays")
        self.forward_date = Ticket.add_days(datetime.date.today(), int(self.days_to), self.range)

        self.days_from = prop.get("backAfterDays")
        self.backward_date = Ticket.add_days(self.forward_date, int(self.days_from), 'false')

        self.forward_city = prop.get("departureFrom")
        self.backward_city = prop.get("arrivalTo")

    @staticmethod
    def add_days(date, days_to_add, range_or_not):
        if range_or_not == 'true':
            days_to_add = random.randint(0, days_to_add)
        return date + datetime.timedelta(days_to_add)

