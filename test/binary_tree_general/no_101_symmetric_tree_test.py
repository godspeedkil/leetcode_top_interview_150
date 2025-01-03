from src.interview_questions.binary_tree_general.no_101_symmetric_tree import Solution
from src.interview_questions.utils import TreeNode

solution = Solution()

def test_case_true():
    node_7 = TreeNode(val=3)
    node_6 = TreeNode(val=4)
    node_5 = TreeNode(val=4)
    node_4 = TreeNode(val=3)
    node_3 = TreeNode(val=2, left=node_6, right=node_7)
    node_2 = TreeNode(val=2, left=node_4, right=node_5)
    node_1 = TreeNode(val=1, left=node_2, right=node_3)
    assert solution.isSymmetric(node_1)

def test_case_false():
    node_5 = TreeNode(val=3)
    node_4 = TreeNode(val=3)
    node_3 = TreeNode(val=2, right=node_5)
    node_2 = TreeNode(val=2, right=node_4)
    node_1 = TreeNode(val=1, left=node_2, right=node_3)
    assert not solution.isSymmetric(node_1)