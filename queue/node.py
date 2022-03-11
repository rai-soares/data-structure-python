# This class represents one node of a doubly linked structure
class Node:
    def __init__(self, data=0, next_node=None):
        # print("pass:" + str(data))
        self.data = data
        self.next_node = next_node