from src.hash_map.no_219_contains_duplicate_ii import Solution

solution = Solution()

def test_true_case():
    nums = [1,2,3,1]
    k = 3
    assert solution.containsNearbyDuplicate(nums, k)

def test_true_case_2():
    nums = [1,0,1,1]
    k = 1
    assert solution.containsNearbyDuplicate(nums, k)

def test_false_case():
    nums = [1,2,3,1,2,3]
    k = 2
    assert not solution.containsNearbyDuplicate(nums, k)