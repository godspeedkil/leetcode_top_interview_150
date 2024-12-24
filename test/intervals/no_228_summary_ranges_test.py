from src.interview_questions.intervals.no_228_summary_ranges import Solution

solution = Solution()

def test_normal_case_1():
    nums = [0,1,2,4,5,7]
    assert solution.summaryRanges(nums) == ['0->2', '4->5', '7']

def test_normal_case_2():
    nums = [0,2,3,4,6,8,9]
    assert solution.summaryRanges(nums) == ['0', '2->4', '6', '8->9']