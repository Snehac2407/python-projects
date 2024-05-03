#self variable
# self is a default vairable that always point to current object PYTHON VIRTUAL MACHINE providevalue to self
# 1st argument to instance variableis always self
# by self variable we can access instance variable and methood
# self should be 1st parameter inside constructor and instance methood
# self is not a keyword so we can use any thing
'''class Student:
    def __init__(trail):
        trail.name='sneha'
        trail.roll = 45
        trail.sub ='bca'
    def info(trail):
        print("hii i m",trail.name)
        print("my roll number is", trail.roll)
        print("i choose", trail.sub,"as my subject")
s = Student()
s.info()'''

#CONSTRUTOR:-
# main purpose of constructor is to declare and initalize the instance variable
#  per object constructor will be exectued once only
# each class have atleast one constructor and these are optional if we dont declare then by default PVM
#  will declare it
#  PVM always consider last constructor
# constructor is a special methood and constructors get created  automatically when objects are created
# constructor overloading is not possible in python
# constructor can be called explicitly but then will be act as a normal methood and
# no new object will going to be created

'''class constructor:
    def __init__(self):
        print("here is are construtor",id(self))
t=constructor()
t.__init__()
t.__init__()
t.__init__()
t.__init__()#here id of self and obect t will be same as self points to current object'''

'''class check:
    def __init__(self,name):
        self.name=name

        def __init__(self, name):
            self.name = neha

d =check("sneha")
print(d.name)
d.__init__("aakhya")
print(d.name)
s=check("soumya")
print(s.name)'''


# # passing class member to another
# class Employee:
#     def __init__(self,eno,ename,esal):
#         self.eno = eno
#         self.ename = ename
#         self.esal = esal
#     def display(self):
#         print("eno:-",self.eno)
#         print("ename:-",self.ename)
#         print("esal:-",self.esal)
#
# class Test:
#     def modify(emp):
#         emp.esal = emp.esal + 10000
#
#         emp.display()
#
# e = Employee(100,'sneha',1000)
# e = Employee(101,'neha',1356)
# e.display()
#
# Test.modify(e)

#
# class Pizza:
#     def __init__(self,spicy,cheeze_brust):
#         self.spicy='indi tandori'
#         self.cheeze_brust='green chilly'
#     def show (self):
#         print("priemium quality spicy pizza is",self.spicy)
#         print("priemium quality cheezy pizza is", self.cheeze_brust)
# pizzy=Pizza('indi tandori','green chilly')
# pizzy.show()
#
# class Alternative:
#     def add(Shop):
#         Shop.spicy='punjabi tadka'
#         Shop.cheeze_brust = 'magrita'
#         Shop.show()
# Alternative.add(pizzy)
#
#
#
# # class inside class
# class Person:
#     def __init__(self):
#         self.name = 'jonny'
#         self.dob = self.Dob()
#     def display(self):
#         print("Name:-",self.name)
#     class Dob:
#         def __init__(self):
#             self.dd = 10
#             self.mm = 10
#             self.yy = 1989
#         def display(self):
#             print('Dob={}/{}/{}'.format(self.dd,self.mm,self.yy))
# p = Person()
# p.display()
# d = p.dob
# d.display()

# heirarchy of clases(nested classes )
'''class Bank:
    def __init__(self):
        self.Bname="CENTRAL BANK OF INDIA"
        self.Account=self.Account()
        self.Withdraw=self.Account.Withdraw()

    def display(self):
        print("",self.Bname,"AT YOUR SERVICE")
        self.Account.info()
        self.Account.details()
        self.Withdraw.debit()

    class Account:
        def info(self):
            self.name="sneha"
            self.age=20
            self.acc_no=2345432

        def details(self):
            print(" Name of account holder is",self.name)
            print(" Age of account holder is", self.age)
            print(" Account no. is", self.acc_no)


        class Withdraw:
            def debit (self):
                self.cash="cash"
                self.cheque="cheque"
                print(" Withdrawal can be made  from either cash or by  cheque ")
b=Bank()
b.display()'''

# wap for nested  clases
class Person:
    def __init__(self,dd,mm,yyyy):
        self.name="sneha"
        self.dob=self.dob(dd,mm,yyyy)

    def display(self):
        print("name of the person is",self.name)
        self.dob.display()

    class dob:
        def __init__(self,dd,mm,yyyy):
           self.dd=dd
           self.mm=mm
           self.yyyy=yyyy

        def display(self):
            print('DOB is {} /{}/{} '.format(self.dd,self.mm,self.yyyy))
day=Person(12,6,2004)
day.display()

# nested methood
class Calculator:
    def var():
        def methood (a,b):
            print("sum",a+b)
            print("sub", a-b)
            print("multiply",a*b)
            print("divide",a/b)
            print()

        methood(23,456)
        methood(3453,456)
        methood(23,456)

c=Calculator
c.var()

# nested class with prorperty of inheiretance
class Department:
    def __init__(self,Dname,HOD_name,post):
        self.Dname=Dname
        self.HOD_name=HOD_name
        self.post=post
    def  D_details (self):
        print("these are required information of a department \n 1. {} is the name of deparment \n 2.{} is are HOD \n 3.  I am {}".format(self.Dname,self.HOD_name,self.post))
class Candidant():
    def __init__(self,name,age):
        self.name=name
        self.age =age
    def refreshment (self):
        print("please grab your beer glasses with veggie bites")
class Employee(Candidant):
    def __init__(self,name,age,skill,esal,D):
        super().__init__(name,age)
        self.esal=esal
        self.skill=skill
    def getInfo(self):
        print("following are the information required of each and every employee")
        print("name of employee",self.name)
        print("age of employee", self.age)
        print("salary of employee", self.esal)
        print("name of employee", self.skill)

D=Department("developer","andrew","intern")
D.D_details()
e=Employee("sneha",20,"python coder",23000,D)
e.getInfo()
e.refreshment()



