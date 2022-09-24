# Given an integer array of size N and an integer K,
# check if there exists a pair of indices (i, j)
# such that 1) A[i] + A[j] = K and 2) i != j

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