class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def verify_linked_list(head: ListNode, expected: list) -> bool:
    while head:
        if head.val != expected.pop(0):
            return False
        head = head.next
    return len(expected) == 0