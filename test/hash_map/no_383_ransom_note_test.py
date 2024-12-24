from src.interview_questions.hash_map.no_383_ransom_note import Solution

solution = Solution()

def test_false_case():
    ransom_note = 'a'
    magazine = 'b'
    assert not solution.canConstruct(ransom_note, magazine)

def test_false_case_2():
    ransom_note = 'aa'
    magazine = 'b'
    assert not solution.canConstruct(ransom_note, magazine)

def test_true_case():
    ransom_note = 'aa'
    magazine = 'aab'
    assert solution.canConstruct(ransom_note, magazine)