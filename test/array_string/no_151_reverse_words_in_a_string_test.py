from src.array_string.no_151_reverse_words_in_a_string import Solution

solution = Solution()

def test_normal_case():
    s = 'the sky is blue'
    assert solution.reverseWords(s) == 'blue is sky the'

def test_trailing_and_leading_whitespaces():
    s = '  hello world  '
    assert solution.reverseWords(s) == 'world hello'

def test_multiple_internal_whitespaces():
    s = 'a good   example'
    assert solution.reverseWords(s) == 'example good a'