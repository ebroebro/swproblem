class Calculator:
    count=0

    def info(self):
        print("1")

    @staticmethod
    def add(a,b):
        print("2")

    @classmethod
    def history(cls):
        print('3')

c1 = Calculator()
c1.info()
c1.add(1,2)
c1.history()