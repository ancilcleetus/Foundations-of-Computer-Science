#!/usr/bin/env python3

# Check if there is a subsequence in the given array with gcd = 1

from time import perf_counter_ns


def get_gcd_01(a, b):
    """
    TC = O(min(a, b))
    SC = O(1)
    """
    if a == 0 or b == 0:
        return a + b

    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            gcd = i

    return gcd


def get_gcd_02(a, b):
    """
    TC = O(log b))
    SC = ? (Recursion Stack)
    """

    if a == 0:
        return b
    
    return get_gcd_02(b % a, a)


def check_subsequence_01(A):
    """
    if gcd(any subsequence) == 1:
        gcd(all elements) = 1

    Hence,
    if gcd(all elements) == 1:
        ans = True
    else:
        ans = False

    TC = O(N * A[i])
    SC = O(1)
    """
    N = len(A)

    gcd = A[0]
    for i in range(1, N):
        gcd = get_gcd_01(gcd, A[i])

    return gcd == 1


def check_subsequence_02(A):
    """
    if gcd(any subsequence) == 1:
        gcd(all elements) = 1

    Hence,
    if gcd(all elements) == 1:
        ans = True
    else:
        ans = False

    TC = O(N * log A[i])
    SC = O(1)
    """
    N = len(A)

    gcd = A[0]
    for i in range(1, N):
        gcd = get_gcd_02(gcd, A[i])

    return gcd == 1


A = [2, 30, 14, 72, 60]

tic = perf_counter_ns()
print(check_subsequence_01(A))
toc = perf_counter_ns()
print(f"Took {(toc-tic)/1000} us = {(toc-tic)/1000000} ms")

A = [6, 15, 30, 10, 150]

tic = perf_counter_ns()
print(check_subsequence_01(A))
toc = perf_counter_ns()
print(f"Took {(toc-tic)/1000} us = {(toc-tic)/1000000} ms")

A = [2, 30, 14, 72, 60]

tic = perf_counter_ns()
print(check_subsequence_02(A))
toc = perf_counter_ns()
print(f"Took {(toc-tic)/1000} us = {(toc-tic)/1000000} ms")

A = [6, 15, 30, 10, 150]

tic = perf_counter_ns()
print(check_subsequence_02(A))
toc = perf_counter_ns()
print(f"Took {(toc-tic)/1000} us = {(toc-tic)/1000000} ms")
