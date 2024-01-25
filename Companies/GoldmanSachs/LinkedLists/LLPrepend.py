class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
            
    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node #current node tail to new node
            self.tail = new_node #now tail to be at new node
        self.length += 1
        
    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while (temp.next): #when temp.next is none then stop the loop
            pre = temp
            temp = temp.next
        self.tail = pre #to the previous Node
        self.tail.next = None #since no next node, put None, cos POP
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    
    
my_linked_list = LinkedList(2)
my_linked_list.append(3)
my_linked_list.prepend(1)
my_linked_list.print_list()