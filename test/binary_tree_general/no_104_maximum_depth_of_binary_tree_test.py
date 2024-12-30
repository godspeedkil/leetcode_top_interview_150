from src.interview_questions.binary_tree_general.no_104_maximum_depth_of_binary_tree import Solution
from src.interview_questions.utils import TreeNode

solution = Solution()

def test_case_1():
    node_5 = TreeNode(val=7)
    node_4 = TreeNode(val=15)
    node_3 = TreeNode(val=20, left=node_4, right=node_5)
    node_2 = TreeNode(val=9)
    node_1 = TreeNode(val=3, left=node_2, right=node_3)
    assert solution.maxDepth(node_1) == 3

def test_case_2():
    node_2 = TreeNode(val=2)
    node_1 = TreeNode(val=1, right=node_2)
    assert solution.maxDepth(node_1) == 2