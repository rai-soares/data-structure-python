from node import Node

class Queue:
    def __init__(self, debug=False):
        self.first = None
        self.last = None
        self.debug = debug

    def add(self, data):
        new_node = Node(data=data)

        if self.first == None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next_node = new_node
            self.last = new_node

        if self.debug:
            print(f"Insert value {data} at the end of the queue")

    def remove(self):
        if self.first == None:
            raise Exception('Queue is empty')
        else:
            if self.debug:
                print(f"Remove value {self.first.data} at the init of the queue")
                
            self.first = self.first.next_node
            if self.first == None:
                self.last = None
            

# Create a queue
my_queue = Queue(debug=True)

# Add to queue
for i in range(1, 5):
    my_queue.add(f"Test {i}")

# Remove from queue
for i in range(1, 4):
    my_queue.remove()