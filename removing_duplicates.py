'''s = input("enter any string that is having duplicates")
l = []
for x in s:
    if x not in l: # here
        l.append(x)
output = ''.join(l)
print(output)'''

s = input("enter any string that is having duplicates")
l = ''
i=0
for x in s:
     if s.index(x)==i:
         l+=x # here we are appendingvalue of each upcoming character of the string s in l so the character get addedin l 
     i+=1 # here we are increasing i value  sol indexget increases 
print(l)
