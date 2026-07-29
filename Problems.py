from typing import List
prices = [7, 1, 5, 3, 6, 4]


def max_profit(prices: List[int]) -> int:
    if not prices:
        return 0

    min_price_so_far = prices[0]
    best_profit = 0

    for price in prices[1:]:
        best_profit = max(best_profit, price - min_price_so_far)
        min_price_so_far = min(min_price_so_far, price)

    return best_profit


print(max_profit(prices))
