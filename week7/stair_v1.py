# Kaung Khant Lin
# 6540131
# 542

# Version 1: Naive Recursive Brute Force (Stair Climbing)
import sys
import time

sys.setrecursionlimit(10000)

input_data = sys.stdin.read().split()
N = int(input_data[0])
costs = [int(input_data[i]) for i in range(1, N + 1)]

call_count = 0

def min_energy(i):
    global call_count
    call_count += 1
    
    # BASE CASE: Step 0
    if i == 0:
        return costs[0]
    
    # BASE CASE: Step 1
    if i == 1:
        return costs[1] + min_energy(0)
    
    # RECURSIVE CASE: Step i
    prev_step_1 = min_energy(i - 1)
    prev_step_2 = min_energy(i - 2)
    
    return costs[i] + min(prev_step_1, prev_step_2)

start_time = time.time()
result = min_energy(N - 1)
end_time = time.time()

print(f"Minimum energy cost: {result}")
print(f"Recursive calls: {call_count}")
print(f"Time: {end_time - start_time:.6f} seconds")