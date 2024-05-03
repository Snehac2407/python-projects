'''class Animal:
    legs=4
    @classmethod
    def walk(cls,name):
        print('{} walks with {} legs'.format(name,cls.legs))
Animal.walk('dog')
Animal.walk('cat')
Animal.walk('cow')
Animal.walk('elephant')
Animal.walk('goat')
'''

# wap forthe the ount of no of object created
'''class Test:
    count=0
    def __init__(self):
        Test.count=Test.count+1
    @classmethod
    def no_obj(cls):
        print("the no object are",Test.count)
t=Test()
t1=Test()
t2=Test()
t3=Test()
Test.no_obj()
t7=Test()
t8=Test()
t9=Test()
Test.no_obj()'''
