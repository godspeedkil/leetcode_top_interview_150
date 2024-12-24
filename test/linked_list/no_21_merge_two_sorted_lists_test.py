from src.interview_questions.linked_list.no_21_merge_two_sorted_lists import Solution
from src.interview_questions.utils import ListNode, verify_linked_list

solution = Solution()

def test_case_1():
    node_1_1 = ListNode(1)
    node_1_2 = ListNode(2)
    node_1_3 = ListNode(3)
    node_1_1.next = node_1_2
    node_1_2.next = node_1_3
    node_2_1 = ListNode(1)
    node_2_2 = ListNode(3)
    node_2_3 = ListNode(4)
    node_2_1.next = node_2_2
    node_2_2.next = node_2_3
    head = solution.mergeTwoLists(node_1_1, node_2_1)
    verify_linked_list(head, [1,1,2,3,4,4])