"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()

        result = set()
        for i in range(len(nums)-2):
            fixed = nums[i]
            left = i + 1
            right = len(nums) - 1
            while left < right:
                two_sum = nums[left] + nums[right]
                if two_sum + fixed == 0:
                    result.add(tuple([nums[i], nums[left], nums[right]]))
                if (two_sum + fixed) < 0:
                    left += 1
                else:
                    right -= 1
        return result