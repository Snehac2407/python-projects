# '''l =[10,20,30,40]
# l[1] = 555
# print(l)
# '''
#
#
# '''l = [10,20,30]
# l1 = [70,80,90]
# l.append(40)#40 will get added at the end of list l
# l.insert(1,50)#50 will get added at index 1 of list l
# l.extend(l1)
# print(l)
# '''
#
# '''l1 = ['B','D','E','A']
# l1.sort()
# print(l1)
# l1.sort(reverse = True)
# print(l1)'''
# # referncingone variable with another
# '''x = [10,20,30,40]
# y = x
# x[1] = 45
# the problem in this approach is by using one refrence variable if we are changing
# content,then those changes will be reflected to the other refrence variable.
# to overcome this problem we should go for cloning.
# print(id(x))
# print(x)
# print(id(y))
# print(y)'''
# # cloning
# #by slicing of list
# x = [10,20,30,40,50]
# y= x[:]
# y[1] = 888
# print(id(x))
# print(x)
# print(id(y))
# print(y)
#
# '''#by copying
# x = [10,20,30,40,50]
# y = x.copy()
# y[1] = 999
# print(id(x))
# print(id(y))
# print(x)
# print(y)
#
# x = [10,20,30,40,50]
# y= x[:]
# y[1] = 8234
# print(x)
# print(y)'''
#
#
# '''a = [10,20,30]
# b =[40,50,60]
#
# c = a+b
# c = a + [30]#these will print list aand add 90
# print(c)
# '''
# x = ['Dog','Cat','Rat']
# y = ['Dog','Cat','Rat']
# z = ['DOG','CAT','RAT']
#
# print(x==y)
# print(id(x))
# print(id(y))
# print(x!=z)
# print(x>z)
# print(chr(65))
# print(chr(97))
#
# '''n = [[10,20,30],[40,50,60],[70,80,90]]
# print(n)
# for r in n:
#     print(r)
# for j in range(len(n)):        # in matrix format
#     for i in range(len(n[j])):
#         print(n[j][i],end=' ')
#     print()
# '''
#
# words = "the quick brown fox jumps over the lazy dog".split()
#
# print(words)
#
# l = [[w.capitalize(),len(w)] for w in words]
# print(l)


# limit values greater than 15, memorizing of lost values.
# lst = [11,18,9,12,23,4,17]
# lost = []
# for idx in range(len(lst)):
#  val = lst[idx]
#  if val > 15:
#      lost.append(val)
#  lst[idx] = 15
# print("modif:",lst,"-lost:",lost)

# square of list
# x = [1,3,5,7,9]
# sum_squared = sum([y**2 for y in x])
# print(sum_squared)

# wap for taking multiple values from user of different line in evqal
# a,b,c=[eval(x) for x in input("enter the three corresonping values").split(",")]
# print(type(a))
# print(type(b))
# print(type(c))
# print("corresonding values are:-"a,b,c,sep=',')

# sum of elements of list
# l=eval(input("ener the elements"))
# sum=0
# for i in l:
#     sum=sum+i
# print(sum)

# l=eval(input("ener the elements"))
# sum=0
# L=len(l)
# i=1
# while i<=L:
#     sum=sum+i
#     i+=1
# print(sum)

# wap for reversing a list :-
# lst=eval(input("enter the elemenntsof list".split(',')))
# L=len(lst)-1
# for i in range(L,-1,-1):
#     print(lst[i])

#function for multipling string
# n = [23,34,45,7,78]
# times=int(input("from whichyou want to multiply"))
# print(n)
# results=[]
# results=[times*(i) for i in n]
# print(results)

 # Concatenate two lists in the following order
# list1 =['sneha','aakhya']
# list2 =['24','2004']
# result=[x+y for x in list1 for y in list2]
# print(result)

# iteratetwo list simultaneously:-
list1=[23,43,45,56,67]
list2=[23,43,45,56,67]
for x,y in zip(list1,list2):
    print(x,y)