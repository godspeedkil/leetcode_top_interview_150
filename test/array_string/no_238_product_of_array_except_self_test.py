from src.array_string.no_238_product_of_array_except_self import Solution

solution = Solution()

def test_normal_case():
    nums = [1,2,3,4]
    assert solution.productExceptSelf(nums) == [24,12,8,6]

def test_additional_case():
    nums = [-1,1,0,-3,3]
    assert solution.productExceptSelf(nums) == [0,0,9,0,0]