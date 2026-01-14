# Kaung Khant Lin
# 6540131
# 542
# Dynamic Programming Solution

import sys
import time
sys.setrecursionlimit(10000)

line1 = sys.stdin.readline()
N = int(line1.strip())

v_list = []
d_list = []

for _ in range(N):
    line = sys.stdin.readline()
    v_in, d_in = map(int, line.split())
    v_list.append(v_in)
    d_list.append(d_in)

start_time = time.time()

# dp[i] = set of (product, sum) tuples achievable using items 0..i-1
# (1, 0) represents the empty subset (product starts at 1, sum starts at 0)
dp = [set() for _ in range(N + 1)]
dp[0].add((1, 0))

for i in range(N):
    # Option 1: Don't take item i (carry forward previous states)
    dp[i + 1].update(dp[i])
    
    # Option 2: Take item i (create new states by including item i)
    for product, total_sum in dp[i]:
        new_product = product * v_list[i]
        new_sum = total_sum + d_list[i]
        dp[i + 1].add((new_product, new_sum))

# Find minimum difference
# Exclude the empty subset (1, 0) since we need at least one item
min_diff = float('inf')
for product, total_sum in dp[N]:
    if not (product == 1 and total_sum == 0):  # Skip empty subset
        diff = abs(product - total_sum)
        if diff < min_diff:
            min_diff = diff

end_time = time.time()

print(min_diff)
print(f"Time: {end_time - start_time:.6f} seconds")
