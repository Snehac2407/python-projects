# write a program to find the number of  occurences of each character
s =  "ABCDABBCDABBBCCCCDDDEEEE"
d = {}
for x in s:
    if x in d.keys():
        d[x] = d[x] + 1
    else:
        d[x] = 1
#print(d)
for k,v in d.items():
   print("{}={} Times ".format(k,v))

'''str = input("enter any string:")
a = {}
for i in str:
    if i in a:
        a[i] += 1
    else:
        a[i] = 1
print(str,(a))'''


'''str=input("Enter the String:")
char=input("Enter the Character:")
strLen = len(str)
sum = 0
for i in str:
    if char==i:
        sum = sum+1
print("\nOccurrence of Given Character is:")
print(sum)'''

