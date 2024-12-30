from src.interview_questions.binary_tree_general.no_100_same_tree import Solution
from src.interview_questions.utils import TreeNode

solution = Solution()

def test_true_case():
    node_1_3 = TreeNode(val=3)
    node_1_2 = TreeNode(val=2)
    node_1_1 = TreeNode(val=1, left=node_1_2, right=node_1_3)
    node_2_3 = TreeNode(val=3)
    node_2_2 = TreeNode(val=2)
    node_2_1 = TreeNode(val=1, left=node_2_2, right=node_2_3)
    assert solution.isSameTree(node_1_1, node_2_1)

def test_false_case_1():
    node_1_2 = TreeNode(val=2)
    node_1_1 = TreeNode(val=1, left=node_1_2)
    node_2_2 = TreeNode(val=2)
    node_2_1 = TreeNode(val=1, right=node_2_2)
    assert not solution.isSameTree(node_1_1, node_2_1)

def test_false_case_2():
    node_1_3 = TreeNode(val=1)
    node_1_2 = TreeNode(val=2)
    node_1_1 = TreeNode(val=1, left=node_1_2, right=node_1_3)
    node_2_3 = TreeNode(val=2)
    node_2_2 = TreeNode(val=1)
    node_2_1 = TreeNode(val=1, left=node_2_2, right=node_2_3)
    assert not solution.isSameTree(node_1_1, node_2_1)