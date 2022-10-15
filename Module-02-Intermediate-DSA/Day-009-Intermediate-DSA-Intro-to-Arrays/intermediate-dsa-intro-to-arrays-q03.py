#!/usr/bin/env python3

# Given an integer array, reverse it in SC = O(1) i.e. modify input array


from time import perf_counter_ns

def reverseArray01(array):
    """
    TC = O(N)
    SC = O(1)
    No need to return anything since
    we are modifying the input itself
    """
    array_size = len(array)
    left = 0
    right = array_size - 1
    while left < right:
        temp = array[left]
        array[left] = array[right]
        array[right] = temp

        left += 1
        right -= 1


array1 = [3, -2, 1, 4, 3, 6, 8]
array2 = [2, 4, -3, 7]
array3 = [2, 3, 8, 5, 3]

    
tic = perf_counter_ns()
print(f"Before: array1 = {array1}")
reverseArray01(array1)
print(f"After: array1 = {array1}")
toc = perf_counter_ns()
print(f"Took {toc-tic} ns")
tic = perf_counter_ns()
print(f"Before: array2 = {array2}")
reverseArray01(array2)
print(f"After: array2 = {array2}")
toc = perf_counter_ns()
print(f"Took {toc-tic} ns")
tic = perf_counter_ns()
print(f"Before: array3 = {array3}")
reverseArray01(array3)
print(f"After: array3 = {array3}")
toc = perf_counter_ns()
print(f"Took {toc-tic} ns")


def reverseArray02(array):
    """
    TC = O(N)
    SC = O(1)
    No need to return anything since
    we are modifying the input itself
    """
    array_size = len(array)
    left = 0
    right = array_size - 1
    while left < right:
        # To swap a and b without temporary variable
        # a = a + b
        # b = a - b
        # a = a - b
        array[left] = array[left] + array[right]
        array[right] = array[left] - array[right]
        array[left] = array[left] - array[right]

        left += 1
        right -= 1
    
tic = perf_counter_ns()
print(f"Before: array1 = {array1}")
reverseArray02(array1)
print(f"After: array1 = {array1}")
toc = perf_counter_ns()
print(f"Took {toc-tic} ns")
tic = perf_counter_ns()
print(f"Before: array2 = {array2}")
reverseArray02(array2)
print(f"After: array2 = {array2}")
toc = perf_counter_ns()
print(f"Took {toc-tic} ns")
tic = perf_counter_ns()
print(f"Before: array3 = {array3}")
reverseArray02(array3)
print(f"After: array3 = {array3}")
toc = perf_counter_ns()
print(f"Took {toc-tic} ns")


def reverseArray03(array):
    """
    TC = O(N)
    SC = O(1)
    No need to return anything since
    we are modifying the input itself
    """
    array_size = len(array)
    left = 0
    right = array_size - 1
    while left < right:
        # To swap a and b without temporary variable
        array[left], array[right] = array[right], array[left]

        left += 1
        right -= 1
    
tic = perf_counter_ns()
print(f"Before: array1 = {array1}")
reverseArray03(array1)
print(f"After: array1 = {array1}")
toc = perf_counter_ns()
print(f"Took {toc-tic} ns")
tic = perf_counter_ns()
print(f"Before: array2 = {array2}")
reverseArray03(array2)
print(f"After: array2 = {array2}")
toc = perf_counter_ns()
print(f"Took {toc-tic} ns")
tic = perf_counter_ns()
print(f"Before: array3 = {array3}")
reverseArray03(array3)
print(f"After: array3 = {array3}")
toc = perf_counter_ns()
print(f"Took {toc-tic} ns")
