from src.matrix.no_289_game_of_life import Solution

solution = Solution()

def test_normal_case():
    board = [[0,1,0]
             ,[0,0,1]
             ,[1,1,1]
             ,[0,0,0]]
    solution.gameOfLife(board)
    assert board == [[0,0,0]
                     ,[1,0,1]
                     ,[0,1,1]
                     ,[0,1,0]]
    
def test_additional_case():
    board = [[1,1]
             ,[1,0]]
    solution.gameOfLife(board)
    assert board == [[1,1]
                     ,[1,1]]