# Change-Making Algorithms

This task implements two approaches for making change with coin denominations
`[50, 25, 10, 5, 2, 1]`.

## Greedy vs Dynamic Programming

The greedy algorithm (`find_coins_greedy`) always picks the largest coin that
does not exceed the remaining amount. With a fixed number of denominations, it
runs in **O(k)** time, where `k` is the number of coin types (a constant here),
and uses **O(1)** extra space. It is very fast for large amounts. The downside
is that greedy choice is not guaranteed to be optimal for every coin system,
although for this set it does produce the minimum number of coins.

The dynamic programming algorithm (`find_min_coins`) computes the minimum coin
count for every value from `1` to `amount`. Its time complexity is
**O(amount * k)** and space complexity is **O(amount)**. It guarantees the
optimal result for any coin system, but becomes slower and more memory-intensive
for large amounts.

## Efficiency Comparison

- For large amounts, the greedy algorithm is practically instantaneous because
  the number of steps depends only on the number of denominations.
- DP scales linearly with the amount, so for big values of `amount` it is
  noticeably slower and uses more memory.
- In this coin system, the greedy approach is optimal, so it wins in performance
  without sacrificing solution quality.

## Conclusions

- The greedy algorithm is the most efficient for large amounts in this coin
  system.
- Dynamic programming is useful as a universal method, but it has higher time
  and memory costs for large sums.
