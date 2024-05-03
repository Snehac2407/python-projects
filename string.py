#wap for given input as "A1B2C3" a stribg and ABC123as output
'''
s = "A1B2C3"
s1 = s2 = output = ''
for x in s:
    if x.isalpha():
        s1 = s1 + x
    else:
        s2 = s2 + x
for x in sorted(s1):
    output = output + x
for x in sorted(s2):
    output = output + x
print(output)
'''

# s =  "A1B2C3"
# output = ''
# for x in s:
#     if x.isalpha():
#         output = output + x
#         previous = x
#     else:
#         output = output + previous * (int(x)-1)
# print(output)

#ASCII char of a string
'''s = "a6"
output = ''
for x in s:
    if x.isalpha():
        output  = output + x
        previous = x
    else :
        output  = output  + chr(ord(previous) + int(x))
print(output)'''

# repetion of each char in a string
#
# s =  "ABCDABBCDABBBCCCCDDDEEEE"
# d = {}
# for x in s:
#     if x in d.keys():
#         d[x] = d[x] + 1
#     else:
#         d[x] = 1
# print(d)
# # for k,v in d.items():
#     print("{}={} Times ".format(k,v))

# 1).Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
# Sample String : 'restart'
# Expected Result : 'resta$t'
# str="restart"
# print("String :",str)
# char = str[0]
# str = str.replace(char, '@')
# str = char + str[1:]
# print("After String :",str)

# Algo: count  number of e in the string.
# s = "Some text"
# cnt = 0
# for c in s:
#  if c == "e":
#     cnt = cnt + 1
# print("found",cnt,"'e'")


#
# pswd = input("enter password ")
#
# if(len(pswd) >= 8 and len(pswd) <= 15):
#     if pswd.isalnum():
#         print("Good password!")
#     else:
#         print("Password should contain alpha numeric characters!")
#
# else:
#     print("Password length should be in range [8-15]")
#

# def isPalindrome(s):
# 	return s == s[::-1]
#
#
# # Driver code
# s = "malayalam"
# ans = isPalindrome(s)
#
# if ans:
# 	print("Yes")
# else:
# 	print("No")

#   count no of vowels in  string
# string=raw_input("Enter string:")
# vowels=0
# for i in string:
#       if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
#             vowels=vowels+1
# print("Number of vowels are:")
# print(vowels)
# #
# # convert upper to lower and lower to upper
# str1 = "Great Power";
# newStr = "";
# for i in range(0, len(str1)):
#     if str1[i].islower():
#         newStr += str1[i].upper();
#     elif str1[i].isupper():
#         newStr += str1[i].lower();
#     else:
#         newStr += str1[i];
# print("String after case conversion : " + newStr);
# w = "Python Programinf"
# wo = " "
# for i in range(len(w)):
#     if i%2==0:
#         wo += w[i].lower();
#     else :
#        wo += w[i].upper();
# print(wo)

# c =-10
# while c<15:
#     print(c)
#     c+=3
#
# count no of char in string
# s=input("enter any string")
# count=0
# for i in s:
#     count+=1
# print(count)

# wapfor prinintingstring character present at even index
'''str=input("enter any string")
l=len(str)
for i in range(0,l-1,2):
    print("char at even no are",str[i])'''


#=====or by list=====
# str = input("enter any string")
# LIST=list(str)
# for i in LIST[0::2]:
#     print(i)

# wap for removing first n char from a string
# str=input("enter any string")
# n=int(input("enter char which you want to remove from begning "))
# l=len(str)
# for i in range(n,l):
#     print("char at even no are",str[i])

# wap for creating a new string from the existing string that include 1st,mid and last char of the given string
# str =input("enter anystring")
# result=str[0]
# l=len(str)
# mid=int(l/2)
# result=result+str[mid]
# result=result+str[l-1]
# print(result)

# wap for excessing middle 3 elements from a string
'''str=input("enter any string")
mid=int(len(str)/2)
result=str[mid-1:mid+2]
print(result)
'''
# : Append new string in the middle of a given string
# str=input("enter the given string")
# str2=input("enter any string ")
# mid=int(len(str)/2)
# str3=str[:mid:]
# str3=str3+str2 # for exceesing values before middle  element
# str3=str3+str[mid:]
# print(str3)
# def logarithm(n):
#     i = 1
#     while i <= n :
#         i = i * 2
#         print(i)
# logarithm(100)


# Arrange string characters such that lowercase letters should come first
# str=input("enter the number ")
# lower =[]
# upper=[]
# for i in str:
#     if i.islower():
#         lower.append(i)
#     else:
#         upper.append(i)
# sorted = ''.join(lower+upper)
# print(sorted)


# str=input("enter the number ")
# digit =0
# number=0
# special=0
# for i in str:
#     if i.isalpha():
#         digit+=1
#     elif i.isalnum():
#         number+=1
#     else:
#         special+=1
# print("the countingof the foolowing is as",digit,"\n",number,"\n",special)

# wap a mix of two string one in ascending orderand other in descending
# s1=input("enterany string")
# s2=input("enterany  sub string")
# index=s1.rfind(s2)
# print(index)













'''capitalize():-	Converts the first character of the string to a capital (uppercase) letter
casefold()	Implements caseless string matching
center()	Pad the string with the specified character.
count()	Returns the number of occurrences of a substring in the string.
encode()	Encodes strings with the specified encoded scheme
endswith()	Returns “True” if a string ends with the given suffix
expandtabs()	Specifies the amount of space to be substituted with the “\t” symbol in the string
find()	Returns the lowest index of the substring if it is found
format()	Formats the string for printing it to console
format_map()	Formats specified values in a string using a dictionary
index()	Returns the position of the first occurrence of a substring in a string
isalnum()	Checks whether all the characters in a given string is alphanumeric or not
isalpha()	Returns “True” if all characters in the string are alphabets
isdecimal()	Returns true if all characters in a string are decimal
isdigit()	Returns “True” if all characters in the string are digits
isidentifier()	Check whether a string is a valid identifier or not
islower()	Checks if all characters in the string are lowercase
isnumeric()	Returns “True” if all characters in the string are numeric characters
isprintable()	Returns “True” if all characters in the string are printable or the string is empty
isspace()	Returns “True” if all characters in the string are whitespace characters
istitle()	Returns “True” if the string is a title cased string
isupper()	Checks if all characters in the string are uppercase
join()	Returns a concatenated String
ljust()	Left aligns the string according to the width specified
lower()	Converts all uppercase characters in a string into lowercase
lstrip()	Returns the string with leading characters removed
maketrans()	 Returns a translation table
partition()	Splits the string at the first occurrence of the separator 
replace()	Replaces all occurrences of a substring with another substring
rfind()	Returns the highest index of the substring
rindex()	Returns the highest index of the substring inside the string
rjust()	Right aligns the string according to the width specified
rpartition()	Split the given string into three parts
rsplit()	Split the string from the right by the specified separator
rstrip()	Removes trailing characters
splitlines()	Split the lines at line boundaries
startswith()	Returns “True” if a string starts with the given prefix
strip()	Returns the string with both leading and trailing characters
swapcase()	Converts all uppercase characters to lowercase and vice versa
title()	Convert string to title case
translate()	Modify string according to given translation mappings
upper()	Converts all lowercase characters in a string into uppercase
zfill()	Returns a copy of the string with ‘0’ characters padded to the left side of the string'''



s = 'what is multi threading and multitasking'
l = s.split()
word = [i [::-1] for i in l]
string = ' '.join(word)
print(string)


