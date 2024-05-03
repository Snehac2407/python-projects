# implement a stack using array :-
'''
class Stack:
    def __init__(self, limit=4):
        self.limit = limit
        self.stack = [ ] * limit
        self.top = 0
    def is_empty(self):
        return len(self.stack) == 0
    def push(self, item):
        if self.top == self.limit :
            print("stack is overflow")
            return
        self.top += 1
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            print("Stack is empty. Cannot peek.")
            return None
    def size(self):
        return len(self.stack)
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(23)
stack.push(3)
# stack.push(3)
print("Stack:", stack.stack)
print("Peek:", stack.peek())
print("Pop:", stack.pop())
print("Stack:after pop ", stack.stack)
print("Is Empty?", stack.is_empty())
print("Stack Size:", stack.size())'''

 # implement a stack using dynamic array :-
# class Stack:
#     def __init__(self, limit=4):
#         self.limit = limit
#         self.stack = [ ] * limit
#         self.top = 0
#     def is_empty(self):
#         return len(self.stack) == 0
#     def push(self, item):
#         if len(self.stack) >= self.limit:
#             self.resize()
#         self.stack.append(item)
#     def resize(self):
#         new_stack=(self.stack)
#         self.limit = 2*(self.limit)
#         self.stack=new_stack
#
#     def pop(self):
#         if not self.is_empty():
#             return self.stack.pop()
#         else:
#             return None
#     def peek(self):
#         if not self.is_empty():
#             return self.stack[-1]
#         else:
#             print("Stack is empty. Cannot peek.")
#             return None
#     def size(self):
#         return len(self.stack)
# stack = Stack()
# stack.push(1)
# stack.push(2)
# stack.push(3)
# stack.push(23)
# stack.push(3)
# # stack.push(3)
# print("Stack:", stack.stack)
# print("Peek:", stack.peek())
# print("Pop:", stack.pop())
# print("Stack:after pop ", stack.stack)
# print("Is Empty?", stack.is_empty())
# print("Stack Size:", stack.size())

# implement a stack by linkedlist:-
# class Node():
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class Linkedlist():
#     def __init__(self):
#         self.head = None
#     def is_empty(self):
#         if self.head == None:
#             return True
#         else:
#             return False
#     def push(self,data):
#         if self.head==None:
#             self.head=None(data)
#         else:
#             new_node=Node(data)
#             new_node.next=self.head
#             new_node = self.head
#     def pop (self):
#         if self.is_empty():
#             return None
#         else:
#             pop_node=self.head
#             self.head=self.head.next
#             pop_node.next=None
#             return pop_node.data
#     def printList(self):
#         temp = self.head
#     	while temp != None:
#             print(temp.data, end="-->")
#     		temp = temp.next

# wap for reversing a stack element :-
# class Stack:
#     def __init__(self):
#         self.items = []
#     def is_empty(self):
#         return self.items == []
#     def push(self, data):
#         self.items.append(data)
#     def pop(self):
#         return self.items.pop()
#     def display(self):
#         for data in reversed(self.items):
#             print(data)
# def insert_at_bottom(s, data):
#     if s.is_empty():
#         s.push(data)
#     else:
#         popped = s.pop()
#         insert_at_bottom(s, data)
#         s.push(popped)
# def reverse_stack(s):
#     if not s.is_empty():
#         popped = s.pop()
#         reverse_stack(s)
#         insert_at_bottom(s, popped)
# s = Stack()
# elements= input('Please enter the elements to push: ').split()
# for data in elements:
#     s.push((data))
# print('The stack:')
# s.display()
# reverse_stack(s)
# print('After reversing:')
# s.display()


# def reverse_stack(user_input):
#     stack = []
#     for data in user_input:
#         stack.append(data)
#     rev = ''
#     while len(stack) > 0:
#         last = stack.pop()
#         rev = rev + last
#         print(last)
#     return rev
# a= input('What is your number:').split(',')
# reverse = reverse_stack(a)
# print('Reversed is: ', reverse)

# wap a python program for checking weather the given input string is palindrome  or not :-
# stack =[]
# def push(stack, data):
#      stack.append(data)
# def pop(stack):
#     return stack.pop()
# def is_palindrome(str,stack):
#     i=0
#     mid=len(str)/2
#     flag=1
#     while(i<mid):
#         push(stack,str[i])
#         i=i+1
#     if len(str)%2 !=0:
#         i=i+1
#     while i<len(str):
#         popped_char=pop(stack)
#         if popped_char != str[i]:
#             flag=0
#             break
#         i=i+1
#
#     if flag==1:
#         print("string is palindrome")
#     else:
#         print("string is not palindrome")
# def user_input(str):
#     str=input("enter the string")
#     print(str)
#     return str
# string=user_input(str)
# is_palindrome(string,stack)

# wap for creatng two stack from a array:
# class stack():
#     def __init__(self,n):
#         self.size=n
#         self.arr=[None]*n
#         self.top1=-1
#         self.top2=self.size
#     def push1(self,data):
#         if self.top1<self.top2-1:
#             self.top1=self.top1+1
#             self.arr[self.top1]=data
#         else:
#             print("stack is overflow")
#     def push2(self,data):
#         if self.top1<self.top2-1:
#             self.top2=self.top2-1
#             self.arr[self.top2]=data
#         else:
#             print("stack is overflow")
#     def pop1(self):
#         if self.top1>=0:
#             data=self.arr[self.top1]
#             self.top1=self.top1 -1
#             return data
#         else:
#             print("stack underflow")
#     def pop2(self):
#         if self.top2<self.size:
#             data=self.arr[self.top2]
#             self.top2=self.top2 +1
#             return data
#         else:
#             print("stack underflow")
#
# two_stack=stack(5)
# two_stack.push1(52)
# two_stack.push1(46)
# two_stack.push2(54)
# two_stack.push2(56)
# two_stack.push2(34)
# print("Popped element from stack1 is " + str(two_stack.pop1()))
# two_stack.push2(40)
# print("Popped element from stack2 is " + str(two_stack.pop2()))


# wap for the following:-
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
# class LinkedList:
#     def __init__(self):
#         self.head = None
#     def add(self, new_data):
#         new_node = Node(new_data)
#         new_node.next = self.head
#         self.head = new_node
#     def printList(self):
#         temp = self.head
#         while(temp):
#             print (temp.data,end="-->")
#             temp = temp.next
#     def add(self, new_data):
#         new_node = Node(new_data)
#         new_node.next = self.head
#         self.head = new_node
#
#     def reorderList(self,head):
#         if head is None:
#             return head
#         stack = []
#         temp = head
#         while temp is not None:
#             stack.append(temp)
#             temp = temp.next
#         list  = head
#         fromHead = head
#         fromStack =  True
#         while fromStack and list is not stack[-1] or  not fromStack and list!=fromHead:
#             if fromStack:
#                 fromHead = fromHead.next
#                 list.next = stack.pop()
#                 fromStack = False
#             else:
#                 list.next = fromHead
#                 fromStack = True
#             list = list.next
#         list.next = None
# l= LinkedList()
# for i in range(0,10):
#     l.add(i)
# l.printList()
# head=self.head
# l.reorderList(head)


# wap for removing anadjacent element from the string using stack :-
# def remove_adjacent_duplicates(string):
#     stack = []
#     for char in string:
#         if stack and char is stack[-1]:
#             stack.pop()
#         else:
#             stack.append(char)
#     return ''.join(stack)
# string1 = "abbcdcb"
# print(remove_adjacent_duplicates(string1))

# wap to check blancing of parenthesis using stack:-
# def checking_balance(parenthesis):
#     stack=[]
#     for i in parenthesis:
#         if i in ["(","{","["]:
#             stack.append(i)
#         else:
#             if not stack:
#                 return False
#             top_element=stack.pop()
#             if top_element=="(":
#                 if i != ")":
#                     return False
#             if top_element=="[":
#                 if i != "]":
#                     return False
#             if top_element=="{":
#                 if i != "}":
#                     return False
#     if stack:
#         return False
#     return True
# parenthesis="({}])"
# if checking_balance(parenthesis):
#     print("the given string is balanced")
# else:
#     print("the given string is unbalanced")



# wap to check next gereatest element:-
# def createstack():
#     stack=[]
#     return stack
# def is_empty(stack):
#     return len(stack)==0
# def push(stack,data):
#     stack.append(data)
# def pop(stack):
#     if is_empty(stack):
#         print("stack is underflow")
#     else:
#         return stack.pop()
# def next_greatest_element(array):
#     s=createstack()
#     current=0
#     next=0
#     push(s,array[0])
#     for i in range(1,len(array)):
#         next=array[i]
#         if is_empty(s)==False:
#             current=pop(s)
#             while current<next:
#                 print(str(current)+"--"+str(next))
#                 if is_empty(s)==True:
#                     break
#                 current=pop()
#             if current>next:
#                 push(s,current)
#         push(s,next)
#     while is_empty(s)==False:
#         current=pop(s)
#         next=-1
#         print(str(current) + "--" + str(next))
# array=[12,32,34,54,56,65,6]
# next_greatest_element(array)
#

# wap for converting a postfix expression in prefix using stack:-
# def is_operand(x):
#     if x=='+':
#         return True
#     if x=='-':
#         return True
#     if x=='*':
#         return True
#     if x=='/':
#         return True
#     return False
# def post_to_pre(postfix_expression):
#     s=[]
#     length=len(postfix_expression)
#     for i in range(length):
#         if (is_operand(postfix_expression[i])):
#             operand_1=s[-1]
#             s.pop()
#             operand_2 = s[-1]
#             s.pop()
#             temp=postfix_expression[i] + operand_2 + operand_1
#             s.append(temp)
#         else:
#             s.append(postfix_expression[i])
#     answer=''
#     for i in s:
#        answer+=i
#     return answer
# postfix_expression="AB+CD-"
# print("prefix to postfix",post_to_pre(postfix_expression))

# wap to remove duplicates of string_2 that are pesent in string_1 :-
# string_1>string_2
size=256
# def list_conversion(string):
#     temp=[]
#     for i in string:
#         temp.append(i)
#     return temp
# def string_conversion(List):
#     return ''.join(List)
# def get_count_of_char(string):
#     count=[0]*size
#     for i in string:
#         count[ord(i)] += 1
#     return count
# def remove_duplicates(string_1,string_2):
#     count=get_count_of_char(string_2)
#     input_index=0
#     resultant_index=0
#     temp=''
#     str_list=list_conversion(string_1)
#     while input_index is not len(str_list):
#         temp=str_list[input_index]
#         if count[ord(temp)]==0:
#             str_list[resultant_index]=str_list[input_index]
#             resultant_index+=1
#         input_index +=1
#     return string_conversion(str_list[0:resultant_index])
# string_1="carry"
# string_2="car"
# print(remove_duplicates(string_1,string_2))

# wap to implement stack using double ended queue:-
from collections import deque
class Stack :
    def __init__(self):
        self.dequeue=deque()
    def push(self,data):
        self.dequeue.append(data)
    def pop(self):
        return self.dequeue.pop()
    def size(self):
        return len(self.dequeue)
    def is_empty(self):
        return not self.dequeue
    def top(self):
        if self.is_empty():
            return None
        return self.dequeue[-1]
st = Stack()
st.push(1)
st.push(2)
st.push(3)
print("current size:", st.size())
print(st.top())
st.pop()
print(st.top())
st.pop()
print(st.top())
print("current size:", st.size())