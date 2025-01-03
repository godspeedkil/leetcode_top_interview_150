from src.interview_questions.one_d_dp.no_70_climbing_stairs import Solution

solution = Solution()

def test_case_1():
    n = 2
    assert solution.climbStairs(n) == 2

def test_case_2():
    n = 3
    assert solution.climbStairs(n) == 3