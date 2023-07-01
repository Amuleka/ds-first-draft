# Stack implementation
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()

    def isEmpty(self):
        return len(self.items) == 0

def isBalanced(input_string):
    stack = Stack()
    opening = "({["
    closing = ")}]"
    
    for char in input_string:
        if char in opening:
            stack.push(char)
        elif char in closing:
            if stack.isEmpty():
                return False
            if opening.index(stack.pop()) != closing.index(char):
                return False
    
    return stack.isEmpty()

# Test cases
test_cases = [
    ("()", True),
    ("[{}]", True),
    ("({[]})", True),
    ("({})", False),
    ("[({})", False),
    ("([)]", False)
]

# Test the isBalanced function
for i, (input_string, expected) in enumerate(test_cases):
    result = isBalanced(input_string)
    print(f"Test case {i+1}: {input_string} => {result}, Expected: {expected}")
