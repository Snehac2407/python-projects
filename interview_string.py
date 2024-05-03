# wap for checking weather a srt is palindrome or symmetric:-

# def palindrome(srt):
#     mid=(len(srt)-1//2)
#     start=0
#     end=len(srt)-1
#     flag=0
#     while start<=mid:
#         if (srt[start]==srt[end]):
#             start +=1
#             end -=1
#         else:
#             flag=1
#             break;
#     if flag==0:
#         print("srt is palindrome")
#     else:
#         print("srt IS is not palindrome ")

# def symmetric(srt):
#     half=int(len(srt)/2)
#     start=srt[:half]
#     end=srt[half:]
#     if start==end:
#         print("string is symmetric")
#     else:
#         print("not symmetric")

# str=palindrome("naveen")
# str=symmetric("naveen")
# print(str)


# wap to reverse a string :
# def reversed(string):
#     rev=string.split()[::-1]
#     l=[]
#     for i in rev:
#         l.append(i)
#         print("".join(l))
# strr=reversed("hye you")

# wap for removing the occurance of particular character:-
# test="snehaischoudhary"
# new_STRING=test.replace('s','')
# print("string after removing 's' from string", new_STRING)
# # for removing the first occurance of s
# new_str = test.replace('s', '', 1)
# print("string after removing 's' from string", new_str)

# wap for converting half stringin uppercase:-
# str="hye buddy how do you doing"
# half=len(str)/2
# result=str[:half]+str[half:].upper()
# print (str(result))

# wap for capitalising forst and last character of every string :-
# s = "welcome to geeksforgeeks"
# a = s.split()
# res = []
# for i in a:
#     x = i[0].upper()+i[1:-1]+i[-1].upper()
#     res.append(x)
# res = " ".join(res)
# print("String after:", res)

# wap to check in string weather has one alpha aur number:-
# def checkString(str):
#     flag_l = False
#     flag_n = False
#     for i in str:
#         if i.isalpha():
#             flag_l = True
#         if i.isdigit():
#             flag_n = True
#     return flag_l and flag_n
# print(checkString('thishasboth29'))
# print(checkString('geeksforgeeks'))

# wap to check weather the string has vowels or not:-
# def check(string):
#     if len(set(string.lower()).intersection("aeiou")) >= 5:
#         return ("all good")
#     else:
#         return ("nothing is good")
# check=check("areityou")
# print(check)
#

# wap program to check the similar char in two string:-
# def similarity(string1,string2):
#     return (len((set(string1)).intersection(set(string2))))
# string1="hyie buddy"
# string2="daddy hello"
# similar=similarity(string1.lower(),string2.lower())
# print(similar)

# wap for counting vowel in a string :_
# str="use of aueioufdgrs is a whole"
# vowel_r=set("aeiouAEIOU")
# count=0
# for alpha in str:
#     if alpha in vowel_r:
#         count+=1
# print("count of vowels  is ",count)

# wap to remove duplicates from a string :-
# 


# wap for least frequent charater of a string :-
# str="i am trying these program for the first time "
# frequent={}
# for i in str:
#     if  i in frequent:
#         frequent[i]+=1
#     else:
#         frequent[i]=1
# res = min(frequent, key = frequent.get) 
# print("hee is your desired result",res)


# wap for  Odd Frequency Characters
test_str = 'geekforgeeks is best for geeks'
x=set(test_str)
res=[]
for i in x:
    if(test_str.count(i)%2!=0):
        res.append(i)

print("The Odd Frequency Characters are : " + str(res))