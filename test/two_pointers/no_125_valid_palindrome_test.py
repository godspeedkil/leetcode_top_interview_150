from src.two_pointers.no_125_valid_palindrome import Solution

solution = Solution()

def test_normal_case():
    s = 'rotator'
    assert solution.isPalindrome(s) == True

def test_non_alpha_chars():
    s = 'A man, a plan, a canal: Panama'
    assert solution.isPalindrome(s) == True

def test_negative_case():
    s = 'race a car'
    assert solution.isPalindrome(s) == False

def test_empty_string():
    s = ''
    assert solution.isPalindrome(s) == True