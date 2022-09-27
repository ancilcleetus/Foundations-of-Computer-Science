#!/usr/bin/env python3

# Armstrong Numbers

"""
Problem Description

You are given an integer N you need to print all the Armstrong Numbers between 1 to N.

If sum of cubes of each digit of the number is equal to the number itself, then the number is called an Armstrong number.

For example, 153 = ( 1 * 1 * 1 ) + ( 5 * 5 * 5 ) + ( 3 * 3 * 3 ).


Problem Constraints

1 <= N <= 500



Input Format

First and only line of input contains an integer N.



Output Format

Output all the Armstrong numbers in range [1,N] each in a new line.



Example Input

Input 1:

 5
Input 2:

 200


Example Output

Output 1:

1
Output 2:

1
153


Example Explanation

Explanation 1:

1 is an armstrong number.
Explanation 2:

1 and 153 are armstrong number under 200.
"""

from time import perf_counter_ns

def cube(num):
    return num * num * num

def isArmstrong(num):
    """
    No of Iterations = ceil(log10(num))
    """
    
    orig_num = num
    sum_digit_cubes = 0
    while num != 0:
        digit = num % 10
        sum_digit_cubes += cube(digit)
        num = num // 10

    return sum_digit_cubes == orig_num
    
tic = perf_counter_ns()
print(f"isArmstrong(10) = {isArmstrong(10)}")
toc = perf_counter_ns()
print(f"Took {toc-tic} ns")
tic = perf_counter_ns()
print(f"isArmstrong(999) = {isArmstrong(999)}")
toc = perf_counter_ns()
print(f"Took {toc-tic} ns")
tic = perf_counter_ns()
print(f"isArmstrong(9999) = {isArmstrong(9999)}")
toc = perf_counter_ns()
print(f"Took {toc-tic} ns")
tic = perf_counter_ns()
print(f"isArmstrong(999999) = {isArmstrong(999999)}")
toc = perf_counter_ns()
print(f"Took {toc-tic} ns")
tic = perf_counter_ns()
print(f"isArmstrong(199999999) = {isArmstrong(199999999)}")
toc = perf_counter_ns()
print(f"Took {toc-tic} ns")
