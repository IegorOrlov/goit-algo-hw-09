from collections import defaultdict


def find_coins_greedy(coins: list[int], amount: int) -> dict[int, int]:
    index = 0
    result = defaultdict(int)
    while amount > 0:
        coin = coins[index]
        if coin <= amount:
            amount = amount - coin
            result[coin] += 1
        else:
            index += 1
    return dict(result)
