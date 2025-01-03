from src.interview_questions.binary_tree_general.no_112_path_sum import Solution
from src.interview_questions.utils import TreeNode

solution = Solution()

def test_true_case():
    node_9 = TreeNode(val=1)
    node_8 = TreeNode(val=2)
    node_7 = TreeNode(val=7)
    node_6 = TreeNode(val=4, right=node_9)
    node_5 = TreeNode(val=13)
    node_4 = TreeNode(val=11, left=node_7, right=node_8)
    node_3 = TreeNode(val=8, left=node_5, right=node_6)
    node_2 = TreeNode(val=4, left=node_4)
    node_1 = TreeNode(val=5, left=node_2, right=node_3)
    assert solution.hasPathSum(node_1, 22)

def test_false_case_1():
    node_3 = TreeNode(val=3)
    node_2 = TreeNode(val=2)
    node_1 = TreeNode(val=1, left=node_2, right=node_3)
    assert not solution.hasPathSum(node_1, 5)

def test_false_case_2():
    assert not solution.hasPathSum(None, 0)