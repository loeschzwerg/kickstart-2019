"""Analysis
We can prove to always get the maximum sum of ceil(N/2) tiles
sum_tiles: the maximum beauty tiles sequence. (uniquely indexable in tiles)
Let start = tiles.index[sum_tiles[0]]
Now, when starting at start + start // 2, we can simply paint every tile by countering the floods movement.
"""
from math import ceil


def output(case: int, b: int):
    print("Case #%i: %i" % (case, b))


def find_max_sum(half: int, tiles: str):
    return max([sum(tiles[tile:tile+half]) for tile in range(half+1)])


if __name__ == "__main__":
    testcases = int(input())
    cases = []  # [[ceil(N/2), [score,...]],...]

    for tc in range(testcases):
        cases += [[ceil(int(input())/2), [int(x) for x in input()]]]

    for case in range(len(cases)):
        b = find_max_sum(*cases[case])
        output(case+1, b)
