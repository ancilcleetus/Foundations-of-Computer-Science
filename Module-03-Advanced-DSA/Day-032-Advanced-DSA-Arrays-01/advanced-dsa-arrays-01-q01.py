#!/usr/bin/env python3

# Given an integer array such that all elements are zero.
# Return the final array after performing multiple queries.
# Query (i, x) => Add x to all elements from A[i] to A[N-1]

from time import perf_counter_ns


def get_final_array_01(A, queries):
    """
    TC = O(Q * N)
    SC = O(1)
    """
    N = len(A)
    for (i, x) in queries:
        for i in range(i, N):
            A[i] += x

    return A


A = [0, 0, 0, 0, 0, 0, 0]
queries = [(1, 3), (4, 2), (3, 1)]

tic = perf_counter_ns()
print(get_final_array_01(A, queries))
toc = perf_counter_ns()
print(f"Took {(toc-tic)/1000} us = {(toc-tic)/1000000} ms")


def get_final_array_02(A, queries):
    """
    TC = O(Q + N)
    SC = O(1)
    """
    N = len(A)

    for (i, x) in queries:
        A[i] += x

    # prefix sum array
    for i in range(1, N):
        A[i] += A[i - 1]

    return A


A = [0, 0, 0, 0, 0, 0, 0]
queries = [(1, 3), (4, 2), (3, 1)]

tic = perf_counter_ns()
print(get_final_array_02(A, queries))
toc = perf_counter_ns()
print(f"Took {(toc-tic)/1000} us = {(toc-tic)/1000000} ms")


def get_final_array_03(A, queries):
    """
    TC = O(Q + N)
    SC = O(1)
    """
    N = len(A)

    for (i, j, x) in queries:
        A[i] = A[i] + x
        if j + 1 < N:
            A[j + 1] = A[j + 1] - x

    # prefix sum array
    for i in range(1, N):
        A[i] += A[i - 1]

    return A


A = [0, 0, 0, 0, 0, 0, 0]
queries = [(1, 3, 5), (2, 5, 1), (0, 3, -1)]

tic = perf_counter_ns()
print(get_final_array_03(A, queries))
toc = perf_counter_ns()
print(f"Took {(toc-tic)/1000} us = {(toc-tic)/1000000} ms")
