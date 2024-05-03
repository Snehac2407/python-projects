class Node:
    def __init__(self):
        self.data=None
        self.next=None
    def setdata(self,data):
        self.data=data
    def getdata(self):
        return self.data
    def setnext(self,next):
        self.next=next
    def getnext(self):
        return self.next
    def __repr__(self):
        return repr(self.data)
    def diplay(self):
        return dispaly(self.data)
class Linkedlist:
    def __init__(self):
        self.head=None
        self.length=0

    def __repr__(self):
        nodes = []
        curr = self.head
        while curr:
            nodes.append(repr(curr))
            curr = curr.getnext()
        return "[" + ", ".join(nodes) + "]"

    # def display(self):
    #     iterator = self.head
    #     string = ''
    #     while iterator:
    #         suffix = ''
    #         if iterator.getnext != self.head:
    #             suffix = '-->'
    #     str += str(iterator.setdata()) + suffix
    #     iterator = iterator.getnext()
    # print(str)

    def List_Length(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getnext()
        return count

    def insert_at_beginning(self,data):
        new_node=Node()
        new_node.setdata(data)
        if self.length==0:
            self.head=new_node
        else:
            new_node.setnext(self.head)
            self.head=new_node
        self.length +=1

    def insert_at_end(self,data):
        new_node=Node()
        new_node.setdata(data)
        current=self.head
        while current.getnext() != None:
            current=current.getnext()
        current.setnext(new_node)
        self.length +=1

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
                    newNode = Node()
                    newNode.setdata(data)
                    count = 0
                    current = self.head
                    while count < pos-1:
                        count = count+1
                        current = current.getnext()
                    newNode.setnext(current.getnext())
                    current.setnext(newNode)
                self.length += 1

    def delete_from_beginning(self):
         if self.length == 0:
            print("list is empty")
         else:
            self.head = self.head.getnext()
         self.length -= 1

    def delete_from_position(self,pos):
        if pos > self.length or pos <0 :
            pass
        else:
            if pos==0:
                self.delete_from_beginning()
            elif pos==self.length:
                self.delete_from_end
            else:
                current=self.head
                prev = self.head
                count=0
                while count < pos-1:
                    count +=1
                    prev=current
                    current=current.getnext()
                prev.setnext(current.getnext())
                current.setnext(None)
            self.length -=1

    def delete_from_end(self):
        current = self.head
        prev = self.head
        while current.getnext() !=None:
            prev=current
            current=current.getnext()
        prev.setnext(None)
        self.length -=1

    # def nth_end_node(self,pos):
    #     current=self.head
    #     count=0
    #     while count < pos  and current.getnext() != None:
    #         count +=1
    #         current = current.getnext()
    #     temp=self.head
    #     while current != None:
    #         current=current.getnext()
    #         temp=temp.getnext()
    #     return temp

    def nth_end_node(self,pos):
        current=self.head
        length=0
        while current != None:
            current=current.getnext()
            length +=1
        if pos > length:
            return None
        current=self.head
        for i in range(0,length-pos):
            current=current.getnext()
        return current

    def reverse(self):
        prev = None
        current = self.head
        while (current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

l=Linkedlist()
l.insert_at_beginning(12)
l.insert_at_beginning(55)
l.insert_at_pos(1,65)
l.insert_at_beginning(62)
l.insert_at_end(6)
l.insert_at_end(42)
print(l)
# l.delete_from_beginning()
# l.delete_from_position(2)
# l.delete_from_end()
print(l.List_Length())
print(l.nth_end_node(6))

l.reverse()
print(l)


