from properties.p import Property

from tests.test_Pack.constantssss import PATH


class Dog:
    name = ""
    age = 0
    city = ""



    def __init__(self, file_name):
        prop = Property()
        dic = prop.load_property_files(PATH + file_name + ".properties")
        self.name = dic['name']
        self.age = dic["age"]
        self.city = dic["city"]




