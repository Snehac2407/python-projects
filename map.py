#sqare of no with map functioning
'''def square(number):
    return number ** 2
numbers = [1, 2, 3, 4, 5]
squared = list(map(square, numbers))
list(squared)
print(squared)'''
#square of number with mapand lambda functioning
'''numbers = (1, 2, 3, 4)
result = list(map(lambda x: x * x, numbers))
print(result)
# adding two list'''
'''numbers1 = [1, 2, 3,432,344]
numbers2 = [4, 5, 6,3,454]
result = map(lambda x, y: x + y, numbers1, numbers2)
print(list(result))'''

l = ['sat', 'bat', 'cat', 'mat']

# map() can listify the list of strings individually
'''test = tuple(map(list, l))
print(test)'''

''''#dicitonaries  different inputs as a list
str ={}
n = int(input("how many following details are required  "))
for i in range (n):
    name = input("enter name:")
    rollno=int(input("enter age "))
    str[name]= rollno
LIST = str
list1=list(LIST.items())
print(list1)
test1 = tuple(map(list, list1))
print(test1)'''

#findeven ina list and doublethe even
'''def even (num):
        if num%2==0:
          return num * 2
        else:
          return num
number=[12,32,34,33,55,53,31,13,31]
test1 = list(map(even,number))
print(test1)'''

#sum of array
'''def findSum(arr):
    return sum(map(sum, arr))
arr = [[1, 2, 3], [4, 5, 6], [2, 1, 2]]
print(arr)
print("Sum = ", findSum(arr))'''

#calculate square of a array
'''def calculateSquare(n):
    return n*n
# numbers is a list of elements
numbers = [1, 2, 3, 4]
result = map(calculateSquare, numbers)
print(result)
set_result = set(result)
print(set_result)'''

#sum of ascii value ofthe given sentence
def asciiSums(sentence):
    words = sentence.split(' ')
    result = {}
    for i in words:
        Sum = sum(map(ord, i))
        result[i] = Sum
    sumsOfAscii = [result[i] for i in words]
    print(' '.join(map(str, sumsOfAscii)))
    print(sum(sumsOfAscii))#the sum 
sentence = 'I am a geek'
asciiSums(sentence)

