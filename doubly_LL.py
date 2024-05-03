# doubly linked list
# class Node:
#     def __init__(self, prev=None, data=None, next=None):
#         self.data = data
#         self.prev = prev
#         self.next = next
#     def setdata(self, data):
#         self.data = data
#     def getdata(self):
#         return self.data
#     def setprev(self, prev):
#         self.prev = prev
#     def getprev(self):
#         return self.prev
#     def setnext(self, next):
#         self.next = next
#     def getnext(self):
#         return self.next
#     def __repr__(self):
#         return repr(self.data)
#
#
# class DobulyLinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.length = 0
#
#     def __repr__(self):
#         nodes = []
#         curr = self.head
#         while curr:
#             nodes.append(repr(curr))
#             curr = curr.next
#         return "->".join(nodes)
#
#     def insert_at_beginning(self, data):
#         newNode = Node()
#         newNode.setdata(data)
#         if self.head == None:
#             self.head = self.tail = newNode
#         else:
#             # newNode.setprev(None)
#             newNode.setnext(self.head)
#             self.head.setprev(newNode)
#             self.head = newNode
#         self.length += 1
#
#     def insert_at_end(self, data):
#         newNode = Node()
#         newNode.setdata(data)
#         if self.length == 0 or self.head == None:
#             self.head = newNode
#             self.head = self.tail = newNode
#         else:
#             current = self.head
#             while current.getnext() != None:
#                 current = current.getnext()
#             current.setnext(newNode)
#             newNode.setprev(current)
#             self.tail = newNode
#         self.length += 1
#
#     def insert_at_pos(self,data,pos):
#         newNode=Node()
#         newNode.setdata(data)
#         count =0
#         current = self.head
#         temp = None
#         while count < pos - 1:
#             count = count + 1
#             temp = current
#             current = current.getnext()
#         temp.setnext(newNode)
#         newNode.setprev(temp)
#         current.setprev(newNode)
#         newNode.setnext(current)
#
#
#
#     def delete_from_beginning(self):
#         if self.head==None:
#             pass
#         else:
#             self.head=self.head.getnext()
#
#     def delete_from_end(self):
#         if self.head == None:
#             pass
#         else:
#             current = self.head
#             prev= self.head
#             while current.getnext() != None:
#                 prev=current
#                 current=current.getnext()
#             prev.setnext(None)
#         self.length -=1
#
#     def delete_from_position(self,pos):
#         if pos > self.length or pos <0 :
#             pass
#         else:
#             if pos==0:
#                 self.delete_from_beginning()
#             elif pos==self.length:
#                 self.delete_from_end
#             else:
#                 count=0
#                 current=self.head
#                 prev=self.head
#                 while count < pos-1:
#                     count+=1
#                     prev=current
#                     current=current.getnext()
#                 prev.setnext(current.getnext())
#                 current.setprev(prev)
#             self.length -=1
#
#     def reverse(self):
#         current=self.head
#         temp=self.head
#         while current.getnext() != None:
#             temp=current.getprev()
#             current.setprev(current.getnext())
#             current.setnext(temp)
#             current=current.getprev()
#         self.head=temp.getprev()
#
#
#
#
# l = DobulyLinkedList()
# (l.insert_at_beginning(1))
# l.insert_at_beginning(2)
# l.insert_at_beginning(6)
# l.insert_at_end(67)
# l.insert_at_end(68)
# l.insert_at_end(69)
# l.insert_at_end(70)
# l.insert_at_pos(4,7)
# # l.delete_from_beginning()
# # l.delete_from_end()
# # l.delete_from_position(4)
# # l.reverse()
# print(l)