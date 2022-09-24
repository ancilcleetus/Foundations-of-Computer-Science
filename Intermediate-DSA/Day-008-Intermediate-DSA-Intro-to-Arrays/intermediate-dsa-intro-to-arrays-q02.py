# Given an integer array of size N and an integer K,
# check if there exists a pair of indices (i, j)
# such that 1) A[i] + A[j] = K and 2) i != j

"""
Problem Description
Given an array A and an integer B. A pair(i, j) in the array is a good pair if i != j and (A[i] + A[j] == B). Check if any good pair exist or not.



Problem Constraints
1 <= A.size() <= 104

1 <= A[i] <= 109

1 <= B <= 109



Input Format
First argument is an integer array A.

Second argument is an integer B.



Output Format
Return 1 if good pair exist otherwise return 0.



Example Input
Input 1:

A = [1,2,3,4]
B = 7
Input 2:

A = [1,2,4]
B = 4
Input 3:

A = [1,2,2]
B = 4


Example Output
Output 1:

1
Output 2:

0
Output 3:

1


Example Explanation
Explanation 1:

 (i,j) = (3,4)
Explanation 2:

No pair has sum equal to 4.
Explanation 3:

 (i,j) = (2,3)
"""

from time import perf_counter_ns

def checkSumPair01(array, K):
    """
    TC = O(N^2)
    SC = O(1)
    """
    array_size = len(array)

    for i in range(array_size):
        for j in range(array_size):
            if array[i] + array[j] == K and i != j:
                return True

    return False


array1, K1 = [3, -2, 1, 4, 3, 6, 8], 10
array2, K2 = [2, 4, -3, 7], 8
array3, K3 = [2, 3, 8, 5, 3], 6

    
tic = perf_counter_ns()
print(f"checkSumPair01({array1}, {K1}) = {checkSumPair01(array1, K1)}")
toc = perf_counter_ns()
print(f"Took {toc-tic} ns")
tic = perf_counter_ns()
print(f"checkSumPair01({array2}, {K2}) = {checkSumPair01(array2, K2)}")
toc = perf_counter_ns()
print(f"Took {toc-tic} ns")
tic = perf_counter_ns()
print(f"checkSumPair01({array3}, {K3}) = {checkSumPair01(array3, K3)}")
toc = perf_counter_ns()
print(f"Took {toc-tic} ns")


def checkSumPair02(array, K):
    """
    TC = O(N^2)
    SC = O(1)
    """
    array_size = len(array)

    for i in range(array_size):
        for j in range(i+1, array_size):
            if array[i] + array[j] == K:
                return True

    return False
    
tic = perf_counter_ns()
print(f"checkSumPair02({array1}, {K1}) = {checkSumPair02(array1, K1)}")
toc = perf_counter_ns()
print(f"Took {toc-tic} ns")
tic = perf_counter_ns()
print(f"checkSumPair02({array2}, {K2}) = {checkSumPair02(array2, K2)}")
toc = perf_counter_ns()
print(f"Took {toc-tic} ns")
tic = perf_counter_ns()
print(f"checkSumPair02({array3}, {K3}) = {checkSumPair02(array3, K3)}")
toc = perf_counter_ns()
print(f"Took {toc-tic} ns")
