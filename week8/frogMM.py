# Kaung Khant Lin
# 6540131
# 542

import sys
import time

sys.setrecursionlimit(10000)

N = int(sys.stdin.readline())
# Height list
h = list(map(int, sys.stdin.readline().split()))

call_count = 0
memo = {}

def min_cost(i):
    global call_count
    call_count += 1
    
    # CHECK MEMO
    if i in memo:
        return memo[i]
    
    # BASE CASES & RECURSIVE STEPS
    if i == 0:
        result = h[0]
    elif i == 1:
        # Step 1 must come from Step 0
        result = abs(h[1] - h[0]) + min_cost(0)
    else:
        # RECURSIVE CASE: Step i
        jump_1 = min_cost(i - 1) + abs(h[i] - h[i - 1])
        jump_2 = min_cost(i - 2) + abs(h[i] - h[i - 2])
        result = min(jump_1, jump_2)
    
    # STORE IN MEMO
    memo[i] = result
    return result

start_time = time.time()
result = min_cost(N - 1)
end_time = time.time()

print(f"Minimum jump cost: {result}")
print(f"Recursive calls: {call_count}")
print(f"Time: {end_time - start_time:.6f} seconds")