import datetime
import random

from main.custom_utils.general_utils import property_reader


class Ticket:
    def __init__(self, property_name):
        prop = property_reader(property_name)
        self.train_number = None
        self.train_number_round = None
        self.place_type = None
        self.place_type_round = None
        self.place_number = None
        self.place_number_round = None
        self.last_and_first_names = None
        self.price = None
        self.price_round = None

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

    def get_info(self) -> list:
        return list([self.train_number, self.place_type, self.place_number,
                     self.last_and_first_names, self.price, ])

    def get_round_info(self) -> list:
        return list([self.train_number_round, self.place_type_round,
                     self.place_number_round, self.last_and_first_names, self.price_round])
