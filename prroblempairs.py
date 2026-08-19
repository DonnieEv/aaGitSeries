from typing import List
prices = [10, 20, 30, 40, 50]
target = 60

def find_product_indices(prices: List[int], target: int) -> List[int]:
    price_to_index = {}
    for index, price in enumerate(prices):
        complement = target - price
        if complement in price_to_index:
            return [price_to_index[complement], index]
        price_to_index[price] = index
    return []

print(find_product_indices(prices, target))
    