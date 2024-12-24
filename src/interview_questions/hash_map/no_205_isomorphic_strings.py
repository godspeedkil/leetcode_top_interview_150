"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 
Example 1:

Input: s = "egg", t = "add"

Output: true

Explanation:

The strings s and t can be made identical by:

Mapping 'e' to 'a'.
Mapping 'g' to 'd'.
Example 2:

Input: s = "foo", t = "bar"

Output: false

Explanation:

The strings s and t can not be made identical as 'o' needs to be mapped to both 'a' and 'r'.

Example 3:

Input: s = "paper", t = "title"

Output: true


Constraints:

1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.
"""
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        translation_s = {}
        for i in range(len(s)):
            known = translation_s.get(s[i], '')
            if (known == '' or known == t[i]):
                translation_s[s[i]] = t[i]
            else:
                return False
        translation_t = {}
        for i in range(len(t)):
            known = translation_t.get(t[i], '')
            if (known == '' or known == s[i]):
                translation_t[t[i]] = s[i]
            else:
                return False
        return True