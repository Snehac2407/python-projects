# write a program to find some of digits of given number.
'''n= int(input("enter the following numbers"))
add = 0
while(n>0):
    dig=n%10# these we use to get last digit
    add=add+dig
    n = n//10#to add all no
print(add)
# n= (input("enter the following numbers"))
# add = 0
# for i in str(n):
#     add = add+int(i)
# print(add)
# '''
# wap to reverse the given digit
# n= int(input("enter the following numbers"))
# rev = 0
# while (n>0):
#     reminder=n%10# these we use to get last digit
#     rev=rev*10+reminder
# print(rev)

# n= int(input("enter the following numbers"))
# string=str(n)
# size=len(string)
# rev = string[size::-1]
# print (rev)

# wap for product of given digits in a no
n = 5

# n= (input("enter the following numbers"))
# i=1
# product= 1
# for i in str(n):
#    product= product*int(i)
# print(product)

# write a program to calculate sum of series (1/1+1/2+1/3+1/4+.....
# i = 1;n = 34;s = 0.0;
# for i in range(1, n + 1):
#      s = s + 1 / i
# print(s)

# wap to check given no is armstrong or nit
# n= (input("enter the following numbers"))
# order = len(str(n))
# sum = 0
# while n != 0:
#    digit = n %10
#    sum += digit ** order
#    n //= 10
# if n == sum:
#    print(n,"is an Armstrong number")
# else:
# #    print(n,"is not an Armstrong number")
#
# number=int(input("enter a number"))
# number = str(n)
# n = len(number)
# output = 0
# for i in number:
#     output = output + int(i) ** n
#
# if output == int(number):
#     print("yes the number isa armstrong number")
# else:
#     print("no it is not")

#   wap to find factorial of given number:-

# change the value for a different result
num = 7

# To take input from the user
# num = int(input("Enter a number: "))
# fact = 1
# for i in range(1,num + 1):
#        fact = fact*i
# print("The factorial of",num,"is",fact)

# wap for checking weather a no is perfect or not
'''n= int(input("Enter a number: "))
sum=0
for i in range (1,n):
       if n%i==0:
              sum=sum+i
if sum==n:
       print("its a perfect number")
else:
      print("no is not perfect")'''

#  Write a program to accept n number from user and show how many numbers are even or odd.
'''l = [10, 21, 4, 45, 66, 93, 11]
# n= len(list1)
even_count,odd_count=0,0
for i in l :
    if i%2==0:
        even_count += 1
    else:
        odd_count += 1
print("total no of evens in a digit",even_count)
print("total no of odd in a digit", odd_count)
'''
# Write a program to find LCM of two numbers
'''def Lcm(x, y):
   if x > y:
       greater = x
   else:
       greater = y
   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm
num1 = 54,num2 = 24
print("The L.C.M. is",Lcm(num1, num2))'''
# =================OR======================
'''x,y=int(input("x = ")),int(input("y ="))
greater=x  if x>y else y
while greater<=x*y:
    if greater%x==0 and greater%y == 0:
        break
    greater=greater+y
print("lcm of {} ,{} is {} ".format(x,y,greater))'''

# wap for hcf of two number:-
# x,y=int(input("x = ")),int(input("y ="))
# smaller=x  if x>y else x
# while smaller > 1:
#     if smaller%x==0 and smaller%y == 0:
#         break
#     smaller-=1
# print("hcf of {} ,{} is {} ".format(x,y,smaller))

'''def compute_hcf(x, y):
   while(y):
       x, y = y, x % y
   return x

hcf = compute_hcf(234,345)
print("The HCF is", hcf)'''

