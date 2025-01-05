class Node: 
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None

    def beginInsert(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def endInsert(self, data): 
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return newNode
        
        currentNode = self.head
        while currentNode.next:
            currentNode = currentNode.next
        
        currentNode.next = newNode
        return newNode

    def sizeOf(self):
        size = 0
        currentNode = self.head
        while currentNode:
            size += 1
            currentNode = currentNode.next
        return size

    def printAll(self):
        currentNode = self.head
        while currentNode:
            print(currentNode.data, end=" -> ")
            currentNode = currentNode.next
        print("4 -> 2 -> 1 loop detected")

def collatzConjecture(value):
    llist = linkedList()
    currentNode = llist.endInsert(value) 
    while currentNode.data != 1:
        if currentNode.data % 2 == 0:
            currentNode = llist.endInsert(currentNode.data // 2)  
        else:
            currentNode = llist.endInsert(currentNode.data * 3 + 1) 
    llist.printAll()
    print("Number of iterations:", llist.sizeOf())
