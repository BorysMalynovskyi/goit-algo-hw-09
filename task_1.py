from typing import Dict, List


COINS: List[int] = [50, 25, 10, 5, 2, 1]


def find_coins_greedy(amount: int) -> Dict[int, int]:
    """Return change for amount using a greedy strategy."""
    if amount < 0:
        raise ValueError("Amount must be non-negative.")

    remaining = amount
    result: Dict[int, int] = {}

    for coin in COINS:
        if remaining == 0:
            break
        count, remaining = divmod(remaining, coin)
        if count:
            result[coin] = count

    return result


def find_min_coins(amount: int) -> Dict[int, int]:
    """Return change with the minimum number of coins using dynamic programming."""
    if amount < 0:
        raise ValueError("Amount must be non-negative.")
    if amount == 0:
        return {}

    max_value = amount + 1
    min_coins = [0] + [max_value] * amount
    last_coin = [0] * (amount + 1)

    for coin in COINS:
        for value in range(coin, amount + 1):
            candidate = min_coins[value - coin] + 1
            if candidate < min_coins[value]:
                min_coins[value] = candidate
                last_coin[value] = coin

    if min_coins[amount] == max_value:
        return {}

    result: Dict[int, int] = {}
    value = amount
    while value > 0:
        coin = last_coin[value]
        if coin == 0:
            break
        result[coin] = result.get(coin, 0) + 1
        value -= coin

    return {coin: result[coin] for coin in sorted(result)}


if __name__ == "__main__":
    sample_amount = 113
    print(f"Greedy: {find_coins_greedy(sample_amount)}")
    print(f"DP: {find_min_coins(sample_amount)}")
