# Kaung Khant Lin
# 6540131
# 542

import time

N, M = map(int, input().split())
weights = list(map(int, input().split()))
values = list(map(int, input().split()))

# memoization -> tabulation (bottom-up DP)
dp = [[0] * (M + 1) for _ in range(N + 1)]

# DP use loop instead of recursion
for i in range(1, N + 1):
    
    current_weight = weights[i-1]
    current_value = values[i-1]
    
    for w in range(M + 1):
        
        # Option 1: Skip (Copy from the row above)
        skip = dp[i-1][w]
        
        # Option 2: Take (Add value + look up remaining space in row above)
        take = -1
        if current_weight <= w:
            take = current_value + dp[i-1][w - current_weight]
        
        # Pick the maximum of both options
        dp[i][w] = max(skip, take)

start_time = time.time()
result = dp[N][M]
end_time = time.time()

print(f"Maximum profit: {result}")
print(f"Time: {end_time - start_time:.6f} seconds")