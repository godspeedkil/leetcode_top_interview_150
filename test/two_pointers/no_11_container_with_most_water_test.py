from src.two_pointers.no_11_container_with_most_water import Solution

solution = Solution()

def test_normal_case():
    height = [1,8,6,2,5,4,8,3,7]
    assert solution.maxArea(height) == 49

def test_additional_case():
    height = [1,1]
    assert solution.maxArea(height) == 1

def test_no_valid_container():
    height = [0,1]
    assert solution.maxArea(height) == 0