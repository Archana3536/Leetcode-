# Rotate Linked List (User Input)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Create linked list from input
def create_list(arr):
    if not arr:
        return None
    head = Node(arr[0])
    temp = head
    for i in range(1, len(arr)):
        temp.next = Node(arr[i])
        temp = temp.next
    return head


# Rotate function
def rotate_list(head, k):
    if not head or not head.next:
        return head

    # Find length
    temp = head
    length = 1
    while temp.next:
        temp = temp.next
        length += 1

    # Make circular
    temp.next = head

    # Reduce k
    k = k % length

    # Find new tail (length - k steps)
    steps = length - k
    new_tail = head

    for _ in range(steps - 1):
        new_tail = new_tail.next

    # New head
    new_head = new_tail.next
    new_tail.next = None

    return new_head


# Print linked list
def print_list(head):
    temp = head
    while temp:
        print(temp.data, end=" -> ")
        temp = temp.next
    print("None")


# -------- USER INPUT --------
arr = list(map(int, input("Enter elements: ").split()))
k = int(input("Enter k: "))

head = create_list(arr)
new_head = rotate_list(head, k)

print("Rotated List:")
print_list(new_head)



# Enter elements: 1 2 3 4 5
# Enter k: 2
# Rotated List:
# 4 -> 5 -> 1 -> 2 -> 3 -> None