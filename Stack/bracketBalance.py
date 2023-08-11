from stack import Stack


def getOpeningBrace (closingBrace):
    if closingBrace == ')':
        return '('
    elif closingBrace == '}':
        return '{'
    elif closingBrace == ']':
        return '['
    else:
        return None

def checkBracketBalance(brakets):
    stack = Stack()
    for c in brakets:
        if c == '(' or c == '{' or c == '[':
            stack.push(c)
        
        elif c == ')' or c == '}' or c == ']':
            topOfStack = stack.peek()
            if topOfStack == None or topOfStack != getOpeningBrace(c):
                return False
            else:
                stack.pop()
    return stack.getStack() == []

# Test Cases:

# Positive
print(checkBracketBalance('{}'))
print(checkBracketBalance('{}{}'))
print(checkBracketBalance('(({[]}))'))

# Negative
print(checkBracketBalance('(()'))
print(checkBracketBalance('{{{)}]'))
print(checkBracketBalance('[][]]]'))
