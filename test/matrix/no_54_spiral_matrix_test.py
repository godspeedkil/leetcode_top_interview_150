from src.matrix.no_54_spiral_matrix import Solution

solution = Solution()

def test_normal_case():
    matrix = [[1,2,3]
              ,[4,5,6]
              ,[7,8,9]]
    assert solution.spiralOrder(matrix) == [1,2,3,6,9,8,7,4,5]

def test_additional_case():
    matrix = [[1,2,3,4]
              ,[5,6,7,8]
              ,[9,10,11,12]]
    assert solution.spiralOrder(matrix) == [1,2,3,4,8,12,11,10,9,5,6,7]

def test_single_element():
    matrix = [[1]]
    assert solution.spiralOrder(matrix) == [1]