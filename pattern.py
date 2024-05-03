'''n=5
for i in range(0,n):
    for j in range(0,i+1):
        print("*",end ='')#By default, the print function ends with a newline. Passing the whitespace to the end parameter (end=' ') indicates that the end character has to be identified by whitespace and not a newline.
    print()
'''
'''n=5;i=0
while i<n:
    j=i+1 #formula for increasing rows
    while j > 0:
       print("*", end ="")
       j = j -1
    i = i +1
    print() '''
def pypart(n):
    myList = []
    for i in range(0,n+1):
        myList.append("*" * i )
    print("\n".join(myList))
n = 5
pypart(n)