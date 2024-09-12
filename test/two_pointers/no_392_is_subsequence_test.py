from src.two_pointers.no_392_is_subsequence import Solution

solution = Solution()

def test_normal_case():
    s = 'abc'
    t = 'ahbgdc'
    assert solution.isSubsequence(s, t) == True

def test_negative_case():
    s = 'axc'
    t = 'ahbgdc'
    assert solution.isSubsequence(s, t) == False

def test_empty_sequence():
    s = ''
    t = ''
    assert solution.isSubsequence(s, t) == True