# Kaung Khant Lin
# 6540131
# 542

import sys

def solve_frog():
    N = int(sys.stdin.readline())
    # Height list
    h = list(map(int, sys.stdin.readline().split()))

    dp = [0] * N

    dp[0] = 0
    
    if N > 1:
        dp[1] = abs(h[1] - h[0])

    for i in range(2, N):
        jump_one = dp[i-1] + abs(h[i] - h[i-1])

        jump_two = dp[i-2] + abs(h[i] - h[i-2])

        dp[i] = min(jump_one, jump_two)

    print(dp[N-1])

solve_frog()