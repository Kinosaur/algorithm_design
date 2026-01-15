# Kaung Khant Lin
# 6540131
# 542

import time

FLAT = 0
UPPER2 = 1
LOWER2 = 2

L = int(input())

dp = [[0] * 3 for _ in range(L + 2)]

# Base cases
dp[L][FLAT] = 1
dp[L][UPPER2] = 0
dp[L][LOWER2] = 0

for d in range(L - 1, -1, -1):
    for s in [FLAT, UPPER2, LOWER2]:
        if s == FLAT:
            dp[d][FLAT] = dp[d + 2][FLAT] + dp[d + 1][UPPER2] + dp[d + 1][LOWER2]
        else:  # s is either UPPER2 or LOWER2
            dp[d][s] = dp[d + 1][FLAT] + dp[d + 2][s]
        
start_time = time.time()
print(dp[0][FLAT])
end_time = time.time()

print(f"Execution time: {end_time - start_time} seconds")