from src.array_string.no_380_insert_delete_getrandom_O1 import RandomizedSet

def test_normal_case():
    randomized_set = RandomizedSet()
    assert randomized_set.insert(1) == True
    assert randomized_set.remove(2) == False
    assert randomized_set.insert(2) == True
    assert randomized_set.getRandom() in [1,2]
    assert randomized_set.remove(1) == True
    assert randomized_set.insert(2) == False
    assert randomized_set.getRandom() == 2