from src.interview_questions.hash_map.no_242_valid_anagram import Solution

solution = Solution()

def test_true_case():
    s = 'anagram'
    t = 'nagaram'
    assert solution.isAnagram(s, t)

def test_false_case():
    s = 'rat'
    t = 'car'
    assert not solution.isAnagram(s, t)