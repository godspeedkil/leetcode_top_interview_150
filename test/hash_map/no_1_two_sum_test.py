from src.hash_map.no_1_two_sum import Solution

solution = Solution()

def test_case():
    nums = [2,7,11,15]
    target = 9
    assert solution.twoSum(nums, target) == [0,1]

def test_case_2():
    nums = [3,2,4]
    target = 6
    assert solution.twoSum(nums, target) == [1,2]

def test_case_3():
    nums = [3,3]
    target = 6
    assert solution.twoSum(nums, target) == [0,1]