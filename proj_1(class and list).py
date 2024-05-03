# class Movie:
#     def __init__(self,title,content,region):#inside constructor values are assigned
#         self.title=title
#         self.content =content
#         self.region = region
#     def info(self):
#         print("Title of movie",self.title)
#         print("movie is ", self.content)
#         print("these movie is from", self.region )
# movie_list = []
# while True:
#     title = input("enter movie name:-")
#     content = input("movie is:-")
#     region= input("movie is from:-")
#     m=Movie(title,content,region)
#     movie_list.append(m)
#     option =input("would you like add some more movies in your watchlist [y|n]")
#     if option.lower()=='n':
#         break
# print("something for your taste regards movies")
# print("."*60)
# for Movie in movie_list:
#     Movie.info()
#     print(" ")
#     print("_____ ___"*5)



import sys
class Customer:
    bankname = 'sneha bank'
    def __init__(self,name,balance=0.0):
        self.name = name
        self.balance = balance
    def deposite(self,amt):
        self.balance = self.balance + amt
        print('Balance after deposit: ',self.balance)
    def withdraw(self,amt):
        if  amt>self.balance :
            print("insufficent balnce...")
            sys.exit()
        self.balance = self.balance - amt
        print('Balance after withdrawl:',self.balance)

print("welcome to sneha bank",Customer.bankname)

name = input("enter your name")
c = Customer(name)

while True:
    print("d-Deposit \n w-Withdrawl \n e-Exit")
    option = input("Choose your option:")
    if option == 'd' or option == 'D':
        amt = float(input('enter amount'))
        c.deposite(amt)
    elif option == 'w' or option == 'W':
        amt = float(input('enter amount'))
        c.withdraw(amt)
    elif option == 'e' or option == 'E':
        print("Thanks Happy banking")
        sys.exit()
    else:
        print("invalid option")

