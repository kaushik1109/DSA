class Node:
    def __init__(self,value):
        self.value = value
        self.prev = None
        self.next = None

def create_linked_list(values):
    head = Node(values[0])

    current = head
    for value in values[1:]:
        new_node = Node(value)
        current.next = new_node
        new_node.prev = current
        current = current.next
    
    return head, current

def print_linked_list(head):
    current = head
    while current:
        print(f"{current.value} -> ", end="")
        current = current.next
    print("END")

def print_linked_list_backwards(tail):
    current = tail
    while current:
        print(f"{current.value} -> ", end="")
        current = current.prev
    print("END")


# Main execution

values = [2,4,1,5,6]
head, tail = create_linked_list(values)
print_linked_list(head)
print_linked_list_backwards(tail)


        

