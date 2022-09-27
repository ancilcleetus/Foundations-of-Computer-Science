#!/usr/bin/env python3

# Given an integer array A, find max value of 
# f(i, j) = |A[i] - A[j]| + |i - j| for all i, j indices in A

from time import perf_counter_ns

def get_max_fn_01(A):
    """
    TC = O(N)
    SC = O(1)
    """
    N = len(A)
    max_1 = A[0] + 0
    min_1 = A[0] + 0
    max_2 = A[0] - 0
    min_2 = A[0] - 0
    for i in range(1, N):
        if A[i] + i > max_1:
            max_1 = A[i] + i
        elif A[i] + i < min_1:
            min_1 = A[i] + i
        if A[i] - i > max_2:
            max_2 = A[i] - i
        elif A[i] - i < min_2:
            min_2 = A[i] - i

    return max(max_1 - min_1, max_2 - min_2)


A = [1, 3, 5, 2]

tic = perf_counter_ns()
print(f"Max value of f(i, j) for {A} = {get_max_fn_01(A)}")
toc = perf_counter_ns()
print(f"Took {(toc-tic)/1000} us = {(toc-tic)/1000000} ms")

A = [1, 3, 8, 10, 0, 6, 9]

tic = perf_counter_ns()
print(f"Max value of f(i, j) for {A} = {get_max_fn_01(A)}")
toc = perf_counter_ns()
print(f"Took {(toc-tic)/1000} us = {(toc-tic)/1000000} ms")
