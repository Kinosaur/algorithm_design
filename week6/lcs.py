# Kaung Khant Lin
# 6540131
# 542

import time

N, M = map(int, input().split())
s1 = list(map(int, input().split()))
s2 = list(map(int, input().split()))

# Initialize DP table
# dp[i][j] = LCS length for first i elements of s1 and first j elements of s2
dp = [[0] * (M + 1) for _ in range(N + 1)]

# Fill the table (bottom-up)
for i in range(1, N + 1):
    for j in range(1, M + 1):
        
        if s1[i - 1] == s2[j - 1]:
            # Match: take diagonal value + 1
            dp[i][j] = 1 + dp[i - 1][j - 1]
        else:
            # No match: take max of top or left
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

start_time = time.time()
result = dp[N][M]
end_time = time.time()

print("Execution time:", end_time - start_time, "seconds")
print("LCS length:", result)