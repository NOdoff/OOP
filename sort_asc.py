from singly_list import SinglyList, Node
from print_list import print_list

def sort_asc(unsorted_list):
    n_list = unsorted_list
    node = list_head 
    if not isinstance(list_head, Node):
        print("This is not Node!")
        return
    unsorted_list = sorted(unsorted_list)

s_list = SinglyList()
a = Node(-1)
s_list.add_head(a)

node = s_list.head
b = Node(5)
c = Node(8)
d = Node(7)
a.next = b
b.next = c
c.next = d

# node = s_list.head
# for i in range(10):
#     node.next = Node(i)
#     node = node.next
s_list = sort_asc(s_list)
print_list(s_list.head)
