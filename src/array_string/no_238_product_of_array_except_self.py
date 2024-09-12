"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
"""
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        answer = [0] * n

        answer[0] = 1
        for i in range(1, n):
            answer[i] = nums[i-1] * answer[i-1]

        right = 1
        for i in range(n-1, -1, -1):
            answer[i] = answer[i] * right
            right *= nums[i]
        
        return answer