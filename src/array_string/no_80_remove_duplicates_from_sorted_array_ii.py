"""
Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
"""
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        result = 0
        nums_idx = 0
        for x in range(0, len(nums)):
            if (x == 0 or x == 1):
                nums_idx += 1
                result += 1
                continue
            curr_num = nums[x]
            # If there are aren't yet two instances of this number, go ahead and add to result
            if ((not nums[nums_idx-2] == curr_num) or (not nums[nums_idx-1] == curr_num)):
                nums[nums_idx] = curr_num
                nums_idx += 1
                result += 1
        return result