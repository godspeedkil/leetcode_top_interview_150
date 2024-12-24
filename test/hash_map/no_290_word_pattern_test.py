from src.interview_questions.hash_map.no_290_word_pattern import Solution

solution = Solution()

def test_true_case():
    pattern = 'abba'
    s = 'dog cat cat dog'
    assert solution.wordPattern(pattern, s)

def test_false_case():
    pattern = 'abba'
    s = 'dog cat cat fish'
    assert not solution.wordPattern(pattern, s)

def test_false_case_2():
    pattern = 'aaaa'
    s = 'dog cat cat dog'
    assert not solution.wordPattern(pattern, s)