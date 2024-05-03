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
        s = set()#its a hashmap
        temp = self.head
        while (temp):
            if (temp in s):
                return True
            s.add(temp)
            temp = temp.next
        return False
llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(10)
llist.display()

# Create a loop for testing
llist.head.next  = llist.head

if (llist.detectLoop()):
    print("\nLoop Found")
else:
    print("No Loop ")
