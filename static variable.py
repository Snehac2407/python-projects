'''class static:
    a=200
    name ="sneha"
    def __init__(self):
     print(self.a)
    def methood(self):
        self.b=100
        self.a =234
        print(self.a)
        print(self.b)
    @classmethod
    def methood2(cls):
        print(cls.a)
        print(cls.name)
t=static()
t.methood()
static.methood2()#to call any static variable use class name
print(t.__dict__)
print(static.__dict__)
'''


# class Test:
#     a = 10
#     def __init__(self):
#         Test.b = 20
#         del Test.a
#     def m(self):
#         Test.c = 30
#         del Test.b
#     @classmethod
#     def m1(cls):
#         cls.d = 40
#         del Test.c
#     @staticmethod
#     def m2():
#         Test.e = 50
#         del Test.d
#
# # print(Test.__dict__)
# t = Test()
# t.m()
# Test.m2()
# # print(Test.__dict__)

# wap for calculating area and circumference of circle
class Circle:
    def __init__(self,radius):
        self.radius=radius
    def ar_circle(self):
        return 3.14*self.radius**2
    def circum_circle(self):
        return 2*3.14*self.radius
c=Circle(5)
cir=c.circum_circle()
print(cir)
ar=c.ar_circle()
print(ar)
print(c.__dict__)
print(ar_circle.__dict__)

