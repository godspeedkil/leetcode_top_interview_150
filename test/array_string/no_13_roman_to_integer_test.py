from src.array_string.no_13_roman_to_integer import Solution

solution = Solution()

def test_normal_case():
    s = 'III'
    assert solution.romanToInt(s) == 3

def test_additional_case():
    s = 'LVIII'
    assert solution.romanToInt(s) == 58

def test_subtraction():
    s = 'MCMXCIV'
    assert solution.romanToInt(s) == 1994