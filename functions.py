#postional argument
'''def sub(a,b):
    print(a-b)
sub(200,34)'''
#keyword argument
'''def wish(name,msg,age,gender):
    print(name,msg,age,gender)
wish (name="sneha",msg="not a bitch" ,age =19,gender ="FEMALE")
wish (name="antique",msg="is a whore",age =19,gender ="MALE")'''
'''#default argument
def wish(name = "sneha"):
   print("hello",name,"good morning")
wish()'''

#variable length arguments
'''def multiplier(*num):
    prod = 1
    for i in num:
        prod = prod * i

    print("Product:",prod)

multiplier(3,5)
multiplier(1,2,4,34,56,76,5,4,3,4,5,6,7,7,65554,4,4,33,4,55,)
multiplier(2,2,6,7)
'''
'''#for dictionary
def myPrg(**kwargs):
	for key, value in kwargs.items():
		print (key, "-" , value)

# Driver code for kwargs in python
myPrg(name ='sneha', activity ='coding', language='python')'''

# def nameage(name,age):#value name
# 	print("Hii my name is ",name)
# 	print("Hii my age is ",age)
#
# nameage(name="sneha" , age=19)

#factorial of a number
'''def fact(num):
    result  = 1
    while num >=1:
        result = result * num
        num = num - 1
    return result

# print(fact(101))
for i in range(1,23):
    print(fact(i))
'''
'''
#keyword arguments
def wish(name,msg):
    print(name,msg)

wish(name="sneha",msg="good night")
wish(msg="sneha",name="good night")
wish("sneha",msg="good night")
wish(name="sneha","good night") #invalid'''

'''def f1():
    a = 10 #local variable  # a is a local variable must be access inside a function only
    print(a)

def f2():
    print(a)
f1()
f2() #error'''
# a = 10            #here a is a global variable i,e can be access outside thr function
# def f1():
#     global a
#     a = 777
#     print(a)
# print(a)
# def f2():
#     print(a)
# f1()
# f2()
'''def f1():
    global a
    a = 777
    print(a)


def f2():
    print(a)
f1()
f2()'''

# recursion function


# factorial = n * factorial(n-1)
# def factorial(n):
#     if n == 100:
#         result = 1
#     else:
#         result = n * factorial(n-1)
#     return result
# print(factorial(3))

# wapto take arguments from user:-
# def demo(*args):
#     for i in args:
#         print(i)
# demo(24,45,66)
# demo(48,95,64)


# wap for setting a default arguments in a function :-
# def information(name,salary=9000):
#     print("Name",name, "Salary",salary)
# information ("sneha",23000)
# information("jessica")

# wap for nested function for adding two number and add extra five to the result
# def outer(a,b):
#     def addition(a,b):
#         return a+b
#     add=addition(a,b)
#     return add+5
# result=outer(10,25)
# print(result)

# wap for recurssive function for the sum of 10natural number:-
# def addition(num):
#     if num:
#         return num + addition(num - 1)
#     else:
#         return 0
#
# res = addition(10)
# print(res)

# wap to- get even_number from list using nested function :-
# def Even(Lst):
#     def get_even(num):
#         if num % 2==0:
#             return True
#         else:
#             return False
#     new_list=[]
#     for num in Lst:
#         if get_even(num)==True:
#             new_list.append(num)
#         print("finall list",new_list)
# orignal_list=[12,34,22,33,13,67,75,43]
# Even(orignal_list)


# The nested function checks if the given user has the required access rights to the page.
#  Instead of checking if the user is equal, you can query the database . ‘admin’

# def has_permission(page):
#     def permission(username):
#         if username.lower() == "admin":
#           return (f"'{username}' has right to open {page}.")
#         else:
#              return (f"'{username}' does not have right to open {page}.")
#     return permission
# check_admin_page_permision = has_permission("Admin Page")
# print(check_admin_page_permision.__name__)
# print (check_admin_page_permision ("admin"))
# print (check_admin_page_permision ("adams"))

def debug(func):
    def _debug(*args, **kwargs):
        result = func(*args, **kwargs)
        print(
            f"{func.__name__}(args: {args}, kwargs: {kwargs}) -> {result}"
        )
        return result
    return _debug
@debug
def add(a, b):
    return a + b
 add(5, 6)
# add(args: (5, 6), kwargs: {}) -> 11
# 11