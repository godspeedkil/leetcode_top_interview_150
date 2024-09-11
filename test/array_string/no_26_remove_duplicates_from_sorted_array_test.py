from src.array_string.no_26_remove_duplicates_from_sorted_array import Solution

solution = Solution()

def validate(nums, expected_nums):
    k = len(expected_nums)
    assert k == solution.removeDuplicates(nums)
    result_nums = nums[:k]
    result_nums.sort()
    for i in range(k):
        assert nums[i] == expected_nums[i]

def test_normal_case():
    nums = [1,1,2]
    expected_nums = [1,2]
    validate(nums, expected_nums)

def test_additional_case():
    nums=[0,0,1,1,1,2,2,3,3,4]
    expected_nums = [0,1,2,3,4]
    validate(nums, expected_nums)

def test_empty_nums():
    nums=[]
    expected_nums = []
    validate(nums, expected_nums)