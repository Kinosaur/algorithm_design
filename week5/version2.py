# Kaung Khant Lin
# 6540131
# 542

# Version 2: Recursive Brute Force with Memoization
import sys
import time
sys.setrecursionlimit(2000)

A = input().strip()
B = input().strip()

memo = {} 

def editDistance(i, j):
    # CHECK MEMO
    if (i, j) in memo:
        return memo[(i, j)]
    
    # BASE CASES
    if i == len(A):
        return len(B) - j
    if j == len(B):
        return len(A) - i

    # RECURSIVE CASES
    res = 0
    if A[i] == B[j]:
        res = editDistance(i + 1, j + 1)
    else:
        insert_cost = 1 + editDistance(i, j + 1)
        delete_cost = 1 + editDistance(i + 1, j)
        sub_cost    = 1 + editDistance(i + 1, j + 1)
        res = min(insert_cost, delete_cost, sub_cost)
    
    # Keep in MEMO
    memo[(i, j)] = res
    return res
    
start = time.time()
result = editDistance(0, 0)
end = time.time()

print(f'Minimum Edit Distance: {result}')
print(f"Time: {end - start:.6f} seconds")
