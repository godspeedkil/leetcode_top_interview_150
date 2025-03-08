from collections import Counter

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def verify_linked_list(head: ListNode, expected: list) -> bool:
    while head:
        if head.val != expected.pop(0):
            return False
        head = head.next
    return len(expected) == 0

def verify_binary_tree_inorder(root: TreeNode, expected: list) -> bool:
    if root and root.left:
        verify_binary_tree_inorder(root.left, expected)
    if root and root.val != expected.pop(0):
        return False
    if root and root.right:
        verify_binary_tree_inorder(root.right, expected)
    return True
        
def compare_lists_of_lists_unordered(list1: list[list], list2: list[list]) -> bool:
    set1 = set()
    for ls in list1:
        set1.add(frozenset(ls))
    set2 = set()
    for ls in list2:
        set2.add(frozenset(ls))
    return set1 == set2