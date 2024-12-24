"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
"""
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        current_candidate = None
        current_count = 0
        for num in nums:
            if (current_count == 0):
                current_candidate = num
            if (num == current_candidate):
                current_count += 1
            else:
                current_count -= 1
        return current_candidate