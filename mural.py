"""Analysis
We can prove to always get the maximum sum of ceil(N/2) tiles
sum_tiles: the maximum beauty tiles sequence. (uniquely indexable in tiles)
Let start = tiles.index[sum_tiles[0]]
Now, when starting at start + start // 2, we can simply paint every tile by countering the floods movement.

Large input:
Time limit exceeded for 5 x 10^6 input.
Strategies to reduce processing power:
Reduce the most frequent sum calculations by reusing them.
1.:
Build a binary tree like cache, that memoizes calculations indexwise -X-> Memory Limit Exceeded
2.:
Walk sums from left to right. Begin with [left, n]. Continue with - [left] + [left, n] + [n+1].
"""

from math import ceil


def output(case: int, b: int):
    print("Case #%i: %i" % (case, b))


def paint_length(_list):
    return ceil(len(_list)/2)


def subsums(_list, paint_length):
    _sum = sum(_list[:paint_length])
    _sums = [_sum]
    for i, x in enumerate(_list[paint_length:]):
        _sum = _sum - _list[i] + x
        _sums += [_sum]
    return _sums


def find_max_sum(half: int, tiles: list):
    return max(subsums(tiles, half))


if __name__ == "__main__":
    testcases = int(input())
    cases = []  # [[ceil(N/2), [score,...]],...]

    for tc in range(testcases):
        cases += [[ceil(int(input())/2), [int(x) for x in input()]]]

    for i, case in enumerate(cases):
        b = find_max_sum(*case)
        output(i+1, b)
