from src.matrix.no_73_set_matrix_zeroes import Solution

solution = Solution()

def test_normal_case():
    matrix = [[1,1,1]
              ,[1,0,1]
              ,[1,1,1]]
    solution.setZeroes(matrix)
    assert matrix == [[1,0,1]
                      ,[0,0,0]
                      ,[1,0,1]]
    
def test_additional_case():
    matrix = [[0,1,2,0]
              ,[3,4,5,2]
              ,[1,3,1,5]]
    solution.setZeroes(matrix)
    assert matrix == [[0,0,0,0]
                      ,[0,4,5,0]
                      ,[0,3,1,0]]