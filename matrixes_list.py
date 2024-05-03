'''n = [[10,20,30],[40,50,60],[70,80,90]]
print(n)
for j in range(len(n)):
    for i in range(len(n[j])):
        print(n[j][i],end=' ')
    print()'''


'''length=len(n)
for j in range(length):
    for i in range(length[j]):#not runing
        print(n[j][i],end=' ')
    print()
'''
'''matrix = [[column for column in range(0,10)] for row in range(20,40)]
print(matrix)'''

#WAP for taking user input for matrixes
# Row = int(input("Enter the number of rows:"))
# Column = int(input("Enter the number of columns:"))
# matrix = []
# print("Enter the entries row wise:")
# for row in range(Row):# A for loop for row entries
#     a = []
#     for column in range(Column):# A for loop for column entries
#         a.extend(input())
#     matrix.extend(a)

# For printing the matrix
# for row in range(Row):
#     for column in range(Column):
#         print(matrix[row][column], end=" ")
#     print()


# wap for sum of two matrixs

#
# matrixOne = [[6,9,11],
#              [2 ,3,8]]
#
# matrixTwo = [[15,18,11],
#              [26,16,19]]
#
# result = [[0,0,0],
#          [0,0,0]]
#
#
# # First iterate rows
# for i in range(len(matrixOne)):
#    # Second iterate columns
#    for j in range(len(matrixOne[0])):
#        result[i][j] = matrixOne[i][j] + matrixTwo[i][j]
# print("Addition of two Matrix In Python")
# for res in result:
#    print(res)

# wap for adding two matrixs of mXn taking input from user
# m,n=[int (x) for x in input("enter the size ").split(',')]
# def matrix(m,n):
#     output =[]
#     for i in range(m):
#         rows=[]
#         for j in range(n):
#             inp=int(input(f"enter output[{i}],[{j}]"))
#             rows.append(inp)
#         output.append(rows)
#     return output
# def sum(A,B):
#     output =[]
#     for i in range(len(A)):
#         rows=[]
#         for j in range(len(A[0])):
#             rows.append(A[i][j]+B[i][j])
#         output.append(rows)
#     return output
# # A= int(input("enter elements of A "))
# # B= int(input("enter elements of B "))
# def multiplication(A,B):
#     output =[]
#     for i in range(len(A)):
#         rows=[]
#         for j in range(len(A[0])):
#             rows.append(A[i][j]*B[i][j])
#         output.append(rows)
#     return output
# A=matrix(m,n)
# B=matrix(m,n)
# s=sum(A,B)
# M=multiplication(A,B)
# print (A)
# print (B)
# print(s)
# print(M)
# output:-
# [[23, 43]]
# [[55, 67]]
# [[78, 110]]

# m=[[1, 3, 2], [4, 6, 5], [1, 5, 7]]
# r=len(m)
# c=len(m[0])
# l=[]
# for i in range(r):
#     max=0
#     for j in range(c):
#         if m[i][j] > max:
#             max = m[i][j]
#     l.append(max)
# m2 = list(zip(*m))
# l2=[]
# for i in range(r):
#     max=0
#     for j in range(c):
#         if m[i][j] > max:
#             max = m[i][j]
#     l2.append(max)
#
# print(l)
# print(l2)
# a=[]
# for r in range(len(m)):
#     for c in range(len(m2)):
#         b = m[r][c]
#         if (l[r], l2[c]) == (b, b):
#
#             a.append(b)
# print(len(a))


