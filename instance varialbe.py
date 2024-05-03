# 1.instance variable are those variable those value can be varied from object to object
# 2.instance variable can be declared inside constructor,methood,outside of the class
# 3.if two object is having common  instance variable and if say OBJ1 deleted the variable then
# that variable wont going to be deleted from OBJ2 as every object has seprated copy of instance variable
# and same is applicable on value change of object






# INSTANCE VARIABLE can be assigned as following:-
# 1.inside constructor
'''class Student:
    def __init__(self,name,roll_no,subject):#inside constructor values are assigned
        self.name=name
        self.roll = roll_no
        self.sub = subject
    def info(self):
        print("hii i m",self.name)
        print("my roll number is", self.roll)
        print("i choose", self.sub,"as my subject")
s1 = Student("sneha",23,"BCA")
# print(s1.name,s1.roll,s1.sub)
s1.info() #calling methood
s2 = Student("motabhen",21,"B.com")
# print(s2.name,s2.roll,s2.sub)
s2.info()'''

#2.inside instance method by using self variable.
'''class Student:
    def __init__(trail):
        trail.name='sneha'
        trail.roll = 45
        trail.sub ='bca'
    def info(trail):
        trail.college = 'renaisancce'
s = Student()
s.info()
print(s.__dict__)'''

# 3.outside of the class by using object refrence variable.
# class Student:
#     def __init__(trail):
#         trail.name='sneha'
#         trail.roll = 45
#         trail.sub ='bca'
#     def info(trail):
#         trail.college = 'renaisancce'
# s = Student()
# s.info()
# s.mobile_no=23456784
# print(Student().mobile_no)
# print(s.__dict__)

'''class Test:
    def __init__(self):
        self.a = 10
        self.b = 20
    def m1(self):
        self.c = 30

t = Test()
t.m1()
t.d = 40
print(Test().d)
print(t.__dict__)'''


'''class Student:
    def __init__(trail):
        trail.name='sneha'
        trail.roll = 45
        trail.sub ='bca'
        Student.count=+1
    def info(trail):
        print("hii i m",trail.name)
        print("my roll number is", trail.roll)
        del.subject
        print("i choose", trail.sub,"as my subject")
s = Student()
s.info()
print(Student.count)
'''
# deleting an instance variable
# class Student:
#     def __init__(trail):
#         trail.name='sneha'
#         trail.roll = 45
#         trail.sub ='bca'
#     def info(trail):
#         print("hii i m",trail.name)
#         print("my roll number is", trail.roll)
#         print("i choose", trail.sub,"as my subject")
#         del trail.sub
# s = Student()
# s.info()
# print(s.__dict__)


# calling instance methood without variable
'''class Student:
    def __init__(self,name,mark):#inside constructor values are assigned
        self.name=name
        self.mark = mark
        self.display()#as here diplay is called inside constructor only
    def display(self):
        print("dear",self.name)
        print("your marks are", self.mark)
        self.grade()#here grade is called without object variable
    def grade(self):
       if self.mark>=90:
           print("you will become employee ")
       elif self.mark >= 80:
           print("you willl become a manager ")
       elif self.mark>=70:
           print("you will own a software company ")
       else:
           print("you got excellence grade world bank will take loan from you ")

s=Student('sneha',45)
s=Student('arshi',77)'''

# =========getter and setter methood for taking user input========
class Student:
    def setName(self,name):
        self.name=name
    def getName(self):
        return  self.name
    def setMark(self,mark):
        self.mark=mark
    def getMark(self):
        return self.mark
l=[]
total=int(input("enter no of student"))
for i in range(total):
    s=Student()
    name=input("enter your name ")
    mark=int(input("enter your marks"))
    s.setName(name)
    s.setMark(mark)
    l.append(s)
print(l)
for s in l:
    print("name",s.getName())
    print("enter your name ",s.getMark())
    print()

