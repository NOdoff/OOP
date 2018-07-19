from singly_list import SinglyList, Node
from print_list import print_list

def add_tail(list_head, val):
    node = list_head
    if not isinstance(list_head, Node):
        print("This is not Node!")
        return
    while node.next is not None:
        node = node.next
    node.next = Node(val)

s_list = SinglyList()
s_list.add_head(Node(-1))

node = s_list.head
for i in range(10):
    node.next = Node(i)
    node = node.next

# node = s_list.head
# b = Node(5)
# c = Node(8)
# d = Node(7)
# a.next = b
# b.next = c
# c.next = d

print_list(s_list)
add_tail(s_list.head, 19)
add_tail(None, 19)
print_list(s_list)
