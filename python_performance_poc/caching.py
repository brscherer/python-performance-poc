import functools
import time

@functools.lru_cache(maxsize=None)  # Enable memoization using lru_cache
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Call the function multiple times
start_first_time = time.time()
print(fibonacci(5))  # First call, computes the result and caches it
print("--- %s seconds ---" % (time.time() - start_first_time))
start_second_time = time.time()
print(fibonacci(5))  # Second call, retrieves the result from the cache
print("--- %s seconds ---" % (time.time() - start_second_time))
print(fibonacci(10))  # Computes and caches the result for 10

# Custom caching example
cache = {}  # Custom cache using a dictionary

def factorial(n):
    if n in cache:
        return cache[n]
    elif n <= 1:
        result = 1
    else:
        result = n * factorial(n - 1)
    cache[n] = result  # Store the result in the cache
    return result

# Call the function multiple times
print(factorial(5))  # First call, computes the result and caches it
print(factorial(5))  # Second call, retrieves the result from the cache
print(factorial(10))  # Computes and caches the result for 10