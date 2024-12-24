"""
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.


Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
 

Constraints:

1 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
0 <= k <= 10^5
"""
class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        known_indexes = {}
        n = len(nums)
        for i in range(n):
            num = nums[i]
            known = known_indexes.get(num)
            if known is not None and (i-known) <= k:
                return True
            known_indexes[num] = i
        return False