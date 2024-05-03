#converting adictionary to list
'''stCAP={}
n = int(input("how many capital you want to store:"))
for i in range (n):
    st = input("enter state:")
    cap=input("enter capital ")
    stCAP[st]= cap
inputDictionary=stCAP
List = list(inputDictionary.items())   # printing the resultant list of a dictionary
print(List)'''


info={}
n = int(input("how many following details are required  "))
for i in range (n):
    name = input("enter name:")
    age=int(input("enter age "))
    info[name]= age
print("name with their ages")
print(info)
inputDictionary=info
List = list(inputDictionary.items())   # printing the resultant list of a dictionary
print(List)
print(sorted(List, key=lambda x: x['age'])
print("\r")
print("The list printed sorting by age and name: ")
print(sorted(List, key=lambda x: (x['age'], x['name'])))
print("\r")
print(sorted(List, key=lambda x: x['age'], reverse=True))


# Python code demonstrate the working of
# sorted() with lambda

# Initializing list of dictionaries
list = [{"name": "Nandini", "age": 20},
	{"name": "Manjeet", "age": 20},
	{"name": "Nikhil", "age": 19}]

# using sorted and lambda to print list sorted
# by age
print("The list printed sorting by age: ")
print(sorted(list, key=lambda i: i['age']))
# using sorted and lambda to print list sorted
# by both age and name. Notice that "Manjeet"
# now comes before "Nandini"
print("The list printed sorting by age and name: ")
print(sorted(list, key=lambda i: (i['age'], i['name'])))


# using sorted and lambda to print list sorted
# by age in descending order
print("The list printed sorting by age in descending order: ")
print(sorted(list, key=lambda i: i['age'], reverse=True))
