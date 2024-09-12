from src.array_string.no_134_gas_station import Solution

solution = Solution()

def test_can_complete_circuit():
    gas = [1,2,3,4,5]
    cost = [3,4,5,1,2]
    assert solution.canCompleteCircuit(gas, cost) == 3

def test_cant_complete_circuit():
    gas = [2,3,4]
    cost = [3,4,3]
    assert solution.canCompleteCircuit(gas, cost) == -1