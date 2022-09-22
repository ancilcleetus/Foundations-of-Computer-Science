#!/usr/bin/env python3

# Square Root of a number

"""
Problem Description

Given a number A. Return square root of the number if it is perfect square otherwise return -1.



Problem Constraints

1 <= A <= 10^8



Input Format

First argument is an integer A.



Output Format

Return an integer which is the square root of A if A is perfect square otherwise return -1.



Example Input

Input 1:

A = 4
Input 2:

A = 1001


Example Output

Output 1:

2
Output 2:

-1


Example Explanation

Explanation 1:

sqrt(4) = 2
Explanation 2:

1001 is not a perfect square.
"""

from time import perf_counter_ns

def getSquareRoot(N):
    """
    No of iterations = floor(sqrt(N))
    """

    i = 1
    while i * i <= N:
        if i * i == N:
            return i
        i += 1
    else:
        return -1
    
tic = perf_counter_ns()
print(f"getSquareRoot(10) = {getSquareRoot(10)}")
toc = perf_counter_ns()
print(f"Took {toc-tic} ns")
tic = perf_counter_ns()
print(f"getSquareRoot(100) = {getSquareRoot(100)}")
toc = perf_counter_ns()
print(f"Took {toc-tic} ns")
tic = perf_counter_ns()
print(f"getSquareRoot(1000) = {getSquareRoot(1000)}")
toc = perf_counter_ns()
print(f"Took {toc-tic} ns")
tic = perf_counter_ns()
print(f"getSquareRoot(8100) = {getSquareRoot(8100)}")
toc = perf_counter_ns()
print(f"Took {toc-tic} ns")
tic = perf_counter_ns()
print(f"getSquareRoot(100000000) = {getSquareRoot(100000000)}")
toc = perf_counter_ns()
print(f"Took {toc-tic} ns")
