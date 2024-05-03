#wap for even filtering
'''num=[12,23,43,67,89,9,87,66,54,42]
even = (filter(lambda a:a%2==0,num))
for x in even:
    print(x)'''

# filter non vowels from a list
'''letters = ['a', 'b', 'd', 'e', 'p', 'j', 'i','s', 'o', 'r', 'u']
filter_non_vowels = filter(lambda a: a not in  ['a','e','i','o','u'],letters )
for non_vowel in filter_non_vowels:
    print(non_vowel)
'''
#insertion of two array
'''def insertion (arr1,arr2):
    result=list(filter(lambda x:x in arr1,arr2))
    print("insertion",result)
arr1=[12,21,2,3,43,34]
arr2=[21,3,4,34]
insertion(arr1,arr2)
# PALINDROME in the list
my_list = ["geeks", "naman", "keek", "madam", "aa"]
result = list(filter(lambda x: (x == "".join(reversed(x))), my_list))
print(result)'''

letters = ['a', 'b', 'd', 'e', 'p', 'j', 'i','s', 'o', 'r', 'u']
def vowels(letters):
    if letters in ['a','e','i''o','u']:
        return True
    else:
        return False
filter_vowels = list(filter(vowels,letters))
print(filter_vowels)
