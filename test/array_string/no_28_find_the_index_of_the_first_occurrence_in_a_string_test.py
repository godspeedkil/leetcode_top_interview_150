from src.array_string.no_28_find_the_index_of_the_first_occurrence_in_a_string import Solution

solution = Solution()

def test_normal_case():
    haystack = 'sadbutsad'
    needle = 'sad'
    assert solution.strStr(haystack, needle) == 0

def test_negative_case():
    haystack = 'leetcode'
    needle = 'leeto'
    assert solution.strStr(haystack, needle) == -1

def test_multiple_starting_points():
    haystack = 'sssssadbutsad'
    needle = 'sad'
    assert solution.strStr(haystack, needle) == 4