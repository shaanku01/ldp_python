from stack import Stack

def stringReverse (str):
    stack = Stack()
    i=0
    reversedString = ""
    for s in str:
        stack.push(s)
    while stack.getStack() != []:
        reversedString = reversedString + stack.pop()        
        i=i+1
    return reversedString

# Test:

print(stringReverse("Hello"))
print(stringReverse("!evitacudE ot emocleW"))

