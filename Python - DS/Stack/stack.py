class Stack:
    def __init__(self):
        self.stackList = []
    
    def push(self,element):
        self.stackList.append(element)

    def pop(self):
        return self.stackList.pop()
    
    def isStackEmpty(self):
        return self.stackList == []
    
    def peek(self):
        if  self.isStackEmpty() :
            return None
        else:
            return self.stackList[-1]
        
    def getStack(self):
        return self.stackList   
    


# Stack Demo --

# myStack = Stack()

# myStack.push('A')
# myStack.push('B')
# myStack.push('C')

# print(myStack.getStack())

# myStack.pop()

# print(myStack.getStack())

# print(myStack.peek())
