# first we define a ode class that we will use to create every node in the linked list, we will take care about the linking part ;ater.

# Assume we have an array of values as inpit, we have to create a linked list out of that array

# Define the Node class with 2 parmeters, one is the value and the pointer to next

class Node:
    def __init__(self, data):
        self.value = data
        self.next = None

def create_linked_list(values):
        head = Node(values[0])
        current = head

        # Now run for oop from 2nd element to last

        for i in range (1, len(values)):
            new_node = Node(values[i])
            current.next = new_node
            current = new_node

        return head

def print_linked_list(head):
    current = head
    while current:
        print(f"{current.value} -> ", end="")
        current = current.next
    print("END")

def insert_element_at_head(value, head):
    new_node = Node(value)
    new_node.next = head
    head = new_node
    return head

def insert_element_at_tail(value, head):
    current = head
    while current.next is not None:
         current = current.next
    new_node = Node(value)
    current.next = new_node
    tail = new_node

    return tail

def delete_head(head):
    head = head.next
    return head

def delete_tail(head):
    current = head

    while current.next:
        current = current.next

    element = current.next.value
    current.next = None
    return element
    
    
        

# Main execution

values = [1,2,3,4,5]

head = create_linked_list(values)

print_linked_list(head)

head = insert_element_at_head(7, head)

print_linked_list(head)

tail = insert_element_at_tail(9, head)

print_linked_list(head)

# Main for deleting an element from lINKED list

# First let us try deleting the first element from lINKED list

new_head = delete_head(head)
print_linked_list(new_head)

# Now let us delete the tail of the linkedlist

deleted_element = delete_tail(head)
print(f"We have deleted element {element} from Linked list")







    