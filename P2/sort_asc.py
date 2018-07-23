from singly_list import SinglyList, Node
from print_list import print_list


def sort_asc(unsorted_list):
    s_list = unsorted_list
    node = unsorted_list.head
    if not isinstance(unsorted_list.head, Node):
        print("This is not Node!")
        return
    boo = True
    swapped = False
    while boo:

        if node.next == None:
            if swapped:
                node = unsorted_list.head
                swapped = False
            else:
                boo = False

        elif node.content > node.next.content:
            holder = node.content
            node.content = node.next.content
            node.next.content = holder
            node = node.next
            swapped = True
        else:
            node = node.next
    return unsorted_list

if __name__ == '__main__':
    s_list = SinglyList()
    a = Node(-1)
    s_list.add_head(a)

    node = s_list.head
    b = Node(9)
    c = Node(8)
    d = Node(7)
    a.next = b
    b.next = c
    c.next = d

    # node = s_list.head
    # for i in range(10):
    #     node.next = Node(i)
    #     node = node.next

    print_list(s_list.head)
    s_list = sort_asc(s_list)
    print_list(s_list.head)
