from src.array_string.no_27_remove_element import Solution

solution = Solution()

def validate(nums, val, expected_nums):
    k = len(expected_nums)
    assert k == solution.removeElement(nums, val)
    result_nums = nums[:k]
    result_nums.sort()
    for i in range(k):
        assert nums[i] == expected_nums[i]

def test_normal_case():
    nums = [3,2,2,3]
    val = 3
    expected_nums = [2,2]
    validate(nums, val, expected_nums)

def test_additional_case():
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    expected_nums = [0,1,3,0,4]
    validate(nums, val, expected_nums)

def test_empty_nums():
    nums = []
    val = 0
    expected_nums = []
    validate(nums, val, expected_nums)