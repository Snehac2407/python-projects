# '''s1 = "sneha"
# s2 = "choudhary"

# s1 = "raja"
# s2 = "rani"
s1=input("enter any string")
s2=input("enter any string")
output  = ''
i = 0#storing index of string1
j = 0#storing index of string2
while i < len(s1) or j<len(s2):
    if  i < len(s1):
        output = output + s1[i]
        i = i+1
    if j < len(s2):
        output = output + s2[j]
        j = j+1

print(output)


'''s = "major"
t = "general"
i = j = 0
result = ""
while i < len(s) and j < len(t):
      result += s[i] + t[j]
      i+=1
      j+=1
while i < len(s):
      result += s[i]
      i += 1
while j < len(t):
      result += t[j]
      j += 1
print(result)'''



