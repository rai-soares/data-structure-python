from typing import List

class Stack:
    __stack: List = []
    
    def __init__(self, debug=False):
        self.debug = debug
        if self.debug:
            print("Stack has been created")

    def get_stack(self):
        return self.__stack

    def add(self, item):
        self.__stack.append(item)
        if self.debug:
            print(f"{item} has been added to stack")

    def remove(self):
        if len(self.__stack) > 0:
            removed_item = self.__stack.pop()
            if self.debug:
                print(f"{removed_item} has been removed to stack")
        else:
            raise Exception('Stack is empty')
        

# Create Stack
my_stack = Stack(debug=True)

# Add items to Stack
my_stack.add('Test 1')
my_stack.add('Test 2')
my_stack.add('Test 3')
my_stack.add('Test 4')

# Remove items from Stack
my_stack.remove()
my_stack.remove()
my_stack.remove()

# Show the Stack
print(my_stack.get_stack())