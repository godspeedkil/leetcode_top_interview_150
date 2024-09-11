from src.array_string.no_88_merge_sorted_array import Solution

solution = Solution()

def test_normal_case():
    nums1 = [1,2,3,0,0,0]
    nums2 = [2,5,6]
    solution.merge(nums1, 3, nums2, 3)
    assert nums1 == [1,2,2,3,5,6]

def test_second_list_empty():
    nums1 = [1]
    nums2 = []
    solution.merge(nums1, 1, nums2, 0)
    assert nums1 == [1]

def test_first_list_empty():
    nums1 = [0]
    nums2 = [1]
    solution.merge(nums1, 0, nums2, 1)
    assert nums1 == [1]