from src.array_string.no_58_length_of_last_word import Solution

solution = Solution()

def test_normal_case():
    s = 'Hello World'
    assert solution.lengthOfLastWord(s) == 5

def test_additional_case():
    s = '  fly me  to  the moon  '
    assert solution.lengthOfLastWord(s) == 4

def test_single_char():
    s = 'a'
    assert solution.lengthOfLastWord(s) == 1