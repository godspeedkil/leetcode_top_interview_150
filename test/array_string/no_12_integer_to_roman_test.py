from src.array_string.no_12_integer_to_roman import Solution

solution = Solution()

def test_normal_case():
    num = 58
    assert solution.intToRoman(num) == 'LVIII'

def test_subtractive_case():
    num = 1994
    assert solution.intToRoman(num) == 'MCMXCIV'

def test_additional_subtractive_case():
    num = 3749
    assert solution.intToRoman(num) == 'MMMDCCXLIX'