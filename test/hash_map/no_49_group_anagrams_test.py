from src.interview_questions.hash_map.no_49_group_anagrams import Solution
from src.interview_questions.utils import compare_lists_of_lists_unordered

solution = Solution()

def test_case_1():
    strs = ['a']
    assert solution.groupAnagrams(strs) == [['a']]

def test_case_2():
    strs = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
    result = solution.groupAnagrams(strs)
    assert compare_lists_of_lists_unordered(result, [['bat'], ['nat', 'tan'], ['ate', 'eat', 'tea']])

def test_case_3():
    strs = ['']
    assert solution.groupAnagrams(strs) == [['']]