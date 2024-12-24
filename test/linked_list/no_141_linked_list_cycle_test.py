from src.interview_questions.linked_list.no_141_linked_list_cycle import Solution
from src.interview_questions.utils import ListNode

solution = Solution()

def test_true_case_1():
    node_1 = ListNode(3)
    node_2 = ListNode(2)
    node_3 = ListNode(0)
    node_4 = ListNode(-4)
    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    node_4.next = node_2
    assert solution.hasCycle(node_1)

def test_true_case_2():
    node_1 = ListNode(1)
    node_2 = ListNode(2)
    node_1.next = node_2
    node_2.next = node_1
    assert solution.hasCycle(node_1)

def test_false_case_1():
    assert not solution.hasCycle(None)

def test_false_case_2():
    node_1 = ListNode(1)
    assert not solution.hasCycle(node_1)