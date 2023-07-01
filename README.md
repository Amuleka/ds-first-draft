Data Structures Tutorial: Stack

I. Introduction to Stacks

In computer science, a stack is a linear data structure that follows the Last-In-First-Out (LIFO) principle. It represents a collection of elements where the insertion and removal of items take place at one end called the top of the stack.

A stack can be visualized as a stack of books where the last book placed on top is the first one to be removed. The operations performed on a stack include inserting an item onto the stack (push), removing an item from the stack (pop), and accessing the top item without removal (peek).

II. Stack Operations

A. Push Operation:
• The push operation adds an element to the top of the stack.
• Implementation: We can use the append() method of a Python list to add an item to the stack.

B. Pop Operation:
• The pop operation removes the top element from the stack and returns its value.
• Implementation: We can use the pop() method of a Python list to remove the last item from the stack.

C. Peek Operation:
• The peek operation returns the value of the top element without removing it from the stack.
• Implementation: We can access the last item in the Python list without removing it using indexing.

III. Implementing a Stack using an Array or Linked List

A stack can be implemented using either an array or a linked list. In the exercise provided, we used an array-based implementation. Alternatively, a linked list can be used where each node in the linked list represents an element in the stack.

IV. Common Applications of Stacks

Stacks have various applications in computer science and software development, including:

• Function call stack in programming languages
• Expression evaluation and syntax parsing
• Undo and redo operations in text editors
• Backtracking algorithms
• Implementing recursive algorithms iteratively
• Managing system resources and memory allocation

V. Time and Space Complexity Analysis

The time and space complexity of stack operations depend on the underlying implementation. In an array-based implementation, the time complexity of push, pop, and peek operations is O(1) since accessing the last element of an array takes constant time. Similarly, the space complexity is O(n) where n is the number of elements in the stack.

VI. Challenge Time

'''
You are given a string containing parentheses (, ), brackets [, ], and curly braces {, }.
Write a function that determines if the input string has balanced parentheses.
A string with balanced parentheses has every opening parentheses, bracket,
or brace matched with a closing one of the same type and in the correct order.
'''

Stack implementation

class Stack:
def **init**(self): # Initialize the stack
pass

    def push(self, item):
        # Add an item to the stack
        pass

    def pop(self):
        # Remove and return the top item from the stack
        pass

    def isEmpty(self):
        # Check if the stack is empty
        pass

def isBalanced(input_string):
stack = Stack()
opening = "({["
closing = ")}]"

    for char in input_string:
        if char in opening:
            # TODO: Implement the logic to push opening parentheses onto the stack
            pass
        elif char in closing:
            if stack.isEmpty():
                # TODO: Handle the case when the stack is empty but a closing parenthesis is encountered
                pass
            if opening.index(stack.pop()) != closing.index(char):
                # TODO: Handle the case when the popped character doesn't match the current closing parenthesis
                pass

    return stack.isEmpty()

Test cases

test_cases = [
("()", True),
("[{}]", True),
("({[]})", True),
("({})", False),
("[({})", False),
("([)]", False)
]

Test the isBalanced function

for i, (input_string, expected) in enumerate(test_cases):
result = isBalanced(input_string)
print(f"Test case {i+1}: {input_string} => {result}, Expected: {expected}")

Please check the first-draft-complete file to check the solution.
