# 1.# a file named "trail", will be opened with the reading mode.
# file = open('trail.txt', 'r')
# # This will print every line one by one in the file
# for each in file:
#      print(each)
# file.close()
#
#
# 2.# we can do these by theseb also
# file = open("trail.txt", "r")
# print (file.read())
# file.close()
# print('is file closed->',file.closed)
#
# 3.# now we can do these with 'with' statement
# with open("trail.txt") as file:
#     data = file.read()
# print(data)
#
# # operation on files
# f = open("trailtxt",'w')
# print('file name->',f.name)
# print('file mode->',f.mode)
# print('file readable->',f.readable())#to know weather fileis readabler not
# print('file writable->',f.writable())#to know weather fileis writable not
# print('is file closed->',f.closed)
# f.close()
# print('is file closed->',f.closed)#now fileis closed
#
# f = open("trail.txt",'w')
# f.write("hii its me sneha..\n")
# f.write("okay i dont mind that you dont know me\n ")
# f.writelines("but you must have know me its okay just remember me from now onwards...\n")
# print(f)
# # print("data written successfully")
# f.close()
# print("is file is closed ",f.closed)
#
# # WAP FOR COUNTING NO OF WORDS ,LINES in the given file
# file = open("trail.txt", "r")
# word = 0;char = 0;lines=0
# for line in file:
#    lines += 1  #for incraing lines
#    line = line.strip("\n")# for removing ending space char
#    l= line.split()#for counting each word
#    word += len(l)
#    char += len(line)
# file.close()
# print("no of words are",word)
# print("no of char are",char)
# print("no of lines are",lines)
#
# #WAP for checking wheather the file exist or not
# import os.path
# print(os.path.exists('trail.txt'))
# if os.path.exists:
#    with open("trail.txt") as file:
#       data = file.read()
#    print(data)
# else :
#    print(none)
#
# #WAP for checking wheather the file exist or not
# import os.path
# print(os.path.exists("ypp.txt"))
# if os.path.exists:
#    with open("ypp.txt") as file:
#       data = file.read()
#    print(data)
# else:
#    print(none)
#
# # tell methood
# f = open("trail.txt",'r')
# print(f.tell())
# print(f.read(45))#index at which cursor will
# print(f.tell())
#
#
#
# with open("trail.txt","r+") as f:
#     text = f.read()
#     print(text)
#     print("The current position :",f.tell())
#     f.seek(55)
#     print("The current position :",f.tell())
#     f.write("gem.")
#     f.seek(0)
#     text = f.read()
#     print("after modificaiton")
#     print(text


# CREATING A CSV FILE
# import csv
# with open("emp.csv","w",newline='') as f:
#     w = csv.writer(f)
#     w.writerow(["ENO","ENAME","ESAL","EADDR"])
#     n = int(input("enter number of employess: -"))
#     for i in range(n):
#         eno = input("enter employee no:-")
#         ename = input("enter employee name:-")
#         esal = input("enter employee sal:-")
#         eaddr = input("enter employee address:-")
#         w.writerow([eno,ename,esal,eaddr])
# print("data written success fully")

# reading data from csv
# import csv
# f = open("emp.csv",'r')
# r= csv.reader(f) #returns csv reader object
# data = list(r)
# print(data)
# for line in data:
#     for word in line:
#         print(word,"\t",end="")
#     print()

# zipfiles
# from zipfile import *
# # to create zip file
# f = ZipFile("files.zip",'w',ZIP_DEFLATED)
# f.write("trail.txt")
# f.write("emp.csv")
# # f.write("test.sql")
# f.close()
# print(f)

from zipfile import *
f = ZipFile("files.zip",'r',ZIP_STORED)
names = f.namelist()
print(names,"dfsd")
for name in names:
    print("trail.txt",name)
    print("the content of the file is:-")
    f1 = open(name,'r')
    print(f1.read())
    print()

import os
# # cwd = os.getcwd()
# # print(cwd)
# path = "C:\\sampledirectory"
# os.chdir(path)
# for i in range(1,5):
#     new_folder = "directory1"+str(i)
#     os.makedirs(new_folder)


import os
stats = os.stat("trail.txt")
print(stats)