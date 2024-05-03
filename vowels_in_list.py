st=input("Enter Any String ")
output=""
vowels=0
for i in st:
     if (i=='a'or i=='e'or i=='i'or i=='o'or  i=='u'):
        output+=i
vowels = vowels + 1

print(output)