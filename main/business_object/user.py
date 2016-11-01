from properties.p import Property
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
        prop = Property()
        dic = prop.load_property_files(PROP_PATH + property_name + ".properties")
        self.email = dic['email']
        self.password = dic['password']
