'''# wap for sum of n natural no
def add(num):
    sum=0
    if num==0:
        return num
    else:
        sum=num+add(num-1)
    return sum
print(add(30))
#=========or using for loop==========
n=int(input("enter no "))
sum=0
for i in range(n):
    sum =sum+i
print(sum)'''

# wap for printing table of any number
# def table(n,i):
#     if i>10:
#         return
#     else:
#         print(n,"*",i,"=",n*i)
#         return table(n,i+1)
# print(table(20,1))
# ========or=====
# n=20
# for i in range(1,int(n/2)):
#     print(n, "*", i, "=", n * i)

# wap for fibonacci
