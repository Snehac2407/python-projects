'''#wap for full pyramid where in each row no of stars are odd no of time
    *
   ***
  *****
 *******
*********'''
# n=int(input("enter number of rows"))
# for i in range(n):
#     print(" "*(n-i-1) + str(("*")*(2*i+1)) ,end=" ")
#     print()
# =========or=======
# n=int(input("enter number of rows"))
# for i in range(n):
#     print(" "*(n-i-1) + str(("* ")*(i+1)) ,end=" ")
#     print()

# pyramid of a number
# rows = 5
# for i in range(1, rows + 1):
#     for j in range(1, i + 1):
#         print(j, end=' ')
#     print('')

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

#  number pattern pyramid
# rows = 5
# b=0#these is for taking no from where to start pyramid
# for i in range( 1,rows+1):
#     b+=1#for pyramid no increasement
#     for j in range(1, i + 1):
#         print(b, end=' ')
#     print()
#

#INVERTED NUMBER Pyramid reverse for loop from 5 to 0
# rows = 5
# b=0#these is for taking no from where to start pyramid
# for i in range(rows, 0, -1):
#     b+=1#for pyramid no increasement
#     for j in range(1, i + 1):
#         print(b, end=' ')
#     print()

#invwerted pyramid
# rows = 5
# for i in range(rows, 0, -1):
#     for j in range(1, i + 1):
#         print(j, end=' ')
#     print()

# pyramid of stars
# rows = 5
# b=0#these is for taking no from where to start pyramid
# for i in range( 1,rows+1):
#     b+=1#for pyramid no increasement
#     for j in range(1, i + 1):
#         print(b, end=' ')
#     print()




# n = 4
# # upper triangle
# for i in range(n):
#     for j in range(i+1):
#         print(j, end="")
#     print()
# # lower triangle
# for i in range(n):
#     for j in range(n - i - 1):
#         print(j, end="")
#     print()

# wap for alphabet pyramid
'''n=5
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print(chr(64+j),end=" ")
    for k in range(1,i):
        print(chr(64+k),end = " ")
    print()'''
#wap for pasctal triangle
# '''n =5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(n-j,end="")#as we want to start with 4
#     print()
# for k in range(1,n+1):#for inverted traingle
#     for c in range(1,n+1-k):
#         print(n-c,end='')
#     print()'''

#table of any no
# n=int(input("enter any no"))
# for i in range(1,n+1):
#     print(i*n)

#pattern of rectangle for the range of 1-10
# n=5
# for i in range(1,n+1):
#     for j in range(1,11):
#         print(j,end="")
#     print()

# wap program for pattern
#ABCDE
#ABCDE
#ABCDE
#ABCDE
#ABCDE
# n= int(input("enter the no of rows"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(chr(64+j),end=" ")
#     print()

# WAp for pattern
# AAAAA
# BBBBB
# CCCCC
# n= int(input("enter the no of rows"))
# for i in range(1,n+1):
#     for j in range(1,n):
#         print(chr(64+i),end=" ")
#     print()

# ==========or======
# n= int(input("enter the no of rows"))
# for i in range(n):
#     print(chr(65+i)*n+" ")

# wap for pattern
# 4 3 2 1
# 5 4 3 2
# 6 5 4 3
# 7 6 5 4
# n= int(input("enter the no of rows"))
# for i in range(1,n+1):
#     for j in range(1,n):
#         print((n-j+i),end=" ")
#     print()

# wap for pattern
# 5 5 5 5 5 5
# 4 4 4 4 4 4
# 3 3 3 3 3 3
# 2 2 2 2 2 2
# 1 1 1 1 1 1
# 0 0 0 0 0 0

# n= int(input("enter the no of rows"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print((n-i),end=" ")
#     print()


# wap for these pattern
# E E E E
# D D D D
# C C C C
# B B B B
# A A A A
# n=5
# for i in range(1,n+1):
#     for j in range(1,n):
#         print(chr(70-i),end=" ")
#     print()
# =========or======
# n= int(input("enter no of rows"))
# for i in range(n):
#     print(chr(70-i)*n)


# wap forthese pattern
# E D C B A
# E D C B A
# E D C B A
# E D C B A
# E D C B A
# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(chr(70-j),end=" ")
#     print()

#wapfor these pattern
# 5 4 3 2 1
# 5 4 3 2 1
# 5 4 3 2 1
# n=5
# for i in range(1,n-1):
#     for j in range(1,n+1):
#         print((n-j+1),end=" ")
#     print()

# wap for the pattern
# A
# A B
# A B C
# A B C D
# A B C D E
# n= 5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(chr(64+j),end = " ")
#     print()

# wap for the following
# *
# * *
# * * *
# * * * *
# * * * * *

# n= 5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print ("*",end = " ")
#     print()


# # wap  forthe following
# 1
# 1 2
# 1 2 3 
# 1 2 3 4
# 1 2 3 4 5

# n=5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end = " ")
#     print()

 #wap for the following
#    *
#   * *
#  * * *
# * * * *

# n=4
# for i in range(1,n+1):
#     print(" "*(n-i),end="")
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()

# wap forthe following numeric pattern
# n= int(input("enter the no of rows"))
# for i in range(1,n+1):
#     print(" "*(n-i),end =" ")
#     for j in range(1,i+1):
#         print((i-j+1),end=" ")
#     print()
#      1
#     2 1
#    3 2 1
#   4 3 2 1
#  5 4 3 2 1

# wap forthe following numeric pattern
# n = int(input("enter the number  of rows "))
# for i in range(1,n+1):
#     print(" "*(n-i),end="")
#     for j in range(2*i-1,0,-1):
#         print(j,end="")
#     print()
#     1
#    321
#   54321
#  7654321
# 987654321 #here these series is starting from odd no and ending to end
# ----=-------=-=-=--=OR--=--==-=-=-=-=-=-=-===--=-=
# n = int(input("enter the number  of rows "))
# for i in range(1,n+1):
#     print(" "*(n-i),end="")
#     for j in range(1,i+1):
#         print(2*i-j,end="")
#     print()

# n = int(input("enter the number  of rows "))
# for i in range(1,n+1):
#     print(" "*(n-i),end="")
#     for j in range(1,i):
#         print(chr(64+(2*i-j)),end="")
#     print()


# wapfor the following pattern
#     A
#    ABC
#   ABCDE
#  ABCDEFG
# ABCDEFGHI
# n = 5
# for i in range(n):
#     for j in range(n - i - 1):
#         print(' ', end='')
#     for k in range(2 * i + 1):
#         print(chr(65 + k), end='')
#     print()

#     A
#    ABC
#   ABCCD
#  ABCDCDE
# ABCDECDEF
# n = 5
# for i in range(1,n+1):
#     print(" "* (n - i),end="")
#     for k in range(1,i+1):
#         print(chr(64 + k), end='')
#     for j in range(1,i):
#         print(chr(66+j), end='')
#     print()

# wap for the following:-
#     A
#    CBA
#   EDCBA
#  GFEDCBA
# IHGFEDCBA
# n = int(input("enter the number  of rows "))
# for i in range(1,n+1):
#     print(" "*(n-i),end="")
#     for j in range(2*i-1,0,-1):
#         print(chr(64+(j-i)),end="")
#     print()

# A
# AB
# ABC
# ABCD
# ABCDE
# ABC
# AB
# A
# n = int(input("enter the number  of rows "))
# for i in range(1, n + 1):
#     for j in range(1,i+1):
#         print(chr(64 + j), end="")
#     print()
# for c in range(1,n+1):
#     for k in range(n-c-1):
#         print(chr(65+k),end = "")
#     print()

#     A
#    ABC
#   ABCDE
#  ABCDEFG
# ABCDEFGHI
#
# n = int(input("enter the number  of rows "))
# for i in range(1,n+1):
#     print(" "*(n-i),end="")
#     for j in range(0,2 * i -1):
#         print(chr(65+j),end="")
#     print()
'''n = 5
for i in range(1,n+1):
    print(" "*(n-i),end=" ")
    for j in range(0,2*i-1):
            print(chr(65 + j), end=" ")
    print()'''

# n = 5
# for i in range(1,n+1):
#     print(" " * (n-i),str((chr(64+2*i-1)) * (2*i-1)) )
# print()

# n= int(input("enter the no of rows"))
# for i in range(1,n+1):
#     print(" "*(n-i),end =" ")
#     for j in range(2*i-1,0,-1):
#         print(str(chr(64+2*i-1)),end =" ")#as we cant pass more then 1 argument i chr so we converted to a string
#     print()

#      A
#    C C C
#   E E E E E
#  G G G G G G G
# I I I I I I I I I

#wap for the following
# n=int(input("enter no of rows "))
# for i in range(n):
#     print(" "*(n-i-1)+"* "*(i+1),end=" ")
#     print()
# for j in range(n-1):
#     print(" "*(j+1)+"* "*(n-j-1),end=" ")
#     print()

#     *
#    * *
#   * * *
#  * * * *
# * * * * *
#  * * * *
#   * * *
#    * *
#     *

#     1
#    1 2
#   1 2 3
#  1 2 3 4
# 1 2 3 4 5
#  2 3 4 5
#   3 4 5
#    4 5
#     5
'''
n=int(input("enter no of rows "))
for i in range(1,n+1):
    print(" "*(n-i), end=" ")
    for j in range(1,i+1):
        print("",j,end="")
    print()
for i in range(n):
    print(" "*(i+1),end=" ")
    for j in range(1,n-i):
        print('',j+i+1,end="")
    print()
'''
'''n=int(input("enter no of rows "))
for i in range(1,n+1):
    print(" "*(n-i), end=" ")
    for j in range(1,i+1):
        print('',chr(64+j),end="")
    print()
for i in range(n):
    print(" "*(i+1),end=" ")
    for j in range(1,n-i):
        print('',str(chr((64+j)+i+1)),end="")
    print()'''

  #      A
  #     A B
  #    A B C
  #   A B C D
  #  A B C D E
  # A B C D E F
  #  B C D E F
  #   C D E F
  #    D E F
  #     E F
  #      F

# wap for the following pattern \
# n=int(input("enter no of rows"))
# for i in range(n):
#     print((str(i+1)*(n-i)),end="")
#     print()
# 11111
# 2222
# 333
# 44
# 5

# n=int(input("enter no of rows"))
# for i in range(n):
#     print((str(chr(64+i+1))*(n-i)),end="")
#     print()
# AAAAA
# BBBB
# CCC
# DD
# E

# wap for the following
# n=int(input("enter no of rows"))
# for i in range(n):
#     print((str(n-i)*(n-i)),end="")
#     print()
# 55555
# 4444
# 333
# 22
# 1

# wap for the following
# n=int(input("enter no of rows"))
# for i in range(n):
#     print((str(chr(64+n-i))*(n-i)),end="")
#     print()
# EEEEE
# DDDD
# CCC
# BB
# A

# # wap for the folllowing
# n=int(input("enter no of rows "))
# for i in range(n):
#     for j in range(n-i):
#         print(chr(64+n-j),end="")
#     print()
# DCBA
# DCB
# DC
# D


# wap for the following
# 54321
# 5432
# 543
# 54
# 5
# n=int(input("enter no rows"))
# for i in range(n):
#     for j in range(n-i):
#         print(n-j,end="")
#     print()


# wap for the following
# n= int(input("enter no rows"))
# for i in range(n):
#     print(' '*(n-i-1),(str(i+1)+' ')*(i+1),end="")
#     print()
#
#       1
#      2 2
#     3 3 3
#    4 4 4 4
#   5 5 5 5 5
#  6 6 6 6 6 6

# n=int(input("enter the number of rows"))
# for i in range(n):
#     print(" "*(n-i),end=" ")
#     for j in range(i+1):
#         print(chr(64+n+j),end=" ")
#     print()
#       E
#      E F
#     E F G
#    E F G H
#   E F G H I

# # wap for
# n= int(input("enter no rows"))
# for i in range(n):
#     print(" "*(i),"* "*(n-i))
# * * * * * *
#  * * * * *
#   * * * *
#    * * *
#     * *
#      *

# wap for these pattern
# n= int(input("enter no rows"))
# for i in range(n):
#     print(" "*(i),(str(i+1)+" ")*(n-i))
#
#  1 1 1 1 1
#   2 2 2 2
#    3 3 3
#     4 4
#      5

# wap for these pattern
# n= int(input("enter no rows"))
# for i in range(n):
#     print(' '*i,end=" ")
#     for j in range(n-i):
#         print((str(j+1)+' '),end="")
#     print()
#  1 2 3 4 5
#   1 2 3 4
#    1 2 3
#     1 2
#      1

# wap for the following
# n= int(input("enter no rows"))
# for i in range(n):
#     print(' '*i,end=" ")
#     for j in range(n-i):
#         print((str(chr(64+j+1))+' '),end="")
#     print()
#
#  A B C D E
#   A B C D
#    A B C
#     A B
#      A


# n= int(input("enter no rows"))
# for i in range(n):
#     print(' '*i,end=" ")
#     for j in range(n-i):
#         print((str(n-i-j)+' '),end="")
#     print()
#  5 4 3 2 1
#   4 3 2 1
#    3 2 1
#     2 1
#      1


# wap for the following pattern
n= int(input("enter no rows"))
for i in range(n):
    print(' '*i,end=" ")
    for j in range(n-i):
        print((str(n-j)+' '),end="")
    print()
#
#  5 4 3 2 1
#   5 4 3 2
#    5 4 3
#     5 4
#      5

# wap for the following pattern:
# n=int(input("enter the following"))
# for i in range(n):
#     print(" "*(n-i-1),(str(i+1)+' ')*(i+1))
# for j in range(n-1):
#     print(" "*(j+1),(str(n-1-j)+' ')*(n-j-1))
 #      1
 #     2 2
 #    3 3 3
 #   4 4 4 4
 #  5 5 5 5 5
 # 6 6 6 6 6 6
 #  5 5 5 5 5
 #   4 4 4 4
 #    3 3 3
 #     2 2
 #      1