class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def lengthOfLinkedList(self):
        currentNode = self.head
        length = 0
        while currentNode:
            length = length + 1
            currentNode = currentNode.next
        return length

    def insertAtPosition(self, data, position):
        new_node = Node(data)
        if position > self.lengthOfLinkedList():
            print("Invalid Position ")
            return
        if self.head == None:
            self.head = new_node
            return
        current_node = self.head
        i = 1
        while i < position - 1:
            current_node = current_node.next
            i = i + 1
        new_node.next = current_node.next
        current_node.next = new_node

    def insertAfterNode(self, nodeValue, newNodeData):
        new_node = Node(newNodeData)
        current_node = self.head
        while current_node:
            if current_node.data == nodeValue:
                new_node.next = current_node.next
                current_node.next = new_node
                return "Success"
            current_node = current_node.next
        return "Such Node Doesnt exist"

    def deleteByValue(self,nodeValue):
        if self.head.data == nodeValue:
            self.head = self.head.next
        else:
            current = self.head
            while current:                
                if(current.next.data == nodeValue):
                    current.next = current.next.next
                    break
                current = current.next
    
    def deleteByPosition(self,position):
        if position == 0:
            self.head = self.head.next
        else:
            i=0
            current_node = self.head
            while i<position-2:
                current_node = current_node.next
                i = i + 1
            current_node.next = current_node.next.next

    def swapNodes(self,key1,key2):
        current_node = self.head
        while current_node:
            if(current_node.data == key1):
                current_node.data = key2
            elif(current_node.data == key2):
                current_node.data = key1
            current_node = current_node.next
    
    def reverseList(self):
        current_node = self.head
        prev = None
        while current_node:
            next_node = current_node.next
            current_node.next = prev
            prev = current_node
            current_node = next_node 
        self.head = prev      

    def printList(self):
        currentNode = self.head
        while currentNode:
            print(currentNode.data)
            currentNode = currentNode.next


linkedList = LinkedList()
linkedList.append("A")
linkedList.append("B")
linkedList.append("C")
linkedList.append("D")


# linkedList.prepend("I")
# linkedList.prepend("O")
# linkedList.prepend("K")

# linkedList.insertAtPosition("Position Insert", 2)
# linkedList.insertAfterNode("I", "New Node Insertion")
# linkedList.deleteByValue("C")
# linkedList.deleteByPosition(8)
linkedList.printList()
print('-------------')
# linkedList.swapNodes('A','C')
linkedList.reverseList()
linkedList.printList()
