import time

from ..custom_utils.constants import PROP_PATH


class User:
    name = ""
    surename = ""
    age = ""
    email = ""
    password = ""
    city = ""

    def __init__(self, property_name):
        """ This model of User is created from configured property file """
        prop = dict(line.strip().split('=') for line in open(PROP_PATH + property_name + '.txt'))
        self.email = str(self.millis()) + prop.get('email')
        self.password = prop.get('password')

    def millis(self):
        milli_time = lambda: int(round(time.time() * 1000))
        return milli_time()
