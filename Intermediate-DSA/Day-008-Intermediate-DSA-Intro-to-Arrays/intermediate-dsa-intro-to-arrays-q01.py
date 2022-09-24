# Given an integer array of size N, count the no of elements
# having at least 1 element greater than itself

from time import perf_counter_ns

def getCount01(array):
    """
    TC = O(N)
    SC = O(1)
    """
    array_size = len(array)

    # Find largest element
    largest = array[0]
    for i in range(1, array_size):
        if array[i] > largest:
            largest = array[i]

    # Find count of largest element
    count_largest = 0
    for i in range(array_size):
        if array[i] == largest:
            count_largest += 1

    return array_size - count_largest


array1 = [-3, -2, 6, 8, 4, 8, 5]
array2 = [10, 3, 10, 8, 2, 10, 10, 8]
array3 = [8, 8, 8, 8, 8, 8]

    
tic = perf_counter_ns()
print(f"getCount01({array1}) = {getCount01(array1)}")
toc = perf_counter_ns()
print(f"Took {toc-tic} ns")
tic = perf_counter_ns()
print(f"getCount01({array2} = {getCount01(array2)}")
toc = perf_counter_ns()
print(f"Took {toc-tic} ns")
tic = perf_counter_ns()
print(f"getCount01({array3} = {getCount01(array3)}")
toc = perf_counter_ns()
print(f"Took {toc-tic} ns")

def getCount02(array):
    """
    TC = O(N)
    SC = O(1)
    """
    array_size = len(array)

    # Single for loop for getting largest & count_largest
    largest = array[0]
    count_largest = 1
    for i in range(1, array_size):
        if array[i] > largest:
            largest = array[i]
            count_largest = 1
        elif array[i] == largest:
            count_largest += 1

    return array_size - count_largest
    
tic = perf_counter_ns()
print(f"getCount02({array1}) = {getCount02(array1)}")
toc = perf_counter_ns()
print(f"Took {toc-tic} ns")
tic = perf_counter_ns()
print(f"getCount02({array2} = {getCount02(array2)}")
toc = perf_counter_ns()
print(f"Took {toc-tic} ns")
tic = perf_counter_ns()
print(f"getCount02({array3} = {getCount02(array3)}")
toc = perf_counter_ns()
print(f"Took {toc-tic} ns")