import threading


class Test_test:
    a = [10, 88]
    b = "string"
    th = threading.local()
    th.ff = []

    def __init__(self):
        self.d = 8
        self.v = "luntik"
        print("papa")

    @staticmethod
    def ponchik(s="ponchik papa"):
        Test_test.th.ff.append(66)
        print(s,Test_test.th.ff)


class Test_quest(Test_test):
    def __init__(self):
        super().__init__()
        print("lopi")


Test_test.ponchik()
