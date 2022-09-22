#!/usr/bin/env python3

"""
Problem Description

Given an integer A, you have to tell whether it is a prime number or not.

A prime number is a natural number greater than 1 which is divisible only by 1 and itself.



Problem Constraints

1 <= A <= 10^6



Input Format

First and only line of the input contains a single integer A.



Output Format

Print YES if A is a prime, else print NO.



Example Input

Input 1:

 3 
Input 2:

 4 


Example Output

Output 1:

 YES 
Output 2:

 NO 


Example Explanation

Explanation 1:

 3 is a prime number as it is only divisible by 1 and 3.
Explanation 2:

 4 is not a prime number as it is divisible by 2.
"""

from time import perf_counter_ns

def isPrime(N):
    """
    No of iterations = N
    """

    factor_count = 0
    for i in range(1, N+1):
        if N % i == 0:
            factor_count += 1
    
    return factor_count == 2
    
tic = perf_counter_ns()
print(f"isPrime(10) = {isPrime(10)}")
toc = perf_counter_ns()
print(f"Took {toc-tic} ns")
tic = perf_counter_ns()
print(f"isPrime(100) = {isPrime(100)}")
toc = perf_counter_ns()
print(f"Took {toc-tic} ns")
tic = perf_counter_ns()
print(f"isPrime(1000) = {isPrime(1000)}")
toc = perf_counter_ns()
print(f"Took {toc-tic} ns")
tic = perf_counter_ns()
print(f"isPrime(7919) = {isPrime(7919)}")
toc = perf_counter_ns()
print(f"Took {toc-tic} ns")
