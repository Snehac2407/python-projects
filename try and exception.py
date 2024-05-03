'''# wap for zerodivision error exception handling
print("statment-1")
try:
    print(10/0)
except ZeroDivisionError:
    print(10/2)
print("Statement-3")
'''
# printingexception information as message
# try:
#     print(10/0)
# except ZeroDivisionError as msg:
#     print(msg)
#
# try:
#     x = int(input("enter first number"))
#     y = int(input("enter second number"))
#     print(x/y)
# except ZeroDivisionError:
#     print("can't divide with zero")
# except ValueError:
#     print("please provide some int value")
#

# x = int(input("enter any integer"))
# try:
#   print(x)
# except NameError as msg:
#    print("msg")
# except:
#   print("Something else went wrong")
#
#
# try:
#   f = open("trail.txt")
#   try:
#     f.write("Lorum Ipsum")
#   except File:
#     print("Something went wrong when writing to the file")
#   finally:
#     f.close()
# except:
#   print("Something went wrong when opening the file")


#   user define exceptiond
# class TooYoungException(Exception):
#     print()
#     class TooOldException(Exception):
#         print()
#
# age = int(input("enter age"))
# if age > 60:
#     raise TooYoungException("you are not eligible to marry wait for some more time ")
# elif age < 18:
#     raise TooOldException("you are not eligible")
# else:
#     print("please go and marry")


# define Python user-defined exceptions
class InvalidAgeException(Exception):
    print('',end=" ")
number = 18
try:
    input_num = int(input("Enter a number: "))
    if input_num < number:
        raise InvalidAgeException
    else:
        print("Eligible to Vote")

except InvalidAgeException:
    print("Exception occurred: Invalid Age")