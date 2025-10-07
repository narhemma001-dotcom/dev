class Node:
    
    def __init__(self, next=None, value=None, head = None):
        self.value = value
        self.next = next
        self.head = head

    def append(self, value):
        new_node = Node(value)

        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node 
        
        
    def prepend(self,value):  
        new_node = Node(value)

        current = self.head
        new_node.next = current
        self.head = new_node
  

    def print_list(self):
        current = self.head
        while current:
           print(current.value, end= "->" if current.next else "\n" )        

linked = Node()

linked.append(3)
linked.prepend(12)
linked.print_list()
            




            
         

