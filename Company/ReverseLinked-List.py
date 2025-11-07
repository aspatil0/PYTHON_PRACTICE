class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse_linked_list(head):
    prev = None
    curr = head

    while curr:
        next_node = curr.next   
        curr.next = prev        
        prev = curr             
        curr = next_node        

    return prev   

def print_list(node):
    while node:
        print(node.data, end=" → ")
        node = node.next
    print("NULL")

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

print("Original list:")
print_list(head)

head = reverse_linked_list(head)

print("Reversed list:")
print_list(head)
