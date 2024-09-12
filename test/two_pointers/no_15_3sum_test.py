from src.two_pointers.no_15_3sum import Solution

solution = Solution()

def test_normal_case():
    nums = [-1,0,1,2,-1,-4]
    assert solution.threeSum(nums) == {(-1,-1,2), (-1,0,1)}

def test_single_solution():
    nums = [0,0,0]
    assert solution.threeSum(nums) == {(0,0,0)}

def test_no_solution():
    nums = [0,1,1]
    assert solution.threeSum(nums) == set()