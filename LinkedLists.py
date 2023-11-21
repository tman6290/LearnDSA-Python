
    

class Node:
    def __init__(self, num:int):
        self.num = num
        self.next:Node = None

class LinkedList:
    def __init__(self):
        self.head = None

    def addNode(self, newNode:Node):
        if self.head == None:
            self.head = newNode
            current = self.head

        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = newNode
    
    def display(self):
        current = self.head

        while current.next != None:
            print(current.num, end= "->")
            current = current.next
        print(current.num, end= "->")
        print(None)

    def removeNode(self, qNode:Node):
        if qNode == self.head:
            current = self.head.next
            self.head = None
            self.head = current
        else:
            prev = None
            current = self.head
            while current != qNode:
                prev = current
                current = current.next
            prev.next = current.next
            current = None

        

           

list = LinkedList()

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)

list.addNode(n1)
list.addNode(n2)
list.addNode(n3)
list.addNode(n4)
list.addNode(n5)
list.addNode(n6)

list.display()
list.removeNode(n1)
list.removeNode(n5)
list.display()

            


    