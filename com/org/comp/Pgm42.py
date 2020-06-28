class ADemo:
    def info_1(self):
        print("Running info_1() instance method")

    @staticmethod
    def info_2():
        print("Running info_2() class method")

ref = ADemo()
ref.info_1()

ADemo.info_2()