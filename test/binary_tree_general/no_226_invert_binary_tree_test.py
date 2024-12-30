from src.interview_questions.binary_tree_general.no_226_invert_binary_tree import Solution
from src.interview_questions.utils import TreeNode, verify_binary_tree_inorder

solution = Solution()

def test_case_1():
    node_7 = TreeNode(val=9)
    node_6 = TreeNode(val=6)
    node_5 = TreeNode(val=3)
    node_4 = TreeNode(val=1)
    node_3 = TreeNode(val=7, left=node_6, right=node_7)
    node_2 = TreeNode(val=2, left=node_4, right=node_5)
    node_1 = TreeNode(val=4, left=node_2, right=node_3)
    assert verify_binary_tree_inorder(node_1, [1,2,3,4,6,7,9])
    inverted = solution.invertTree(node_1)
    assert verify_binary_tree_inorder(inverted, [9,7,6,4,3,2,1])

def test_case_2():
    node_3 = TreeNode(val=3)
    node_2 = TreeNode(val=1)
    node_1 = TreeNode(val=2, left=node_2, right=node_3)
    assert verify_binary_tree_inorder(node_1, [1,2,3])
    inverted = solution.invertTree(node_1)
    assert verify_binary_tree_inorder(inverted, [3,2,1])

def test_case_3():
    node_1 = None
    assert verify_binary_tree_inorder(node_1, list())
    inverted = solution.invertTree(node_1)
    assert verify_binary_tree_inorder(node_1, list())