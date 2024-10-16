class Calculator:
    num=100

    def __init__(self,a,b):
        self.fnumber=a
        self.snumber=b


    def greeting(self):
        print("abin")
    def summation(self):
        return self.fnumber + self.snumber + Calculator.num

obj= Calculator(5,6)
obj.greeting()
print(obj.summation())


