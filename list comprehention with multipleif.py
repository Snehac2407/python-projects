fruits=input("enter fruits name")
print(fruits)
y =fruits.split()
print(y)

num =[1,2,3,4,5,6,7]
result =[i for i in num if i>1  if i!=3]
print(result)
result =[(i,f) for i in num if i!=3  for f in fruits ]
print(result)

'''for i in num:
    i!=3 and i>=3
    for j in fruits:
        print(i,j)'''


