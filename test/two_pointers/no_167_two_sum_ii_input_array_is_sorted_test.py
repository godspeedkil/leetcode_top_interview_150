from src.two_pointers.no_167_two_sum_ii_input_array_is_sorted import Solution

solution = Solution()

def test_normal_case():
    numbers = [2,7,11,15]
    target = 9
    assert solution.twoSum(numbers, target) == [1,2]

def test_additional_case():
    numbers = [2,3,4]
    target = 6
    assert solution.twoSum(numbers, target) == [1,3]