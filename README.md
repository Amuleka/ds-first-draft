# Data Structures Tutorial: Stack

I. Introduction to Stacks
In computer science, a stack is a linear data structure that follows the Last-In-First-Out (LIFO) principle. It represents a collection of elements where the insertion and removal of items take place at one end called the top of the stack.
A stack can be visualized as a stack of books where the last book placed on top is the first one to be removed. The operations performed on a stack include inserting an item onto the stack (push), removing an item from the stack (pop), and accessing the top item without removal (peek).

# Stack Operations

A. Push Operation:

    The push operation adds an element to the top of the stack.
    Implementation: We can use the append() method of a Python list to add an item to the stack.

B. Pop Operation:

    The pop operation removes the top element from the stack and returns its value.
    Implementation: We can use the pop() method of a Python list to remove the last item from the stack.

C. Peek Operation:

    The peek operation returns the value of the top element without removing it from the stack.
    Implementation: We can access the last item in the Python list without removing it using indexing.

# Implementing a Stack using an Array or Linked List

A stack can be implemented using either an array or a linked list. In the exercise provided, we used an array-based implementation. Alternatively, a linked list can be used where each node in the linked list represents an element in the stack.

# Common Applications of Stacks

Stacks have various applications in computer science and software development, including:

    Function call stack in programming languages
    Expression evaluation and syntax parsing
    Undo and redo operations in text editors
    Backtracking algorithms
    Implementing recursive algorithms iteratively
    Managing system resources and memory allocation

# Time and Space Complexity Analysis

The time and space complexity of stack operations depend on the underlying implementation. In an array-based implementation, the time complexity of push, pop, and peek operations is O(1) since accessing the last element of an array takes constant time. Similarly, the space complexity is O(n) where n is the number of elements in the stack.

# Exercise: Implementing a Stack

In this exercise, let's explore how to implement a stack data structure using a Python list. We will focus on the fundamental operations of a stack: push, pop, peek, and checking if the stack is empty.

1. Create an empty stack using a Python list.
2. Implement the `push(item)` operation:
   - Take an item as input and add it to the top of the stack using the `append()` method of the list.
3. Implement the `pop()` operation:
   - Check if the stack is not empty.
   - Remove and return the topmost item from the stack using the `pop()` method of the list.
4. Implement the `peek()` operation:
   - Check if the stack is not empty.
   - Return the topmost item from the stack without removing it. You can access the last item in the list using indexing.
5. Implement the `is_empty()` operation:
   - Check if the stack is empty by verifying if the length of the list is 0.
6. Test your stack implementation by performing the following operations:
   - Push several items onto the stack.
   - Pop an item from the stack and verify the returned value.
   - Peek at the top item of the stack and verify the returned value.
   - Check if the stack is empty and verify the returned value.

Try to implement the stack operations and test them using different scenarios. Feel free to use the provided code structure as a starting point:

```python
# Create an empty stack
stack = []

# Implement stack operations
def push(item):
    # TODO: Implement the push operation
    pass

def pop():
    # TODO: Implement the pop operation
    pass

def peek():
    # TODO: Implement the peek operation
    pass

def is_empty():
    # TODO: Implement the is_empty operation
    pass

# Test the stack implementation
push(10)
push(20)
push(30)
print(pop())  # Expected output: 30
print(peek())  # Expected output: 20
print(is_empty())  # Expected output: False
```

# Challenge Time

Let's try your understaing by completing [this challenge](https://github.com/Amuleka/ds-first-draft/blob/main/first-draft-incomplete.py)

Please check the first-draft-complete file to [check the solution](https://github.com/Amuleka/ds-first-draft/blob/main/first-draft-complete.py).
