'''string = input("enter any string:-")
half = int(len(string) / 2)

F_STR = string[:half]
S_STR = string[half:]

if F_STR == S_STR :
    print(string, 'string is symmetrical')
else:
    print(string, 'string is not symmetrical')

# palindrome
if F_STR == S_STR[::-1]:  # ''.join(reversed(second_str))
    print(string, 'string is palindrome')
else:
    print(string, 'string is not palindrome')'''
string = input("enter any string")
half = int(len(string) / 2)

first_str = string[:half]
second_str = string[half:]

# symmetric
if first_str == second_str:
    print(string, 'string is symmetrical')
else:
    print(string, 'string is not symmetrical')

# palindrome
if first_str == second_str[::-1]:  # ''.join(reversed(second_str)) [slower]
    print(string, 'string is palindrome')
else:
    print(string, 'string is not palindrome')