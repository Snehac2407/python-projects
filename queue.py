#queue implementation using array:_
# class Queue:
#     def __init__(self,limit):
#         self.queue=[]
#         self.front=self.rear=0
#         self.limit=limit
#     def enqueue(self,data):
#         if (self.limit==self.rear):
#             print("queue is full")
#         else:
#             self.queue.append(data)
#             self.rear +=1
#
#     def queueDequeue(self):
#         if (self.front == self.rear):
#             print("Queue is empty")
#         else:
#             x = self.queue.pop(0)
#             self.rear -= 1
#     def display(self):
#         if (self.front==self.rear):
#             print("queue is empty ")
#         for i in self.queue:
#             print(i)
# q=Queue(4)
# q.enqueue(23)
# q.enqueue(33)
# q.enqueue(21)
# q.enqueue(67)
# q.display()
# print("elements that get popped from the queue ")
# q.queueDequeue()
# q.queueDequeue()
# q.display()

# Queue implementation in Python
# class Queue:
#     def __init__(self):
#         self.queue = []
#     def enqueue(self, item):
#         self.queue.append(item)
#     def dequeue(self):
#         if len(self.queue) < 1:
#             return None
#         return self.queue.pop(0)
#     # Display  the queue
#     def display(self):
#         print(self.queue)
#     def size(self):
#         return len(self.queue)
# q = Queue()
# for i in range(1,5):
#     q.enqueue(i)
# q.display()
# q.dequeue()
# print("After removing an element")
# q.display()

# Python3 program to implement Queue using
# two stacks with costly enQueue()

# class Queue:
#     def __init__(self):
#         self.s1 = []
#         self.s2 = []
#     def enQueue(self, data):
#         while len(self.s1) != 0:          # Move all elements from s1 to s2
#             self.s2.append(self.s1[-1])
#             self.s1.pop()
#         self.s1.append(data)  # Push item into self.s1
#         while len(self.s2) != 0:         # Push everything back to s1
#             self.s1.append(self.s2[-1])
#             self.s2.pop()
#     def deQueue(self):     # Dequeue an item from the queue
#         # if first stack is empty
#         if len(self.s1) == 0:
#             return -1;
#         # Return top of self.s1
#         data= self.s1[-1]
#         self.s1.pop()
#         return data
#     def display(self):
#       print(self.s1)
# q = Queue()
# q.enQueue(1)
# q.enQueue(2)
# q.enQueue(3)
# q.display()
# print(q.deQueue())
# print(q.deQueue())
# print(q.deQueue())
#
# # wap for reversing first kth element in a queue:-
# from collections import deque
# def reverse_first_k(q, k):
#     solve(q, k)
#     s = len(q) - k
#     for _ in range(s):
#         x = q.popleft()
#         q.append(x)
#     return q
# def solve(q, k):
#     if k == 0:
#         return
#     e = q.popleft()
#     solve(q, k - 1)
#     q.append(e)
# queue = deque([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
# print(queue=)
# k = 5
# queue = reverse_first_k(queue, k)
# while queue:
#     print(queue.popleft(), end=' ')


# # Python3 program for above approach
# class newNode:
# 	def __init__(self, data):
# 		self.val = data
# 		self.left = None
# 		self.right = None

# Iterative method to do level order traversal
# line by line


# def printLevelOrder(root):
#
# 	# Base case
# 	if root is None:
# 		return
# 	# Create an empty queue for level order traversal
# 	q = []

	# Enqueue root and initialize height
	# q.append(root)
    # return q

#
# 	while q:
#
# 		# nodeCount (queue size) indicates number
# 		# of nodes at current level.
# 		count = len(q)
#
# 		# Dequeue all nodes of current level and
# 		# Enqueue all nodes of next level
# 		while count > 0:
# 			temp = q.pop(0)
# 			print(temp.val, end=' ')
# 			if temp.left:
# 				q.append(temp.left)
# 			if temp.right:
# 				q.append(temp.right)
#
# 			count -= 1
# 		print(' ')
#
#
# # Driver Code
# root = newNode(1)
# root.left = newNode(2)
# root.right = newNode(3)
# root.left.left = newNode(4)
# root.left.right = newNode(5)


# class Node:
# 	def __init__(self, data):
# 		self.data = data
# 		self.next = None
# class Queue:
# 	def __init__(self):
# 		self.head = None
# 		self.last = None
# 	def enqueue(self, data):
# 		if self.last is None:
# 			self.head = Node(data)
# 			self.last = self.head
# 		else:
# 			self.last.next = Node(data)
# 			self.last = self.last.next
# 	def dequeue(self):
# 		if self.head is None:
# 			return None
# 		else:
# 			to_return = self.head.data
# 			self.head = self.head.next
# 			return to_return
# 	def print(self):
# 		temp=self.head
# 		while temp is not None:
# 			print(temp.data,"-->",end='')
# 			temp=temp.next
# 		print()
# a_queue=Queue()
# a_queue.enqueue(23)
# a_queue.enqueue(34)
# a_queue.enqueue(54)
# a_queue.enqueue(67)
# a_queue.print()
# a_queue.dequeue()
# a_queue.print()



# Circular Queue implementation in Python
# class Queue(object):
#     def __init__(self, limit=5):
#         self.que = []
#         self.limit = limit
#         self.front = None
#         self.rear = None
#         self.size = 0
#     def isQueueEmpty(self):
#         return self.size <= 0
#     def enQueue(self, item):
#         if self.size >= self.limit:
#             print("Queue Overflow")
#             return
#         else:
#             self.que.append(item)
#         if self.front is None:
#             self.front = self.rear = 0
#         else:
#             self.rear = self.size
#         self.size += 1
#         print("Queue after adding element", self.que)
#     def deQueue(self):
#         if self.isQueueEmpty():
#             print("Queue Unerflow")
#             return
#         else:
#             self.que.pop(0)
#             self.size -= 1
#             if self.size == 0:
#                 self.front = self.rear = None
#             else:
#                 self.rear = self.size - 1
#             print("Queue after deleting element", self.que)
#     def queueSize(self):
#         return self.size
# que = Queue()
# que.enQueue(1)
# que.enQueue(2)
# que.enQueue(3)
# que.enQueue(4)
# que.enQueue(5)
# # dequeue
# que.deQueue()
# # queue size
# print(que.queueSize())


# Design a Queue data structure to get minimum or maximum in O(1) time
# from collections import deque
# class MinMaxQueue:
#     def __init__(self):
#         self.queue = deque()
#         self.min_values = deque()
#         self.max_values = deque()
#     def enqueue(self, value):
#         self.queue.append(value)
#         while self.min_values and self.min_values[-1] > value:        # Update the minimum values deque
#             self.min_values.pop()
#         self.min_values.append(value)
#
#         while self.max_values and self.max_values[-1] < value:       # Update the maximum values deque
#             self.max_values.pop()
#         self.max_values.append(value)
#     def dequeue(self):
#         if not self.queue:
#             return None
#         removed_value = self.queue.popleft()
#         if self.min_values[0] == removed_value:       # Remove the minimum value if it matches the dequeued value
#             self.min_values.popleft()
#         if self.max_values[0] == removed_value:       # Remove the maximum value if it matches the dequeued value
#             self.max_values.popleft()
#         return removed_value
#     def get_min(self):
#         return self.min_values[0] if self.min_values else None
#     def get_max(self):
#         return self.max_values[0] if self.max_values else None
# min_max_queue = MinMaxQueue()
# for i in range(20,43):
#     min_max_queue.enqueue(i)
#
# min_max_queue.dequeue()
# print("Min:", min_max_queue.get_min())
# print("Max:", min_max_queue.get_max())

# wap to implement priority queue using linkedlist:-
# class Node:
#     def __init__(self,data,priority):
#         self.data=data
#         self.priority=priority
#         self.next=None
# class Priority_Queue():
#     def __init__(self):
#         self.head=None
#     def is_empty(self):
#         return self.head is None
#     def enqueue(self,data,priority):
#         new_Node=Node(data,priority)
#         if self.is_empty() or priority >self.head.priority:
#             new_Node.next=self.head
#             new_Node.next=self.head
#             self.head=new_Node
#         else:
#             current=self.head
#             while current.next is not None and current.next.priority >= priority:
#                 current=current.next
#             new_Node.next=current.next
#             current.next=new_Node
#     def dequeue(self):
#         if self.is_empty():
#             return None
#         data=self.head.next
#         self.head=self.head.next
#         return data
#     def display(self):
#         current=self.head
#         while current:
#             print(f"data:{current.data},priority:{current.priority}")
#             current=current.next
# P_Q=Priority_Queue()
# P_Q.enqueue(23,4)
# P_Q.enqueue(2,3)
# P_Q.enqueue(12,10)
# P_Q.enqueue(45,2)
# P_Q.enqueue(3,14)
# P_Q.display()
#

#wap to check if a queue  is sortable or not using stack :-
def Sorted_queue(queue):
    stack=[]
    sorted_queue=[]
    while queue:
        current=queue.pop(0)
        if not sorted_queue:
            sorted_queue.append(current)
        else:
            while sorted_queue and sorted_queue[-1]>current:
                stack.append(sorted_queue.pop())
            sorted_queue.append(current)
            while stack:
                sorted_queue.append(stack.pop())
    return sorted_queue
queue=[23,43,12,1,5,21]
print(Sorted_queue(queue))





