import time
from properties import p
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
        prop = p.Property()
        dic = prop.load_property_files(PROP_PATH + property_name + ".properties")
        self.email = str(self.millis()) + dic['email']
        self.password = dic['password']

    def millis(self):
        milli_time = lambda: int(round(time.time() * 1000))
        return milli_time()
