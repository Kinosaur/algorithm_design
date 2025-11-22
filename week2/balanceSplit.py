# Kaung Khant Lin
# 6540131
# 542

import sys
import time
sys.setrecursionlimit(10000) # set recursion-stack depth

# Global variables
items = []   # The input values
x = []       # The decision list (0 or 1)
n = 0        # Number of items
min_diff = 999999999 # Initialize with a huge number

def solve(i):
    global min_diff
    
    # BASE CASE: All items have been assigned a basket
    if i == n:
        sum_a = 0
        sum_b = 0
        
        # Calculate sums based on the 'x' decision list
        for j in range(n):
            if x[j] == 0:
                sum_a += items[j]
            else:
                sum_b += items[j]
        
        # Calculate difference
        diff = abs(sum_a - sum_b)
        
        # Update global minimum if this is the best split so far
        if diff < min_diff:
            min_diff = diff
        return None

    # RECURSIVE CASE
    
    # Option 0: Put item[i] in Group A
    x[i] = 0
    solve(i + 1)
    
    # Option 1: Put item[i] in Group B
    x[i] = 1
    solve(i + 1)

items = list(map(int, input().split()))
n = len(items)
x = [0] * n  # Initialize state list

start_time = time.time()
solve(0)
end_time = time.time()

print(f"Minimal Difference: {min_diff}")
print(f"Time: {end_time - start_time:.6f} seconds")


# Asked AI to pure explain the logic and application for combination and this balance split problem.
# This is not the optimal solution but a clear recursive approach to understand the problem. I am still trying to figure out optimization.
# The code is write by myself based on the explaination provided by AI.
# The prompt used:
"""
no need to care about optimization just using pure knowledge on combination and combination with counts to aproach this problem steps by steps explaination and no code showing (I will write myself based on my understanding):
PROBLEM B: BALANCE SPLIT ...
"""
