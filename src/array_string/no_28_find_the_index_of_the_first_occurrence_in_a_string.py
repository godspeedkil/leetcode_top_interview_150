"""
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
"""
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                offset = 0
                valid = True
                while valid:
                    if offset >= len(needle):
                        return i
                    if i + offset >= len(haystack) or haystack[i+offset] != needle[offset]:
                        valid = False
                    offset += 1
        return -1