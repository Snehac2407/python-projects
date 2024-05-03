# # apto count no of didit in anumber
# n=int(input("enter any number"))
# count=0
# while n!=0:
#     n=n//10
#     count=count+1
# print(count)

# =======or====
# n =int(input("enter any number"))
# count=0
# for i in str(n):
#     n=n/10
#     count+=1
# print(count)


# wap for lcm of two number
'''a,b=[int (x) for x in input("enter the number").split(',')]
max_num = max(a,b)
while (True):
    if (max_num%a==0 and max_num%b==0):
        break
    else :
        max_num=+1
print(f"lcm of {a} and {b} is {max_num}")
'''

# wap for lcm of two number
# a,b=[int (x) for x in input("enter the number").split(',')]
# if a>b:
#     max=a
# else:
#     max=b
# while max>1:
#     if (max%a==0 and max%b==0):
#         print("hcf is",max)
#         break
#     else:
#        max=max-1
#

# wapfor hcf of two number
# num1,num2=[int (x) for x in input("enter the number").split(',')]
# hcf = 1
# for i in range(1, min(num1, num2)):
#     if num1 % i == 0 and num2 % i == 0:
#         hcf = i
# print("Hcf of", num1, "and", num2, "is", hcf)


# wap for palindrome
# n=int(input("Enter number:"))
# temp=n
# rev=0
# while(n>0):
#     remainder = n%10
#     rev=rev*10+remainder
#     n=n//10
# if(temp==rev):
#     print("The number is a palindrome")
# else:
#     print("tukka nhi laga")

# wap for factorial fora number
# n=int(input("enter any number:-"))
# fact=1
# for  i in range(n):
#     fact=n*(n-1)
# print(fact)

# wap for checking wheather a number is a armstrong number ornot
# n=int(input("enter any number to check wheather the number is armstrong or not "))
# sum =0
# temp=n
# power=len(str(n))
# while n>0:
#     digit=n%10
#     sum =sum+(digit**power)
#     n=n//10
# if sum==temp:
#     print("given number is a armstrong number")
# else:
#     print("not an armstrong number")

# =====or====
# n=str(int(input("enter any number to check wheather the number is armstrong or not ")))
# sum =0
# for i in n:
#     sum=sum + int(i)**len(n)
# if sum==int(n):
#     print("given number is a armstrong number")
# else:
#     print("not an armstrong number")

# wap for counting the occurence of digit in a number
# n=str(int(input("enter any number")))
# a={}
# for i in n:
#     if i  in a:
#         a[i] +=1
#     else:
#         a[i]=1
# print(str,(a))
# ========or========
# num = int(input("Enter the number"))
# digit = int(input("Enter a Digit"))
# count = 0
# n = num
# while n != 0:
#     rem = n % 10
#     if rem == digit:
#         count+=1
#     n = n // 10
#
# print("{} occured {} times in {}".format(digit,count,num))

# wap for calculating sum of previous and current value
# n=int(input("enter any number"))
# sum=0
# previous=0
# for i in range(n):
#     sum=previous+i
#     print("sum of previous no ",previous,"and current number",i, "is",sum)
#     previous=i


# wap to check weather the entered number is primeor not:-
# num=int(input("enter any number"))
# for i in range(2,num):
#     if num%i==0:
#         print("its not a prime number")
#         break
# else:
#     print("it's a prime number")

# wap for printing first 10 natural number uisng while loop:-
# i=1
# while i<10:
#     print(i)
#     i+=1

# calculate the sum of all the number from given
# n=int(input("enter the number"))
# sum=0
# i=0
# while n>=i:
#     sum=sum+i
#     i+=1
# print(sum)
# # ooooorrrrrr
# n = int(input("Enter number "))
# x = sum(range(1, n + 1))
# print('Sum is:', x)

# wap for the following pattern:-
# 54321
# 4321
# 321
# 21
# 1
# n= int(input("enter no of element"))
# for i in range(n):
#     for j in range(n-i):
#         print(n-i-j,end="")
#     print()

# enter the element of10
# -10
# -9
# -8
# -7
# -6
# -5
# -4
# -3
# -2
# -1
# n=int(input("enter the element of"))
# for i in range(-10,0,1):
#     print(i)

# wap for displaying all the prime number between a particular range:-
# start=int(input("enter a starting range"))
# end=int(input("enter a ending range"))
# for num in range(start,end+1):
#     if num>1:
#         for i in range(2,num):
#              if (num % i) ==0:
#                  break
#
#         else:
#             print(num)
#
# wap for fibonaccie seies
# num1,num2=[int (x) for x in input("enter the number").split(',')]
# for i in range(5):
#     result=num1+num2
#     num1=num2
#     num2=result
# print(result)

# wap for n series sum such that n=5 (2+22+222+2222+22222):-
# n= int(input("enter the terms required"))
# start= int(input("enter the terms required"))
# result=0
# for i in range(n):
#     start=start*10+start
#     result += start
# print(result)






