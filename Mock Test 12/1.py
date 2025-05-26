'''
Write a Python program to implement a class 'Stack'
Include methods to 
1. push an element (insert an element in the topmost position)
2. pop an element (delete the topmost element and return it)
3. peek (return the topmost element)
4. check the size of the stack (return the length)
5. check whether the stack is empty or not (return True or False).
Sample Input:
2,4,6,8
Sample Output:
8
6
3
False
'''

#Code starts here

x=[int(i) for i in input().split(',')]

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def size(self):
        return len(self.items)

    def is_empty(self):
        return len(self.items) == 0

s=Stack()

for i in x:
    s.push(i)

print(s.pop())

print(s.peek())

print(s.size())

print(s.is_empty())
#Code ends here 