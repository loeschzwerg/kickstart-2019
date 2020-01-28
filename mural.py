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
Build a binary tree like cache, that memoizes calculations indexwise
"""

from math import ceil


def output(case: int, b: int):
    print("Case #%i: %i" % (case, b))


def memoize(f):
    memo = {}

    def helper(x, y):
        if (x, y) not in memo:
            if x % 2 == 0:
                if y % 2 == 0: create cached
                    memo[(x, y)] = f(x, y)
                    return memo[(x,y)]
                elif (x+1, y) not in memo
            elif y % 2 == 0:
                
            else:    # (x,y-1) is in cache
                return memo[(x,y-1)] + f(y-1, y)
        return memo[(x, y)]
    return helper


def find_max_sum(half: int, tiles: list):
    @memoize
    def subsum(left, right):
        if right - left > 1:
            n_half = left + (right-left) // 2
            return subsum(left, n_half) + subsum(n_half, right)
        else:
            return tiles[left]
    return max([subsum(tile, tile+half) for tile in range(half+(1 if len(tiles) % 2 == 0 else 0))])


if __name__ == "__main__":
    testcases = int(input())
    cases = []  # [[ceil(N/2), [score,...]],...]

    for tc in range(testcases):
        cases += [[ceil(int(input())/2), [int(x) for x in input()]]]

    for case in range(len(cases)):
        b = find_max_sum(*cases[case])
        output(case+1, b)
