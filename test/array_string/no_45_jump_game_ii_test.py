from src.array_string.no_45_jump_game_ii import Solution

solution = Solution()

def test_normal_case():
    nums = [2,3,1,1,4]
    assert solution.jump(nums) == 2

def test_additional_case():
    nums = [2,3,0,1,4]
    assert solution.jump(nums) == 2

def test_single_element():
    nums = [0]
    assert solution.jump(nums) == 0