# Kaung Khant Lin
# 6540131
# 542

# Version 2: Recursive Solution with Memoization (Stair Climbing)
import sys
import time

sys.setrecursionlimit(10000)

input_data = sys.stdin.read().split()
N = int(input_data[0])
costs = [int(input_data[i]) for i in range(1, N + 1)]

call_count = 0
memo = {}

def min_energy(i):
    global call_count
    call_count += 1
    
    # CHECK MEMO
    if i in memo:
        return memo[i]
    
    # BASE CASES & RECURSIVE STEPS
    if i == 0:
        result = costs[0]
    elif i == 1:
        # Step 1 must come from Step 0
        result = costs[1] + min_energy(0)
    else:
        # RECURSIVE CASE: Step i
        prev_step_1 = min_energy(i - 1)
        prev_step_2 = min_energy(i - 2)
        result = costs[i] + min(prev_step_1, prev_step_2)
    
    # STORE IN MEMO
    memo[i] = result
    return result

start_time = time.time()
result = min_energy(N - 1)
end_time = time.time()

print(f"Minimum energy cost: {result}")
print(f"Recursive calls: {call_count}")
print(f"Time: {end_time - start_time:.6f} seconds")