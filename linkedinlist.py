'''This is my code'''

class Node:
    "first class"
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    "second class" 
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

my_linked_list = LinkedList(4)

print(my_linked_list.head.value)  # Output: 4
