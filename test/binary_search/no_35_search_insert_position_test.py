from src.interview_questions.binary_search.no_35_search_insert_position import Solution

solution = Solution()

def test_case_1():
    nums = [1,3,5,6]
    target = 5
    assert solution.searchInsert(nums, target) == 2

def test_case_2():
    nums = [1,3,5,6]
    target = 2
    assert solution.searchInsert(nums, target) == 1

def test_case_3():
    nums = [1,3,5,6]
    target = 7
    assert solution.searchInsert(nums, target) == 4