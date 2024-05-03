num=int(input("enter numbers of rows:-"))
for i in range(num,0,-1):# responsible for rows
    for j in range(0,num-i):#responsible for coloums
        print()
    for j in range(0,i): # increment i value
         print("*",end ='')
print()