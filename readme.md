# Change-Making Algorithms

This task implements two approaches for making change with coin denominations
`[50, 25, 10, 5, 2, 1]`.

## Greedy vs Dynamic Programming

The greedy algorithm (`find_coins_greedy`) always picks the largest coin that
does not exceed the remaining amount. With a fixed set of coin types, this runs
in **O(k)** time, where `k` is the number of coin denominations (constant here),
and uses **O(1)** extra space. It is very fast even for large amounts, but it is
not guaranteed to be optimal for all coin systems. In this particular set of
coins, the greedy choice is optimal, so it matches the minimal number of coins.

The dynamic programming algorithm (`find_min_coins`) computes the minimal coin
count for every value from `1` to `amount`. It runs in **O(amount * k)** time and
uses **O(amount)** space. This guarantees the minimal number of coins for any
coin system, but the runtime grows linearly with the amount. For very large
amounts, it can become significantly slower than greedy.

## Conclusion

- Greedy is the fastest and simplest choice when the coin system is canonical,
  and it scales well for large amounts.
- Dynamic programming is more robust because it always finds the optimal
  solution, but it costs more time and memory as the amount increases.
