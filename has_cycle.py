from singly_list import SinglyList, Node
from print_list import print_list

def has_cycle(list_head):
    node = list_head

    if not isinstance(list_head, Node):
        print("This is not Node!")
        return
    boo = True
    while boo:
        # if node.next != None:
        #     node = node.next
        # else:
        if node.next == list_head:
            print("True")
            boo = False
        elif node.next == None:
            print ("False")
            boo = False
        node = node.next
if __name__ == '__main__':
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
    d.next = a
    # node = s_list.head
    # for i in range(10):
    #     node.next = Node(i)
    #     node = node.next
    #
    # save_head = s_list.head
    # while node:
    #     if node.next == None:
    #         node.next = save_head
    #         break
    node = node.next
    has_cycle(s_list.head)
