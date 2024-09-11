from src.array_string.no_189_rotate_array import Solution

solution = Solution()

def test_normal_case():
    nums = [1,2,3,4,5,6,7]
    k = 3
    solution.rotate(nums, k)
    assert nums == [5,6,7,1,2,3,4]

def test_additional_case():
    nums = [-1,-100,3,99]
    k = 2
    solution.rotate(nums, k)
    assert nums == [3,99,-1,-100]

def test_single_element():
    nums = [1]
    k = 1
    solution.rotate(nums, k)
    assert nums == [1]

def test_rotations_higher_than_nums_size():
    nums = [1,2,3]
    k = 4
    solution.rotate(nums, k)
    assert nums == [3,1,2]

def test_no_rotations():
    nums = [1,2,3]
    k = 0
    solution.rotate(nums, k)
    assert nums == [1,2,3]