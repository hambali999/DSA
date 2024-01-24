# class Node(object):
#     def __init__(self, value):
#         self.value = value
#         self.nextnode = None


# a = Node(1)
# b = Node(2)
# c = Node(3)

# a.nextnode = b
# b.nextnode = c

# print(a.nextnode.value)


# a => b => c

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Udemy
class LinkedList:
    def __init__(self, value):
        new_node = Node(value) #creates the first node
        self.head = new_node
        self.tail = new_node
        self.length = 1

my_linked_list = LinkedList(4)

print(my_linked_list.head.value)