from src.array_string.no_122_best_time_to_buy_and_sell_stock_ii import Solution

solution = Solution()

def test_normal_case():
    prices = [7,1,5,3,6,4]
    assert solution.maxProfit(prices) == 7

def test_additional_case():
    prices = [1,2,3,4,5]
    assert solution.maxProfit(prices) == 4

def test_no_profit():
    prices = [7,6,4,3,1]
    assert solution.maxProfit(prices) == 0

def test_only_one_price():
    prices = [1]
    assert solution.maxProfit(prices) == 0