import time

from main.custom_utils.general_utils import property_reader


class Passenger:
    def __init__(self, property_name):
        """ This model of User is created from configured property file """
        prop = property_reader(property_name)
        self.email = prop.get('email')
        if self.email.startswith("@"): self.email = str(Passenger.millis()) + self.email
        self.first_name = prop.get('firstName')
        self.last_name = prop.get('lastName')
        self.age = prop.get('age')
        self.password = prop.get('password')
        self.pay_system = prop.get('paySystem')
        self.phone = prop.get('phone')

    @staticmethod
    def millis():
        return int(round(time.time() * 1000))
