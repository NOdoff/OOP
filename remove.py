from singly_list import SinglyList, Node
from print_list import print_list

def remove(list_head, val):
    node = list_head
    prev_node = None
    if not isinstance(list_head, Node):
        print("This is not Node!")
        return
    if node.content == val:
        node.content = node.next.content
        node.next = node.next.next
        return
    boo = True
    while boo:
        prev_node = node
        node = node.next
        if node.content == val:
            prev_node.next = node.next
            boo = False
        elif node.next == None:
            boo = False
        #else:
    #        prev_node = node
    #        node = node.next


if __name__ == '__main__':
    s_list = SinglyList()
    s_list.add_head(Node(-1))

    node = s_list.head
    for i in range(10):
        node.next = Node(i)
        node = node.next

    print_list(s_list.head)
    remove(s_list.head, 2)
    print_list(s_list.head)
