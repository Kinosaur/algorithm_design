# Kaung Khant Lin
# 6540131
# 542

# Version 3: Dynamic Programming Solution (Stair Climbing)
import sys
import time

input_data = sys.stdin.read().split()
N = int(input_data[0])
costs = [int(input_data[i]) for i in range(1, N + 1)]

# DP Table to store the minimum energy to reach each step
dp = [0] * N

start_time = time.time()

# BASE CASES
dp[0] = costs[0]

# Cost to reach Step 1
if N > 1:
    dp[1] = costs[1] + dp[0]

# FILL THE TABLE
for i in range(2, N):
    # Option 1: Came from 1 step back
    prev_step_1 = dp[i - 1]
    
    # Option 2: Came from 2 steps back
    prev_step_2 = dp[i - 2]
    
    dp[i] = costs[i] + min(prev_step_1, prev_step_2)

result = dp[N - 1]
end_time = time.time()

print(f"Minimum energy cost: {result}")
print(f"Time: {end_time - start_time:.6f} seconds")