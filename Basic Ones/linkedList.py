def cycle(head):
	slow = head
	fast = head

	while fast is not None and fast.next is not None:
		fast = fast.next.next
		slow = slow.next

		if slow == fast:
			return True
		return False


class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


parent = Node(1)
child = Node(2, parent)
parent.next = child
print(cycle(parent))
