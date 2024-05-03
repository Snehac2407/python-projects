'''# initializing string
str = "i am doing coding"
print("The original string is : " + str)  # printing original string
index= [1, 3, 4, 5, 7] # initializing index list
#Get positional characters from String
res = ''
for i in range(0,len(str)):# Get positional characters from String # using loop
    if i in index:
        res +=str[i]
# printing result
print("Substring of selective characters : " + res)'''

str = "i am doing coding"
print("The original string is : " + str)  # printing original string
index= [1, 3, 4, 5, 7]
res =''
while(len(str)>=0):
    if index in range(len(str)):
        res = res+index
print("Substring of selective characters : " + res)