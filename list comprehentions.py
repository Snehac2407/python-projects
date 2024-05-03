# traditional  approch
'''n= [23,45,6756]
result =[]
for i in n:
    i=i*2
    print(i)
    result.append(i)
print(n)'''
# COMPREHENTION APPROCH
'''n=[23,45,6756]
result=[i * 3 for i in n]
print(result)
'''
# string comprenstion

'''s=("hye here you go ")
result=[i.upper()for i in s ]
print(result)'''

#function for multipling string
'''n = [23,34,45,7,78]
print(n)
def times(n):
    return n*6
results=[]
results=[times(i) for i in n]
print(results)'''

#comprhenstion for dictionary:-
dict={"name":"sneha"},{"name":"choudhary"}
result={ }
results=[i['name'] for i in dict]
print(results)

#comprehenstion with if/else in list
l=[2,3,4,5,6,7]
result =[]
#result=[i for i in l]
#print(result)
#result=[i*5 if i ==5 else i for i in l]
#print(result)
#result=[i*5 if i >=5 else i for i in l]
#print(result)
#result=[i  for i in l if i >=5 ]
#print(result)
result=[i*5 if i ==2 else i for i in l if i >=5 ]
print(result)

# square of list
x = [1,3,5,7,9]
sum_squared = sum([y**2 for y in x])
print(sum_squared)