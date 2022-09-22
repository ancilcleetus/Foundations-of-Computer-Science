# Given a number N, check whether it is Prime or not

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
