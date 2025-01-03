from src.interview_questions.binary_tree_general.no_222_count_complete_tree_nodes import Solution
from src.interview_questions.utils import TreeNode

solution = Solution()

def test_case_1():
    node_6 = TreeNode(val=6)
    node_5 = TreeNode(val=5)
    node_4 = TreeNode(val=4)
    node_3 = TreeNode(val=3, left=node_6)
    node_2 = TreeNode(val=2, left=node_4, right=node_5)
    node_1 = TreeNode(val=1, left=node_2, right=node_3)
    assert solution.countNodes(node_1) == 6

def test_case_2():
    assert solution.countNodes(None) == 0

def test_case_3():
    node_1 = TreeNode(val=1)
    assert solution.countNodes(node_1) == 1