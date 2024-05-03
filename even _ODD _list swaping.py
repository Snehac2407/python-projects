val=[12,23,34,54,3,2]
'''a = input("enter element of list")
for i in a:
    val.append(a)'''
print(val)
s=len(val)
if s%2!=0:
    s=s-1
    print(s)
for i in range(0,s,2):
    val[i],val[i+1]=val[i+1],val[i]
print("List after swapping :",val)
