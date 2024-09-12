from src.array_string.no_14_longest_common_prefix import Solution

solution = Solution()

def test_normal_case():
    strs = ['flower','flow','flight']
    assert solution.longestCommonPrefix(strs) == 'fl'

def test_no_common_prefix():
    strs = ['dog','racecar','car']
    assert solution.longestCommonPrefix(strs) == ''

def test_single_empty_element():
    strs = ['']
    assert solution.longestCommonPrefix(strs) == ''

def test_multiple_empty_elements():
    strs = ['', '']
    assert solution.longestCommonPrefix(strs) == ''