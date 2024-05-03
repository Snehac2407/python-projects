# def division(func):
#     def inner(x,y):
#         if y==0:
#             print("give proper input")
#         else:
#             return func(x,y)
#     return inner
# @division
# def div(a,b):
#     return a/b
# print(div(12,34))


def wish(name):
    print("Hello good morning",name)
wish('sneha')
wish('ankush')
wish('deepika')

# but we want to modify this fucntion to provide different message if name is sunil
# we can do this without touching wish()
def decor(func):
    name =input("enter yourname ")
    def inner(name):
        if name != 'sneha' and"ankush"and"deepika":
            print("Hello  bad morning")
        else:
            func(name)
    return inner

@decor
def wish(name):
    print("Hello ",name,"good morning")
wish("sneha")
wish("name")