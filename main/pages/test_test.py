import threading


class Test_test:
    a = [10, 88, 23, 77, 89, 52, 102]
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
    def __init__(self):
        super().__init__()
        print("lopi")


s = str(Test_test.lo)
print(s[0])
op = list(filter(lambda i: "8" in str(i), map(lambda i: str(i) + " ki", Test_test.a)))
print(op)
