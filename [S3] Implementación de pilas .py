class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, element):
        self.items.append(element)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)


def is_balanced(expression):
    stack = Stack()
    pairs = {')': '(', ']': '[', '}': '{'}
    
    for char in expression:
        if char in pairs.values():
            stack.push(char)
        elif char in pairs.keys():
            if stack.is_empty() or stack.pop() != pairs[char]:
                return False
    
    return stack.is_empty()


def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}
    stack = Stack()
    output = []
    tokens = expression.split()
    
    for token in tokens:
        if token.isnumeric():
            output.append(token)
        elif token == '(':
            stack.push(token)
        elif token == ')':
            while not stack.is_empty() and stack.peek() != '(':
                output.append(stack.pop())
            stack.pop()
        else:
            while (not stack.is_empty() and precedence[stack.peek()] >= precedence[token]):
                output.append(stack.pop())
            stack.push(token)
    
    while not stack.is_empty():
        output.append(stack.pop())
    
    return ' '.join(output)


test_expression_1 = "( 3 + 2 ) * ( 8 / 4 )"
test_expression_2 = "( ( 3 + 2 ) * ( 8 / 4 "

print("Expresión balanceada:", is_balanced(test_expression_1))  # True
print("Expresión balanceada:", is_balanced(test_expression_2))  # False

infix_expr = "3 + 5 * ( 2 - 8 )"
print("Notación postfija:", infix_to_postfix(infix_expr))  # "3 5 2 8 - * +"
