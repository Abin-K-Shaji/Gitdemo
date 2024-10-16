
from Class import Calculator


class ChildImp(Calculator):
    num2=100

    def __init__(self):
        Calculator.__init__(self,2,5)

    def data(self):
        return self.num2 + self.num +self.summation()

obj=ChildImp()
print(obj.data())

