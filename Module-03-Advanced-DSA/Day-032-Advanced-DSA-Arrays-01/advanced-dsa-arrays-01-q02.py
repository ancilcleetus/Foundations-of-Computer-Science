#!/usr/bin/env python3

# Given an integer array A, find max value of 
# f(i, j) = A[i] - A[j] for all i, j indices in A

from time import perf_counter_ns


def get_max_fn_01(A):
    """
    TC = O(N)
    SC = O(1)
    """
    N = len(A)
    max_value = A[0]
    min_value = A[0]
    for i in range(1, N):
        if A[i] > max_value:
            max_value = A[i]
        elif A[i] < min_value:
            min_value = A[i]

    return max_value - min_value


A = [1, 3, 5, 2]

tic = perf_counter_ns()
print(f"Max value of f(i, j) for {A} = {get_max_fn_01(A)}")
toc = perf_counter_ns()
print(f"Took {(toc-tic)/1000} us = {(toc-tic)/1000000} ms")
