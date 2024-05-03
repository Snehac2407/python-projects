# wap to detect loop by hashing
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.length=0
#     def insert_at_beginning(self, new_data):
#         new_node = Node(new_data)
#         new_node.next = self.head
#         self.head = new_node
#         self.length +=1
#     def display(self):
#         temp = self.head
#         while (temp):
#             print(temp.data, end="-->")
#             temp = temp.next
#
#     def detectLoop(self):
#         s = set()#its a hashmap
#         temp = self.head
#         while (temp):
#             if (temp in s):
#                 return True
#             s.add(temp)
#             temp = temp.next
#         return False
#     def CreateLoop(self, n):
#         LoopNode = self.head
#         for _ in range(1, n):
#             LoopNode = LoopNode.next
#         end = self.head
#         while (end.next):
#             end = end.next
#         end.next = LoopNode
#
# l= LinkedList()
# l.insert_at_beginning(20)
# l.insert_at_beginning(4)
# l.insert_at_beginning(15)
# l.insert_at_beginning(10)
# l.display()
# l.CreateLoop(2)
# if (l.detectLoop()):
#     print("\nLoop Found")
# else:
#     print("No Loop ")
#
#


# floyid's algorithm for detecting loop
# Python program to detect loop in the linked list
# class Node:
# 	def __init__(self, data):
# 		self.data = data
# 		self.next = None
# class LinkedList:
# 	def __init__(self):
# 		self.head = None
# 	def push(self, new_data):
# 		new_node = Node(new_data)
# 		new_node.next = self.head
# 		self.head = new_node
# 	def printList(self):
# 		temp = self.head
# 		while(temp):
# 			print(temp.data)
# 			temp = temp.next
# 	def detectLoop(self):
# 		slow_p = self.head
# 		fast_p = self.head
# 		while(slow_p and fast_p and fast_p.next):
# 			slow_p = slow_p.next
# 			fast_p = fast_p.next.next
# 			if slow_p == fast_p:
# 				return 1
# 		return 0
#
# llist = LinkedList()
# llist.push(20)
# llist.push(4)
# llist.push(15)
# llist.push(10)
#
# llist.head.next.next.next.next = llist.head
# if(llist.detectLoop()):
# 	print("Loop Found")
# else:
# 	print("No Loop")

# Python program to detect a loop and
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.length=0
#     def AddNode(self, data):
#         new_node = Node(data)
#         new_node.next = self.head
#         self.head = new_node
#         self.length +=1
#     def CreateLoop(self, n):
#         LoopNode = self.head
#         for _ in range(1, n):
#             LoopNode = LoopNode.next
#         end = self.head
#         while (end.next):
#             end = end.next
#         end.next = LoopNode
#     def detectLoop(self):
#         if self.head is None:
#             return 0
#         slow = self.head
#         fast = self.head
#         flag = 0
#         while (slow and fast and  fast.next):
#             if slow == fast and flag != 0:
#                 count = 1
#                 slow = slow.next
#                 while (slow != fast):
#                     slow = slow.next
#                     count += 1
#                 return count
#             slow = slow.next
#             fast = fast.next.next
#             flag = 1
#         return 0
# myLL = LinkedList()
# myLL.AddNode(1)
# myLL.AddNode(2)
# myLL.AddNode(3)
# myLL.AddNode(4)
# myLL.AddNode(5)
# myLL.CreateLoop(3)
# loopLength = myLL.detectLoop()
# if myLL.head is None:
#     print("Linked list is empty")
# else:
#     print(str(loopLength))


# for finding the intersection point of two linkedlist:-
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.head2 =None
#         self.length=0
#     def insert_at_beginning(self, new_data):
#         new_node = Node(new_data)
#         new_node.next = self.head
#         self.head = new_node
#         self.length +=1
#
#     def insert_at_beginning2(self, new_data):
#         new_node = Node(new_data)
#         new_node.next = self.head2
#         self.head2= new_node
#         self.length +=1
#
#     def display2(self):
#         temp = self.head
#         while (temp):
#             print(temp.data, end="-->")
#             temp = temp.next
#
#     def display(self):
#         temp = self.head2
#         while (temp):
#             print(temp.data, end="-->")
#             temp = temp.next
#
#
#     def intersectiop(self):
#         s = set()#its a hashmap
#         while (self.head != None):
#             s.add(self.head)
#             self.head=self.head.next
#         while (self.head2 != None):
#              if (self.head2 in s):
#                  return self.head2
#              self.head2=self.head2.next
#         return None
#
# l= LinkedList()
# l.insert_at_beginning(20)
# l.insert_at_beginning(4)
# l.insert_at_beginning(15)
# l.insert_at_beginning(10)
# l.insert_at_beginning2(56)
# l.insert_at_beginning2(4)
# l.insert_at_beginning2(15)
# l.insert_at_beginning2(40)
# l.display()
# print()
# l.display2()
# print(l.intersectiop())



# Python program to get intersection point of two linked list
# class Node:
# 	def __init__(self, data):
# 		self.data = data
# 		self.next = None
# def Print(n):
# 	cur = n
# 	while (cur != None):
# 		print(cur.data, end=" ")
# 		cur = cur.next
# 	print("")
# def MegeNode(n1, n2):
# 	hs = set()
# 	while (n1 != None):
# 		hs.add(n1)
# 		n1 = n1.next
# 	while (n2 != None):
# 		if (n2 in hs):
# 			return n2
# 		n2 = n2.next
#
# 	return None
#
# n1 = Node(1)
# n1.next = Node(2)
# n1.next.next = Node(3)
# n1.next.next.next = Node(4)
# n1.next.next.next.next = Node(5)
# n1.next.next.next.next.next = Node(6)
# n1.next.next.next.next.next.next = Node(7)
# n2 = Node(10);
# n2.next = Node(9);
# n2.next.next = Node(8);
# n2.next.next.next = n1.next.next.next;
#
# Print(n1);
# Print(n2);
#
# print(MegeNode(n1, n2).data);
# Python program to merge two sorted linked lists

# class Node:
# 	def __init__(self, data):
# 		self.data = data
# 		self.next = None
# class LinkedList:
# 	def __init__(self):
# 		self.head = None
# 	def printList(self):
# 		temp = self.head
# 		while temp:
# 			print(temp.data, end="-->")
# 			temp = temp.next
# 	def addToList(self, newData):
# 		newNode = Node(newData)
# 		if self.head is None:
# 			self.head = newNode
# 			return
# 		last = self.head
# 		while last.next:
# 			last = last.next
# 		last.next = newNode
# def mergeLists(headA, headB):
# 	dummyNode = Node(0)
# 	tail = dummyNode
# 	while True:
# 		if headA is None:
# 			tail.next = headB
# 			break
# 		if headB is None:
# 			tail.next = headA
# 			break
# 		if headA.data <= headB.data:
# 			tail.next = headA
# 			headA = headA.next
# 		else:
# 			tail.next = headB
# 			headB = headB.next
# 		tail = tail.next
# 	return dummyNode.next
#
#
# # Create 2 lists
# listA = LinkedList()
# listB = LinkedList()
# listA.addToList(5)
# listA.addToList(10)
# listA.addToList(15)
# listA.printList()
# print("")
# listB.addToList(2)
# listB.addToList(3)
# listB.addToList(20)
# listB.printList()
# listA.head = mergeLists(listA.head, listB.head)
# print("\nMerged Linked List is:")
# listA.printList()




# Python program to swap the elements of linked list pairwise
# class Node:
# 	def __init__(self, data):
# 		self.data = data
# 		self.next = None
# class LinkedList:
# 	def __init__(self):
# 		self.head = None
# 	def pairwiseSwap(self):
# 		temp = self.head
# 		if temp is None:
# 			return
# 		while(temp and temp.next):
# 			if(temp.data != temp.next.data):
# 				temp.data, temp.next.data = temp.next.data, temp.data
# 			temp = temp.next.next
# 	def add(self, new_data):
# 		new_node = Node(new_data)
# 		new_node.next = self.head
# 		self.head = new_node
# 	def printList(self):
# 		temp = self.head
# 		while(temp):
# 			print (temp.data,end="-->")
# 			temp = temp.next
#
# llist = LinkedList()
# llist.add(5)
# llist.add(4)
# llist.add(3)
# llist.add(2)
# llist.add(1)
#
# print ("Linked list before ")
# llist.printList()
# llist.pairwiseSwap()
# print ("\nLinked list after")
# llist.printList()


#wap to rotate a linkedlist by kth node in counter clockwise(anti-clockwise):-
# class Node:
# 	def __init__(self, data):
# 		self.data = data
# 		self.next = None
# class LinkedList:
# 	def __init__(self):
# 		self.head = None
# 	def add(self, new_data):
# 		new_node = Node(new_data)
# 		new_node.next = self.head
# 		self.head = new_node
# 	def printList(self):
# 		temp = self.head
# 		while(temp):
# 			print (temp.data,end="-->")
# 			temp = temp.next
#
# 	def add(self, new_data):
# 		new_node = Node(new_data)
# 		new_node.next = self.head
# 		self.head = new_node
#
# 	def rotate(self,k):
# 		if  k==0:
# 			return
# 		current=self.head
# 		count =1
# 		while(count < k and current is not None):
# 			current=current.next
# 			count +=1
# 		if current is None:
# 			return
# 		k_node=current
# 		while(current.next is not None):
# 			current=current.next
# 		current.next=self.head
# 		self.head=k_node.next
# 		k_node.next=None
# l= LinkedList()
# for i in range(70,0,-10):
# 	l.add(i)
# l.printList()
# l.rotate(5)
# print()
# l.printList()



# wap for removingduplicates from a sorted linkedlist
# class Node:
# 	def __init__(self, data):
# 		self.data = data
# 		self.next = None
# class LinkedList:
# 	def __init__(self):
# 		self.head = None
# 	def add(self, data):
# 		new_node = Node(data)
# 		new_node.next = self.head
# 		self.head = new_node
# 	def printList(self):
# 		temp = self.head
# 		while (temp):
# 			print(temp.data, end=' ')
# 			temp = temp.next
# 	def remove_duplicates(self):
# 		current = self.head
# 		if current is None:
# 			return
# 		while current.next is not None:
# 			if current.data == current.next.data:
# 				new = current.next.next
# 				current.next = new
# 			else:
# 				current = current.next
# 		return
#
#
# llist = LinkedList()
# llist.add(35)
# llist.add(30)
# llist.add(12)
# llist.add(12)
# for i in range(50,0,-13):
# 	llist.add(i)
# print("orignal List: ")
# llist.printList()
# print()
# print("List after  removing duplicate elements:")
# llist.remove_duplicates()
# llist.printList()

# wap to delete the last occurance of a data in the lnkedlist:-
# class Node:
# 	def __init__(self, data):
# 		self.data = data
# 		self.next = None
# class LinkedList:
# 	def __init__(self):
# 		self.head = None
# 	def add(self, data):
# 		new_node = Node(data)
# 		new_node.next = self.head
# 		self.head = new_node
# 	def printList(self):
# 		temp = self.head
# 		while (temp):
# 			print(temp.data, end='-->')
# 			temp = temp.next
# 	def delete_last_occurance(self,x):
# 		current=self.head
# 		prev=None
# 		while(current !=None):
# 			if current.data==x:
# 				prev=current
# 			current=current.next
# 		if (prev != None and prev.next == None):
# 			temp=self.head
# 			while(temp.next != prev):
# 				temp=temp.next
# 			temp.next=None
# 			return
# 		if (prev != None and prev.next != None):
# 			prev.data=prev.next.data
# 			temp=prev.next
# 			prev.next=prev.next.next
# 		return self.head
# llist = LinkedList()
# llist.add(37)
# llist.add(37)
# llist.add(47)
# llist.add(57)
# llist.add(34)
# llist.add(77)
# llist.add(77)
# llist.printList()
# print()
# llist.delete_last_occurance(77)
# llist.delete_last_occurance(37)
# llist.printList()

# wap for deleting middle pf the linkedlist:-
# class Node:
# 	def __init__(self, data):
# 		self.data = data
# 		self.next = None
# class LinkedList:
# 	def __init__(self):
# 		self.head = None
# 	def addToList(self, data):
# 		newNode = Node(data)
# 		if self.head is None:
# 			self.head = newNode
# 			return
# 		last = self.head
# 		while last.next:
# 			last = last.next
# 		last.next = newNode
#
# 	def printList(self):
# 		temp = self.head
# 		while (temp):
# 			print(temp.data, end='-->')
# 			temp = temp.next
# 	def deleteMid(self):
# 		if (self.head is None or
# 				self.head.next is None):
# 			return
# 		slow= self.head
# 		fast= self.head
# 		prev = None
# 		while (fast is not None and
# 			   fast.next is not None):
# 			fast= fast.next.next
# 			prev = slow
# 			slow = slow.next
# 		prev.next = slow.next
#
#
# '''def countOfNodes(head):
# 	count = 0
# 	while (head != None):
# 		head = head.next
# 		count += 1
# 	return count
# def deleteMid(head):
# 	if (head == None):
# 		return None
# 	if (head.next == None):
# 		del head
# 		return None
# 	copyHead = head
# 	count = countOfNodes(head)
# 	mid = count // 2
# 	while (mid > 1):
# 		mid -= 1
# 		head = head.next
# 	head.next = head.next.next
# 	return copyHead'''
#
# # Driver code
# linkedList = LinkedList()
# linkedList.addToList(5)
# linkedList.addToList(10)
# linkedList.addToList(15)
# linkedList.addToList(20)
# linkedList.addToList(25)
# print("Original List")
# linkedList.printList()
# linkedList.deleteMid()
# print("\nList after deleting the middle element")
# linkedList.printList()


# wap for deleting N nodesafter M nodes of a linked list
'''class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
class LinkedList:
	def __init__(self):
		self.head = None
	def add(self, data):
		new_node = Node(data)
		new_node.next = self.head
		self.head = new_node
	def printList(self):
		temp = self.head
		while (temp):
			print(temp.data, end='-->')
			temp = temp.next
	def deleting_N_node_after_M(self,N,M):
		current=self.head
		while current:
			for count in range(1,M):
				if current is None:
					return
				current=current.next
			if current is None:
				return
			prev=current.next
			for count in range(1,N+1):
				if prev is None:
					break
				prev=prev.next
			current.next=prev
			current=prev
L=LinkedList()
for i in range(1,20):
	L.add(i)
L.printList()
L.deleting_N_node_after_M(2,3)
print("\nafter deleting N nodes after M nodes in a linked list")
L.printList()'''

# wap to merge two linked list alternatively :
# class Node(object):
# 	def __init__(self,data):
# 		self.data = data
# 		self.next = None
# class LinkedList(object):
# 	def __init__(self):
# 		self.data=None
# 		self.head = None
# 	def push(self,data):
# 		new_node = Node(data)
# 		new_node.next = self.head
# 		self.head = new_node
# 	def printList(self):
# 		temp = self.head
# 		while temp != None:
# 			print(temp.data, end=" ")
# 			temp = temp.next
# 	def merge(self, p, q):
# 		p_curr = p.head
# 		q_curr = q.head
# 		while p_curr != None and q_curr != None:
# 			p_next = p_curr.next
# 			q_next = q_curr.next
# 			q_curr.next = p_next
# 			p_curr.next = q_curr
# 			p_curr = p_next
# 			q_curr = q_next
# 			q.head = q_curr
# llist1 = LinkedList()
# llist2 = LinkedList()
# llist1.push(18)
# llist1.push(17)
# llist1.push(7)
# llist1.push(8)
# llist2.push(4)
# llist2.push(2)
# llist2.push(10)
# llist2.push(32)
# print("First Linked List:")
# llist1.printList()
# print("\nSecond Linked List:")
# llist2.printList()
# llist1.merge(p=llist1, q=llist2)
# print("\nModified first linked list:")
# llist1.printList()


# wap to delete a node from a linkedlist with out head pointer onlyaddress of the pointer is given :-
#
# class Node:
# 	def __init__(self,data):
# 		self.data =data
# 		self.next = None
# class LinkedList:
# 	def __init__(self):
# 		self.head = None
# 	def delete_node_without_head(self, pos):
# 		if pos is None:
# 			return
# 		elif pos.next is None:
# 			print("This is last node, require head, can't be freed\n")
# 			return
# 		pos.data = pos.next.data
# 		pos.next = pos.next.next
# 	def push(self, new_data):
# 		new_node = Node(new_data)
# 		new_node.next = self.head
# 		self.head = new_node
# 	def print_list(self):
# 		temp = self.head
# 		while temp is not None:
# 			print(temp.data, end='->')
# 			temp = temp.next
# 		print("NULL\n")
# llist = LinkedList()
# llist.push(20)
# llist.push(4)
# llist.push(15)
# llist.push(35)
# print("Initial Linked List : ")
# llist.print_list()
# del_node = llist.head.next
# llist.delete_node_without_head(del_node)
# print("Final Linked List after deletion of 15 : ")
# llist.print_list()

# Python program to rearrange link list in place
#
# # Node Class
# class Node:
#     def __init__(self, d):
#         self.data = d
#         self.next = None
# def printlist(node):
#     if (node == None):
#         return
#     while (node != None):
#         print(node.data, " -> ",end ="")
#         node = node.next
# def reverselist(node):
#     prev = None
#     curr = node
#     next = None
#     while (curr != None):
#         next = curr.next
#         curr.next = prev
#         prev = curr
#         curr = next
#     node = prev
#     return node
# def rearrange(node):
#     slow = node
#     fast = slow.next
#     while (fast != None and fast.next != None):
#         slow = slow.next
#         fast = fast.next.next
#     node1 = node
#     node2 = slow.next
#     slow.next = None
#     node2 = reverselist(node2)
#     new_node = Node(0)
#     curr = new_node
#     while (node1 != None or node2 != None):
#         if (node1 != None):
#             curr.next = node1
#             curr = curr.next
#             node1 = node1.next
#         if (node2 != None):
#             curr.next = node2
#             curr = curr.next
#             node2 = node2.next
# head = Node(1)
# head.next = Node(2)
# head.next.next = Node(3)
# head.next.next.next = Node(4)
# head.next.next.next.next = Node(5)
# printlist(head)
# rearrange(head)
# print()
# printlist(head)

# wap to delete every kyh nodefrom a linked list:-
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
# class LinkedList:
# 	def __init__(self):
# 		self.head = None
# 	def add(self, data):
# 		new_node = Node(data)
# 		new_node.next = self.head
# 		self.head = new_node
# 	def printList(self):
# 		temp = self.head
# 		while (temp):
# 			print(temp.data, end='-->')
# 			temp = temp.next
#
#     # def free_List(self):
#     #     current = self.head
#     #     while(current!=None):
#     #         current=current.next
#     #         self.head=current
#     #     return None
#     def deleting_k_node(self,k):
#         if self.head==None:
#             return None
#         # if k==1:
#         #     self.free_List()
#         #     return None
#         prev = None
#         current = self.head
#         count = 0
#         while (current is not None):
#             count +=1
#             if (count%k==0):
#                 prev.next=current.next
#                 count=0
#             elif(count!=0):
#                 prev=current
#             current=prev.next
#         return self.head
# List=LinkedList()
# List.add(20)
# List.add(53)
# List.add(63)
# List.add(27)
# List.add(266)
# List.add(87)
# List.add(38)
# List.add(54)
# List.add(786)
# List.add(23)
# List.printList()
# List.deleting_k_node(4)
# List.printList()
#


# program to delete every k-th Node of a singly linked list.
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
# class linkedList:
#     def __init__(self):
#         self.head=None
#     def freeList(self):
#         while (self.head != None):
#             next = self.head.next
#             self.head = next
#         return self.head
#     def deleteKthNode(self, k):
#         if (self.head == None):
#             return None
#         if (k == 1):
#             self.freeList(self.head)
#             return None
#         current = self.head
#         prev = None
#         count = 0
#         while (current != None):
#             if (count != 0):
#                 prev = current
#             current = prev.next
#             return self.head
#             count = count + 1
#             if (k == count):
#                 prev.next = current.next
#                 count = 0
#     def displayList(head):
#         temp = head
#         while (temp != None):
#             print(temp.data,'-->',end=' ')
#             temp = temp.next
#     def add(self,data):
#         new_node = Node(data)
#         new_node.next = self.head
#         self.head = new_node
#     def printList(self):
#         temp = self.head
#         while (temp):
#             print(temp.data, end='-->')
#             temp = temp.next
#
# List=linkedList()
# List.add(20)
# List.add(53)
# List.add(63)
# List.add(27)
# List.add(266)
# List.add(87)
# List.add(38)
# List.add(54)
# List.add(786)
# List.add(23)
# List.printList()
# List.deleteKthNode(4)
# List.printList()

# wap for counting occurance of a number in a linkedlist:-
# Python program to count the number of time a given
# int occurs in a linked list

# Node class
# class Node:
# 	def __init__(self, data):
# 		self.data = data
# 		self.next = None
# class LinkedList:
# 	def __init__(self):
# 		self.head = None
# 	def count(self, search_for):
# 		current = self.head
# 		count = 0
# 		while(current is not None):
# 			if current.data == search_for:
# 				count += 1
# 			current = current.next
# 		return count
# 	def push(self, new_data):
# 		new_node = Node(new_data)
# 		new_node.next = self.head
# 		self.head = new_node
# 	def printList(self):
# 		temp = self.head
# 		while(temp):
# 			print(temp.data,end='-->')
# 			temp = temp.next
# llist = LinkedList()
# llist.push(1)
# llist.push(3)
# llist.push(1)
# llist.push(2)
# llist.push(1)
# llist.printList()
# print("\ncounting of number is ",llist.count(1))


# Python program to reverse a# linked list in group of given size:-
# class Node:
# 	def __init__(self, data):
# 		self.data = data
# 		self.next = None
# class LinkedList:
# 	def __init__(self):
# 		self.head = None
# 	def reverse(self, head, k):
# 		if head == None:
# 			return None
# 		current = head
# 		next = None
# 		prev = None
# 		count = 0
# 		while (current is not None and count < k):
# 			next = current.next
# 			current.next = prev
# 			prev = current
# 			current = next
# 			count += 1
# 		if next is not None:
# 			head.next = self.reverse(next, k)
# 		return prev
# 	def push(self, new_data):
# 		new_node = Node(new_data)
# 		new_node.next = self.head
# 		self.head = new_node
# 	def printList(self):
# 		temp = self.head
# 		while (temp):
# 			print(temp.data, end='-->')
# 			temp = temp.next
# llist = LinkedList()
# for i in range(1,10):
# 	llist.push(i)
# llist.printList()
# llist.head = llist.reverse(llist.head, 3)
# print("\nReversed Linked list")
# llist.printList()

# wap to merege two sorted linked list recussivley:-
# class Node:
# 	def __init__(self, data):
# 		self.data = data
# 		self.next = None
# class LinkedList:
# 	def __init__(self):
# 		self.head = None
# 	def printList(self):
# 		temp = self.head
# 		while temp:
# 			print(temp.data, end="-->")
# 			temp = temp.next
# 	def insert(self, newData):
# 		newNode = Node(newData)
# 		if self.head is None:
# 			self.head = newNode
# 			return
# 		last = self.head
# 		while last.next:
# 			last = last.next
# 		last.next = newNode
# def mergeSortedLists(head1, head2):
# 	temp = None
# 	if head1 is None:
# 		return head2
# 	if head2 is None:
# 		return head1
# 	if head1.data <= head2.data:
# 		temp = head1
# 		temp.next = mergeSortedLists(head1.next, head2)
# 	else:
# 		temp = head2
# 		temp.next = mergeSortedLists(head1, head2.next)
# 	return temp
# head1 = LinkedList()
# head2 = LinkedList()
# head1.insert(1)
# head1.insert(2)
# head1.insert(4)
# head1.insert(6)
# head1.insert(9)
# head2.insert(3)
# head2.insert(4)
# head2.insert(7)
# head2.insert(8)
# head1.head = mergeSortedLists(head1.head, head2.head)
# head1.printList()



# wap to sort the linkedlist of 0's,1's,2's :- Python program to sort a linked list of 0, 1 and 2
# class LinkedList:
# 	def __init__(self):
# 		self.head = None
# 	class Node :
# 		def __init__(self, data):
# 			self.data = data
# 			self.next = None
# 	def sortList(self):
# 		count = [0, 0, 0]
# 		ptr = self.head
# 		while ptr != None:
# 			count[ptr.data]+=1
# 			ptr = ptr.next
# 		i = 0
# 		ptr = self.head
# 		while ptr != None:
# 			if count[i] == 0:
# 				i+=1
# 			else:
# 				ptr.data = i
# 				count[i]-=1
# 				ptr = ptr.next
# 	def push(self, new_data):
# 		new_node = self.Node(new_data)
# 		new_node.next = self.head
# 		self.head = new_node
# 	def printList(self):
# 		temp = self.head
# 		while temp != None:
# 			print (str(temp.data),end="-->")
# 			temp = temp.next
# 		print()
# llist = LinkedList()
# llist.push(0)
# llist.push(1)
# llist.push(0)
# llist.push(2)
# llist.push(1)
# llist.push(1)
# llist.push(2)
# llist.push(1)
# llist.push(2)
# print ("Linked List before sorting")
# llist.printList()
# llist.sortList()
# print ("Linked List after sorting")
# llist.printList()

# wap for checking weather the given linkedlist is palindrome or not :-
class linkedlist:
	def __init__(self,data):
		self.data=data
		self.next=None
class palindrome:
	def __init__(self):
		self.head=None

	def add(self, new_data):
		new_node = linkedlist(new_data)
		new_node.next = self.head
		self.head = new_node
	def printList(self):
		temp = self.head
		while (temp):
			print(temp.data, end='-->')
			temp = temp.next
	def reverse(self,mid):
		current=self.head
		prev=None
		next=None
		while current is not None:
			next=current.next
			current.next=prev
			prev=current
			current=next
		return prev
	def is_palindrome(self):
		if self.head is None or self.head.next is None:
			return None
		slow=self.head
		fast=self.head
		while fast.next is not None and fast.next.next is not None:
			slow=slow.next
			fast=fast.next.next
		slow.next=self.reverse(slow.next)
		slow=slow.next
		temp=self.head
		while slow is not None:
			if temp.data != slow.data:
				print("is not palindrome")
			else:
				temp=temp.next
				slow=slow.next
			print("it is a palindrome")


L=palindrome()
L.add(23)
L.add(56)
L.add(34)
L.add(22)
L.add(34)
L.add(6)
L.add(23)
L.printList()
L.is_palindrome()
L.printList()







