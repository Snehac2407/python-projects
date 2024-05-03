# wap example for parent and childrelationship
# class P():
#     a=100
#     def __init__(self):
#         self.b=34
# class C(P):
#     c=34
# c=C()
# print(c.a,c.b,c.c)

#===when child class has its own counstructor
'''class P():
    a=100
    def __init__(self):
        self.b=34
class C(P):
    c=34
    def __init__(self):
        super().__init__()#here we use super methood to invoke counstrouctor of parent class
        self.d=66

c=C()
print(c.a,c.b,c.c,c.d)'''

# ====wap for geting emloyee information   ====
'''class Candidant():
    def __init__(self,name,age):
        self.name=name
        self.age =age
    def refreshment (self):
        print("please grab your beer glasses with veggie bites")
class Employee(Candidant):
    def __init__(self,name,age,skill,esal):
        super().__init__(name,age)
        self.esal=esal
        self.skill=skill
    def getInfo(self):
        print("following are the information required of each and every employee")
        print("name of employee",self.name)
        print("age of employee", self.age)
        print("salary of employee", self.esal)
        print("name of employee", self.skill)
e=Employee("sneha",20,"python coder",23000)
e.getInfo()
'''


# wap for single level inheriatence
'''class P:
    def m1(self):
#         print("parent class methood")
# class C(P):
#     def m2(self):
#         print("child class methood")
# c=C()
# c.m1()
# c.m2()'''
#
# # wap for multi level inheriatence
# class P:
#     def m1(self):
#         print("parent class methood")
# class C(P):
#     def m2(self):
#         print("child class methood")
# class SC(C):
#     def m3(self):
#         print("sub child class methood")
# c=SC()
# c.m1()
# c.m2()
# c.m3()
#
# # wap for heirachial  inheriatence
# class P:
#     def m1(self):
#         print("parent class methood")
# class C(P):
#     def m2(self):
#         print("1st child class methood")
# class SC(P):
#     def m3(self):
#         print("2nd chilldchild class methood")
# c=SC()
# c.m1()
# # c.m2()
# c.m3()
#
#
# # wap for multiple inheritance
# class P:
#     def m1(self):
#         print("parent class methood")
# class P2:
#     def m1(self):
#         print("mother parent of child")
# class C(P,P2):
#     def m3(self):
#         print("2nd chilldchild class methood")
# c=SC()
# c.m1()
# # c.m2()
# c.m3()




def function(n):
    for i in range(0,int(n/3)):
        j = 1
        while j <= n:
            j = j + 4
            print("*")
function(20)