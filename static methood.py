class Calculator:
    @staticmethod
    def add(x,y):
        print("sum is",x+y)

    @staticmethod
    def sub(x,y):
        print("difference is",x-y)

    @staticmethod
    def multipy(x,y):
        print("product  is",x*y)

    @staticmethod
    def division(x,y):
        print("reult of divide is",x/y)
Calculator.add(12,34)
Calculator.sub(12,34)


# wap for accessing methoods from one class to another
class Employee:
    def __init__(self,ename,esal):
        self.ename=ename
        self.esal=esal
    def display(self):
        print("emploee name",self.ename)
        print("emploee salary",self.esal)
class Test:
    def update (emp):#as there is no refernce for emp so  not a instanc methood
        emp.esal=emp.esal+10000
        emp.display()
e=Employee('sneha',23455)
Test.update(e)#here e is turning to an argumentto emp