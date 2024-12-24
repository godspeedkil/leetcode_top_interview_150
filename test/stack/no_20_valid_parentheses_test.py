from src.interview_questions.stack.no_20_valid_parentheses import Solution

solution = Solution()

def test_true_case_1():
    s ='()'
    assert solution.isValid(s)

def test_true_case_2():
    s = '()[]{}'
    assert solution.isValid(s)

def test_true_case_3():
    s = '([])'
    assert solution.isValid(s)

def test_false_case_1():
    s = '(]'
    assert not solution.isValid(s)