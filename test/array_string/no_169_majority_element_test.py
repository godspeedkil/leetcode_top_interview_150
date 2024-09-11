from src.array_string.no_169_majority_element import Solution

solution = Solution()

def test_normal_case():
    nums = [3,2,3]
    assert solution.majorityElement(nums) == 3

def test_additional_case():
    nums = [2,2,1,1,1,2,2]
    assert solution.majorityElement(nums) == 2

def test_single_element():
    nums = [1]
    assert solution.majorityElement(nums) == 1