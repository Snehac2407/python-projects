 class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.length=0
    def insert_at_beginning(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
        self.length +=1

    def display(self):
        temp = self.head
        while (temp):
            print(temp.data, end="-->")
            temp = temp.next

    def detectLoop(self):
        fast=self.head
        slow=self.head
        while (slow and fast and fast.next):
            slow=slow.next
            fast= fast.next.next
        if slow==fast:
            return True
        else:
            return False
 l= LinkedList()
 l.insert_at_beginning(20)
 l.insert_at_beginning(4)
l.insert_at_beginning(15)
l.insert_at_beginning(10)
l.display()
l.head.next  = l.head

 if (l.detectLoop()):
     print("\nLoop Found")
 else:
     print("No Loop ")

