from src.array_string.no_274_h_index import Solution

solution = Solution()

def test_normal_case():
    citations = [3,0,6,1,5]
    assert solution.hIndex(citations) == 3

def test_additional_case():
    citations = [1,3,1]
    assert solution.hIndex(citations) == 1

def test_single_element():
    citations = [0]
    assert solution.hIndex(citations) == 0