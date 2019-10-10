# Time complexity is O(n); Space Complexity is O(1) but stack space for recursion
# Recrusion - Cached
from functools import lru_cache

@lru_cache()   # Since the recursion logic would take time when the range of fibonacci series increases. But the lru_cache would cut down the time;
def fibonacci(i):
    if i <= 1:
        return 0
    elif i == 2:
        return 1
    else:
        return fibonacci(i-1) + fibonacci(i-2)

i = 1
while i <= 500:
    print(fibonacci(500))
    i += 1
