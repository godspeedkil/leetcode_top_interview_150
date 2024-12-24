from src.interview_questions.hash_map.no_202_happy_number import Solution

solution = Solution()

def test_true_case():
    n = 19
    assert solution.isHappy(n)

def test_false_case():
    n = 2
    assert not solution.isHappy(n)