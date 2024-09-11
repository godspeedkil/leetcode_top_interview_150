from src.array_string.no_55_jump_game import Solution

solution = Solution()

def test_normal_case():
    nums = [2,3,1,1,4]
    assert solution.canJump(nums) == True

def test_additional_case():
    nums = [3,2,1,0,4]
    assert solution.canJump(nums) == False

def test_single_element():
    nums = [0]
    assert solution.canJump(nums) == True