class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def __repr__(self):
        return repr(self.data)
class CreateList:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.next = self.head
        self.length=0

    def display(self):
        current = self.head;
        if self.head is None:
          return
        else:
            while True:
                print(current.data, end="-->")
                current = current.next;
                if current==self.head:
                    break
            print()


    def List_Length(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.next()
        return count


    def add_at_end(self,data):
        newNode = Node(data)
        if self.head.data is None:
            self.head = newNode
            self.tail = newNode
            newNode.next = self.head#insterting data from the end
        else:
            self.tail.next = newNode
            self.tail = newNode
            self.tail.next = self.head
        self.length +=1

    def add_at_beginning(self, data):
        newNode = Node(data)
        if self.head.data is None:
            self.head = newNode
            self.tail = newNode
            newNode.next = self.head  # insterting data from the end
        else:
            self.head.next = newNode
            self.head = newNode
            self.head.next = self.tail
        self.length += 1

    def insert_at_pos(self,pos,data):
        if pos > self.length or pos < 0:
            return None
        else:
            if pos == 0:
                self.insert_at_beginning(data)
            else:
                if pos == self.length:
                    self.insert_at_end(data)
                else:
                    newNode = Node(data)
                    current=self.head
                    prev=self.head
                    count=0
                    while count < pos-1:
                        count +=1
                        prev = current
                        current=current.next
                        prev.next=newNode
                        newNode.next=current
                    self.length += 1


    def reverse(self, current):
        # Checks if the next node is head, if yes then prints it.
        if (current.next == self.head):
            print(current.data)
            return
        self.reverse(current.next) # Recursively calls the reverse function
        print(current.data)

cl = CreateList()
cl.add_at_beginning(45)
cl.add_at_beginning(55)
cl.add_at_beginning(15)
cl.add_at_end(1)
cl.add_at_end(2)
cl.add_at_end(3)
cl.add_at_end(4)
cl.add_at_end(5)
cl.add_at_end(6)
cl.insert_at_pos(2,66)
cl.insert_at_pos(5,56)
cl.display()
print("\nReversed List: ")
cl.reverse(cl.head)


# class Node:
#     def __init__(self):
#         self.data = None
#         self.next = None
#     def setNext(self, next_node):
#         self.next = next_node
#     def getNext(self):
#         return self.next
#     def setData(self, data):
#         self.data = data
#     def getData(self):
#         return self.data
#     def hasNext(self):
#         return self.getNext() is not None
#     def __repr__(self):
#         return repr(self.data)
#
#
# class CircularLinkedList:
#     def __init__(self):
#         self.head = None
#         self.length = 0
#
#     def display(self):
#         if not self.head:
#             return
#         current = self.head
#         while True:
#             print(current.data, end=" -> ")
#             current = current.getNext()
#             if current == self.head:
#                 break
#         print()
#
#     # def __repr__(self):
#     #     nodes = []
#     #     curr = self.head
#     #     while curr:
#     #         nodes.append(repr(curr))
#     #         curr = curr.next
#     #     return "[" + ", ".join(nodes) + "]"
#
#     def insertAtBeginning(self, data):
#         new_node = Node()
#         new_node.setData(data)
#         new_node.setNext(new_node)  # Circular link to itself
#
#         if self.head is None:
#             self.head = new_node
#         else:
#             current_node = self.head
#             while current_node.getNext() != self.head:
#                 current_node = current_node.getNext()
#             current_node.setNext(new_node)
#             new_node.setNext(self.head)
#             self.head = new_node
#         self.length += 1
#
#     def insertAtEnd(self, data):
#         newNode = Node()
#         newNode.setData(data)
#         newNode.setNext(newNode)
#
#         if self.head is None:
#             self.head = newNode()
#         else:
#             current_node = self.head
#             while current_node.getNext() is not self.head:
#                 current_node = current_node.getNext()
#             current_node.setNext(newNode)
#             newNode.setNext(self.head)
#         self.length += 1
#
#     def insertAtPosition(self, data, position):
#         if position <= 0:
#             self.insertAtBeginning(data)
#         elif position >= self.length:
#             self.insertAtEnd(data)
#         else:
#             new_node = Node()
#             new_node.setData(data)
#             count = 0
#             current_node = self.head
#             while count < position - 1:
#                 count += 1
#                 current_node = current_node.getNext()
#             new_node.setNext(current_node.getNext())
#             current_node.setNext(new_node)
#         self.length += 1
#
#     def delete_from_beginning(self):
#         if not self.head:
#             return "List is empty"
#         current_node = self.head
#         while current_node.getNext() is not self.head:
#             current_node = current_node.getNext()
#         current_node.setNext(self.head.getNext())
#         self.head = self.head.getNext()
#         self.length -= 1
#         return
#
#     def delete_from_end(self):
#         if not self.head:
#             return "List is empty"
#         current_node = self.head
#         prev_node = self.head
#         while current_node.getNext() is not self.head:
#             prev_node = current_node
#             current_node = current_node.getNext()
#         prev_node.setNext(current_node.getNext())
#         self.length -= 1
#         return
#
#     def delete_from_position(self, position):
#         if position < 0:
#             return
#         count = 0
#         current_node = self.head
#         prev_node = self.head
#         while count < position - 1:
#             prev_node = current_node
#             current_node = current_node.getNext()
#         prev_node.setNext(current_node.getNext())
#         current_node.setNext(None)
#         self.length -= 1
#         return
#
#
# circular_linked_list = CircularLinkedList()
#
# circular_linked_list.insertAtBeginning(1)
# circular_linked_list.insertAtBeginning(2)
# circular_linked_list.insertAtPosition(4, 2)
#
# circular_linked_list.display()