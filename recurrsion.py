# wap to print 1 to n
# def number(num):
#     if num==0:
#         return
#     else:
#         number(num-1)
#         print(num,"\n",end="")
# num=10
# number(num)

# ===========Full-Stop==============
# wap to print n to 1
# def number(num):
#     if num==0:
#         return
#     else:
#         print(num,"\n",end="")
#         number(num - 1)
# num=10
# number(num)

# ===========Full-Stop==============

# wap to find mean of array:-
# def sum_array(arr):
#     if not arr :
#         return 0
#     return arr[0] + sum_array(arr[1:])
# array=[2,3,45,4,32,3]
# Mean=sum_array(array)/len(array)
# print(Mean)
#

# ===========Full-Stop==============

# wap to convert decimal to binary:-
def binary(deci):
    if not deci :
        return 0
    else:
        binary(int(deci/2))
        print(deci%2,end="")
binary(45)


