# -*- coding: utf-8 -*-

import datetime
import random
import threading
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Test_test:
    a = [1]
    __b = "string"
    lo = 487
    che = 0
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
    info = None

    def __init__(self):
        super().__init__()
        print("lopi")
        self.re = 45

    @staticmethod
    def io():
        print()

    @staticmethod
    def text_list_in_text(text, text_list):
        for itr in text:
            print(itr)
            checker = 0
            for p in text_list:
                print(p)
                if p not in itr:
                    checker = 1
                    break
            if checker is 0:
                return itr

    def addDays(self, date, daysToAdd, exactOrRandom):
        if exactOrRandom == 'random':
            daysToAdd = random.randint(0, daysToAdd)
        return date + datetime.timedelta(daysToAdd)


ase = ["hjdkdd, hsusdid, sksls    uiyr", "feredip hike lopi son", "fes ri do"]
sew = ["fes", "ri", "do"]
s = "$456.00"
k = re.search("(\d+)", s).group()
e = s.replace(re.search("[^\d]", s).group(), "")
e = e.replace(re.search("\..+", e).group(), "")
print(k)
# list = [i for i in ase for k in sew if k in i]
# for i in ase:
#     Test_quest.che = 0
#     for k in sew:
#         if k not in i:
#             Test_quest.che = 1
#             break
#     if Test_quest.che is 0:
#         Test_quest.info = i
# #
# print(Test_quest.info)
# print(list)

# op = list(filter(lambda i: "8" in str(i), map(lambda i: str(i) + " ki", Test_test.a)))
# print(op)
