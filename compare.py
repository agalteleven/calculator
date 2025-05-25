from libload import lib
import time

# Timing the C++ library call
start = time.perf_counter()
fibonaci_75_lib = lib.fibonaci(75)
end = time.perf_counter()
elapsed_seconds = end - start
print(f"fibonaci(75) from lib took {elapsed_seconds:.6f} seconds")
print(f"Fibonaci 75th from lib: {fibonaci_75_lib}")

# Python implementation
def fibonaci(n):
    previous = [1, 1]
    for i in range(2, n):
        previous = [previous[1], previous[0] + previous[1]]
    return previous[1]

start = time.perf_counter()
fibonaci_75_py = fibonaci(75)
end = time.perf_counter()
elapsed_seconds = end - start
print(f"fibonaci(75) from python took {elapsed_seconds:.6f} seconds")
print(f"Fibonaci 75th from python: {fibonaci_75_py}")
