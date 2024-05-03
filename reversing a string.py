'''s= "sneha is trying to code by herself"
str =''
for i in s:
    str = i + str
print(str)'''


s = "Learning python is very easy"

l = s.split()
l1 = []
i = len(l) - 1

while i >= 0:
    l1.append(l[i])
    i = i - 1

output = ''
i = 0

while i < len(l1):
    output += l1[i]
    if i < len(l1) - 1:
        output += ' '
    i += 1

print(output)



'''s = input("enter string:-")
#print(s[::-1])
l =len(s)-1
target = ''
while l>=0:
     target = target + s[l]
     l -=1
print(target)'''

#print("---------------^^^^^^-----------------")

'''s = "Learning python is very easy"
print(s)
l = s.split()
l1 = []
i = len(l) - 1
while i >= 0:
    l1.append(l[i])
    i = i - 1
print(l1)
i = 0
output = ''
while i < len(l1):
    output = output + l1[i] +' '
    #if i < len(l1) - 1:
        #output += ' '
    i = i + 1
print(output)'''


#print("---------------^^^^^^-----------------")


'''s=input("enter a string")
for i in s[::-1]:
    print(i,end='')
print(''.join(reversed(s)))
s = input("enter string:-")
print(s[::-1])
l =len(s)-1
target = ''
while l>=0:
    target = target + s[l]
    l = l-1
print(target)
print(''.join(reversed(s)))'''

#print("---------------^^^^^^-----------------")


'''s = "Learning python is very easy"

l = s.split()

l1 = []
i = len(l)-1
# print(i)
# print(l)

while i > 0:
    l1.append(l[i])
    i = i-1
# print(''.join(l1))
k = len(l1)
i = 0 
output = '' 
while  i <= k:
     output = output + l1[i] + ' '
     i = i+1
print(output)

l = "learning python is easy"
i = len(l) - 1
word = ""
output = ""

while i >= 0:
    if l[i] != ' ':
        word = l[i] + word
    else:
        output += word + ' '
        word = ""
    i -= 1

output += word  # Append the last word (no trailing space)

print(output)'''
