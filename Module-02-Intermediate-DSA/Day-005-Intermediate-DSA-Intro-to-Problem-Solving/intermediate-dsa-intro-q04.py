#!/usr/bin/env python3

# Is it a Perfect Number?

"""
Problem Description

You are given N positive integers.

For each given integer A, you have to tell whether it is a perfect number or not.

A perfect number is a positive integer which is equal to the sum of its proper positive divisors.



Problem Constraints

1 <= N <= 10

1 <= A <= 106



Input Format

The first line of the input contains a single integer N.

Each of the next N lines contains a single integer A.



Output Format

In a separate line, print YES if a given integer is perfect, else print NO.



Example Input

Input 1:

 2
 4
 6 
Input 2:

 1
 3 


Example Output

Output 1:

 NO
 YES 
Output 2:

 NO 


Example Explanation

Explanation 1:

 For A = 4, the answer is "NO" as sum of its proper divisors = 1 + 2 = 3, is not equal to 4. 
 For A = 6, the answer is "YES" as sum of its proper divisors = 1 + 2 + 3 = 6, is equal to 6. 
Explanation 2:

 For A = 3, the answer is "NO" as sum of its proper divisors = 1, is not equal to 3. 
"""

from time import perf_counter_ns

def getProperDivisors(N):
    """
    No of iterations = floor(sqrt(N))
    """
    
    properDivisors = [1]
    i = 2
    while i * i <= N:
        if N % i == 0:
            if i * i == N:
                properDivisors.append(i)
            else:
                properDivisors.extend([i, N // i])
        i += 1

    return properDivisors

def isPerfect(N):
    """
    No of iterations = floor(sqrt(N))
    """

    properDivisors = getProperDivisors(N)
    return sum(properDivisors) == N
    
tic = perf_counter_ns()
print(f"isPerfect(10) = {isPerfect(10)}")
toc = perf_counter_ns()
print(f"Took {toc-tic} ns")
tic = perf_counter_ns()
print(f"isPerfect(100) = {isPerfect(100)}")
toc = perf_counter_ns()
print(f"Took {toc-tic} ns")
tic = perf_counter_ns()
print(f"isPerfect(1000) = {isPerfect(1000)}")
toc = perf_counter_ns()
print(f"Took {toc-tic} ns")
tic = perf_counter_ns()
print(f"isPerfect(8100) = {isPerfect(8100)}")
toc = perf_counter_ns()
print(f"Took {toc-tic} ns")
tic = perf_counter_ns()
print(f"isPerfect(100000000) = {isPerfect(100000000)}")
toc = perf_counter_ns()
print(f"Took {toc-tic} ns")
