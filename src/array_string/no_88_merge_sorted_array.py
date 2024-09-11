"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
"""
class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_left = nums1[:m]
        result_idx, nums1_idx, nums2_idx = 0, 0, 0

        while (result_idx < len(nums1)):
            # If we're out of elements in nums1
            if (nums1_idx >= len(nums1_left)):
                nums1[result_idx] = nums2[nums2_idx]
                nums2_idx += 1
            # If we're out of elements in nums2
            elif (nums2_idx >= len(nums2)):
                nums1[result_idx] = nums1_left[nums1_idx]
                nums1_idx += 1
            # If nums1 contains the next lowest element
            elif (nums1_left[nums1_idx] <= nums2[nums2_idx]):
                nums1[result_idx] = nums1_left[nums1_idx]
                nums1_idx += 1
            # If nums2 contains the next lowest element
            else:
                nums1[result_idx] = nums2[nums2_idx]
                nums2_idx += 1
            result_idx += 1