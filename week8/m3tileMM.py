# Kaung Khant Lin
# 6540131
# 542

import sys
import time
sys.setrecursionlimit(10001)

FLAT = 0
UPPER2 = 1
LOWER2 = 2

memo = {}

L = int(input())

def nWays(d, s):
    # Check memo
    if (d, s) in memo:
        return memo[(d, s)]
    
    # Base cases
    if d == L and s == FLAT:
        counter = 1
    elif d > L:
        counter = 0
    else:
        # Recursive cases
        counter = 0
        if s == FLAT:
            counter += nWays(d + 2, FLAT)
            counter += nWays(d + 1, UPPER2)
            counter += nWays(d + 1, LOWER2)
        else:  # s is either UPPER2 or LOWER2
            counter += nWays(d + 1, FLAT)
            counter += nWays(d + 2, s)
    memo[(d, s)] = counter
    return counter

start_time = time.time()
print(nWays(0, FLAT))
end_time = time.time()

print(f"Execution time: {end_time - start_time} seconds")
