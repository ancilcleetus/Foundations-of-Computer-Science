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

def getSquareRoot_01(N):
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
print(f"getSquareRoot_01(10) = {getSquareRoot_01(10)}")
toc = perf_counter_ns()
print(f"Took {toc-tic} ns")
tic = perf_counter_ns()
print(f"getSquareRoot_01(100) = {getSquareRoot_01(100)}")
toc = perf_counter_ns()
print(f"Took {toc-tic} ns")
tic = perf_counter_ns()
print(f"getSquareRoot_01(1000) = {getSquareRoot_01(1000)}")
toc = perf_counter_ns()
print(f"Took {toc-tic} ns")
tic = perf_counter_ns()
print(f"getSquareRoot_01(8100) = {getSquareRoot_01(8100)}")
toc = perf_counter_ns()
print(f"Took {toc-tic} ns")
tic = perf_counter_ns()
print(f"getSquareRoot_01(100000000) = {getSquareRoot_01(100000000)}")
toc = perf_counter_ns()
print(f"Took {toc-tic} ns")

def getSquareRoot_02(N):
    """
    No of iterations = floor(log(N))
    """
    
    low = 1
    high = N
    while True:
        if low == high:
            return 1
        elif high-low == 1:
            return -1
        else:
            mid = (low + high) // 2
            if mid * mid > N:
                high = mid
            elif mid * mid == N:
                return mid
            else:
                low = mid
        
tic = perf_counter_ns()
print(f"getSquareRoot_02(10) = {getSquareRoot_02(10)}")
toc = perf_counter_ns()
print(f"Took {toc-tic} ns")
tic = perf_counter_ns()
print(f"getSquareRoot_02(100) = {getSquareRoot_02(100)}")
toc = perf_counter_ns()
print(f"Took {toc-tic} ns")
tic = perf_counter_ns()
print(f"getSquareRoot_02(1000) = {getSquareRoot_02(1000)}")
toc = perf_counter_ns()
print(f"Took {toc-tic} ns")
tic = perf_counter_ns()
print(f"getSquareRoot_02(8100) = {getSquareRoot_02(8100)}")
toc = perf_counter_ns()
print(f"Took {toc-tic} ns")
tic = perf_counter_ns()
print(f"getSquareRoot_02(100000000) = {getSquareRoot_02(100000000)}")
toc = perf_counter_ns()
print(f"Took {toc-tic} ns")