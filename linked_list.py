class Node:

    def __init__(self,value=None):
        self.value = value
        self.next = None

class SinglyLinkedList:

    def __init__(self):
        self.head = None

    def append(self,value):
        new_node = Node(value)  
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node 

    def print_list(self):
        current = self.head
        while current:
            print(current.value, end= "->" if current.next else "\n")
            current = current.next




