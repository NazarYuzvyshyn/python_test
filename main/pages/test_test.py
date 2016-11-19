# -*- coding: utf-8 -*-

import datetime
import random
import threading

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Test_test:
    a = [1]
    __b = "string"
    lo = 487
    th = threading.local()
    th.ff = []

    @staticmethod
    def get():
        return Test_test.__b

    def __init__(self):
        self.d = 8
        self.__v = "luntik"
        print("papa" + Test_test.__b)

    @staticmethod
    def ponchik(s="ponchik papa"):
        Test_test.th.ff.append(66)
        print(s, Test_test.th.ff)


class Test_quest(Test_test):
    daysToAdd = 45
    def __init__(self):
        super().__init__()
        print("lopi")
        self.re = 45

    @staticmethod
    def io():
        print(  )

    def addDays(self, date, daysToAdd, exactOrRandom):
        if exactOrRandom == 'random':
            daysToAdd = random.randint(0, daysToAdd)
        return date + datetime.timedelta(daysToAdd)

# print(Test_quest.daysToAdd)
s = str()
if Test_test.a:
    print("not empty")
# op = list(filter(lambda i: "8" in str(i), map(lambda i: str(i) + " ki", Test_test.a)))
# print(op)
