from singly_list import SinglyList, Node

def print_list(list_head):
    node = list_head

    print("{ ", end="")
    while node is not None:
        print("[", end = "")
        end = "], " if node.next else "]"
        print(node.content, end = end, flush = True)
        node = node.next
    print(" }")


if __name__ == "__main__":
    s_list = SinglyList()
    a = Node(-1)
    s_list.add_head(a)

    # node = s_list.head
    # b = Node(5)
    # c = Node(8)
    # d = Node(7)
    # a.next = b
    # b.next = c
    # c.next = d

    node = s_list.head
    for i in range(10):
        node.next = Node(i)
        node = node.next

    print_list(s_list.head)
