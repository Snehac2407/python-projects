l = [1,2,3,4,5,6,6,7,8,89]
l= lambda x: x*x
[l(x) for x in range(10)]
print(l)


squares = []
for x in range(1,10,3): squares.append(x*x)
print(squares)

#single argument multiplication

x = lambda a : a * 10
print(x(5))

#two argument multiplication
x = lambda a, b : a * b
print(x(5, 6))

#LAMBDA WITHIN FUNCTION
def myfunc(n):
  return lambda a : a * n
n= myfunc(2)
print(n(456))


def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2)
print(mydoubler(11))

def myfunc(n):
  return lambda a : a * n
mytripler = myfunc(3)
print(mytripler(11))

def myfunc(n):
    return lambda a : a /n
divider = myfunc(3)
print(divider(11))

# Lambda function with if-else
square = lambda x: x * x if (x > 0) else x
print(square(23))

#MAXIMUM AMOng two n0:-
max = lambda a,b: a if (a>b) else b
print(max(10,2))
print(max(34,45))

# even and odd using lambda
result = lambda x: f"{x} is even" if x % 2 == 0 else f"{x} is odd"
print(result(12))
print(result(11))

#greatest among two:-
result = lambda x, y: f"{x} is smaller than {y}" \
    if x < y else (f"{x} is greater than {y}" if x > y \
                       else f"{x} is equal to {y}")

# print for numbers
print(result(12, 11))
print(result(12, 12))
print(result(12, 13))