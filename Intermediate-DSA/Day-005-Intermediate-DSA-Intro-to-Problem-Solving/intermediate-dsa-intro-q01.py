# Given a number N, count factors of N

from time import perf_counter_ns

def get_factors_count_01(N):
    count = 0
    for i in range(1, N+1):
        if N % i == 0:
            count += 1
    
    return count
    
tic = perf_counter_ns()
print(f"No of factors of 10 = {get_factors_count_01(10)}")
toc = perf_counter_ns()
print(f"Took {toc-tic} ns")
tic = perf_counter_ns()
print(f"No of factors of 100 = {get_factors_count_01(100)}")
toc = perf_counter_ns()
print(f"Took {toc-tic} ns")
tic = perf_counter_ns()
print(f"No of factors of 1000 = {get_factors_count_01(1000)}")
toc = perf_counter_ns()
print(f"Took {toc-tic} ns")

def get_factors_count_02(N):
    count = 0
    i = 1
    while i * i <= N:
        if N % i == 0:
            if i * i == N:
                count += 1
            else:
                count += 2
        i += 1
    
    return count
    
tic = perf_counter_ns()
print(f"No of factors of 10 = {get_factors_count_02(10)}")
toc = perf_counter_ns()
print(f"Took {toc-tic} ns")
tic = perf_counter_ns()
print(f"No of factors of 100 = {get_factors_count_02(100)}")
toc = perf_counter_ns()
print(f"Took {toc-tic} ns")
tic = perf_counter_ns()
print(f"No of factors of 1000 = {get_factors_count_02(1000)}")
toc = perf_counter_ns()
print(f"Took {toc-tic} ns")