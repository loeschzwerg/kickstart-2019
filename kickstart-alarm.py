"""Analysis
"""

import numpy as np

M = 1000000007
DTYPE = np.int32 # M fits in


def recur_i(a, x_i_1, b, y_i_1, e, F):
    return (a * x_i_1 + b * y_i_1 + e) % F

# O(N)
def calc_A(x_1, y_1, C, D, E_1, E_2, F, N):
    X, Y = np.empty(N, dtype=DTYPE), np.empty(N, dtype=DTYPE)
    X[0], Y[0] = x_1, y_1
    for i in range(1, N):
        X[i] = recur_i(C, X[i-1], D, Y[i-1], E_1, F)
        Y[i] = recur_i(D, X[i-1], C, Y[i-1], E_2, F)
    return (X + Y) % F

# O(N)
def powered(A, N, K):
    result = 0
    _sum = K
    for x in range(1, N+1):
        if x > 1:
            _sum = (_sum + (pow(x, K+1)-1) * pow(x-1, M-2)) % M
        result = ( result + _sum * A[x-1]) % M
        print("sum: %i, result: %i" % (_sum, result))
    return result


def summation(N, K, x_1, y_1, C, D, E_1, E_2, F):
    """
    N => A[1], ..., A[N] parameter array length
    K: Clock rings K times
    A[i] = (x[i] + y[i]) % F for all i in [1, ..., N]
    """
    A = calc_A(x_1, y_1, C, D, E_1, E_2, F, N)
    print(A)
    return powered(A, N, K)

if __name__ == "__main__":
    T = int(input())
    testcases = []

    for i in range(T):
        testcases += [[int(x) for x in input().split()]]

    for i, x in enumerate(testcases):
        print("Case #%i: %i" % (i+1, summation(*x)))
