from src.hash_map.no_205_isomorphic_strings import Solution

solution = Solution()

def test_true_case():
    s = 'egg'
    t = 'add'
    assert solution.isIsomorphic(s, t)

def test_false_case():
    s = 'foo'
    t = 'bar'
    assert not solution.isIsomorphic(s, t)

def test_true_case_2():
    s = 'paper'
    t = 'title'
    assert solution.isIsomorphic(s, t)