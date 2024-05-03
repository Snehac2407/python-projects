d ={}
d = {
    50:"test"
}
print(d)
# key:value
d[100] = 'sneha'
d[200] = 'choudhary'
if 100 in d:
    print(d[100])

#user input in dicitionary
'''rec = {}
n = int(input("enter number of students:"))
i = 0
while i <=n:
    name = input("ente name:")
    marks = input("enter marks:")
    rec[name] = marks
    i = i+1
print(rec)'''


d = "mississippi"
s= {}
for x in d:
    s[x] = s.get(x,0) + 1
for k,v in s.items():
    print(k , "came" ,v,"times")