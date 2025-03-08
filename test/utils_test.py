from src.interview_questions.utils import *

def test_verify_linked_list_empty():
    linked_list = None
    assert verify_linked_list(linked_list, list())

def test_verify_linked_list_case_1():
    linked_list = ListNode(1)
    assert verify_linked_list(linked_list, [1])

def test_verify_linked_list_case_2():
    node_1 = ListNode(1)
    node_2 = ListNode(2)
    node_3 = ListNode(3)
    node_1.next = node_2
    node_2.next = node_3
    assert verify_linked_list(node_1, [1,2,3])

def test_verify_binary_tree_inorder_case_1():
    assert verify_binary_tree_inorder(None, list())

def test_verify_binary_tree_inorder_case_2():
    node_1 = TreeNode(val=1)
    assert verify_binary_tree_inorder(node_1, [1])

def test_verify_binary_tree_inorder_case_3():
    node_2 = TreeNode(val=2)
    node_1 = TreeNode(val=1, left=node_2)
    assert verify_binary_tree_inorder(node_1, [2,1])

def test_verify_binary_tree_inorder_case_4():
    node_2 = TreeNode(val=2)
    node_1 = TreeNode(val=1, right=node_2)
    assert verify_binary_tree_inorder(node_1, [1,2])

def test_verify_binary_tree_inorder_case_5():
    node_3 = TreeNode(val=3)
    node_2 = TreeNode(val=2)
    node_1 = TreeNode(val=1, left=node_2, right=node_3)
    assert verify_binary_tree_inorder(node_1, [2,1,3])    

def test_verify_compare_lists_of_lists_unordered():
    list1 = [['tan', 'nat']]
    list2 = [['nat', 'tan']]
    assert compare_lists_of_lists_unordered(list1, list2)