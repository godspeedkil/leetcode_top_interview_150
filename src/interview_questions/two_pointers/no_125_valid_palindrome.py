"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        only_alpha = ""
        for char in s:
            if char.isalnum():
                only_alpha += char
        left, right = 0, len(only_alpha)-1
        while left < right:
            if only_alpha[left] != only_alpha[right]:
                return False
            left += 1
            right -= 1
        return True