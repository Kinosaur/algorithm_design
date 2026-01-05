# Kaung Khant Lin
# 6540131
# 542

# Version 3: Bottom-Up Dynamic Programming
import time

A = input().strip()
B = input().strip()

"""
========== THEORY & CONVERSION EXPLANATION ==========

1. WHAT WE'RE CONVERTING:
    - From: Top-Down Recursive (starts at (0,0), goes to (len(A), len(B)))
    - To: Bottom-Up DP (builds from base cases upward to target)

2. KEY INSIGHT - UNDERSTANDING THE RECURSION DIRECTION:
    The recursive function editDistance(i, j) computes the minimum edit distance
    for the SUFFIXES A[i:] and B[j:] (from index i to end of A, j to end of B).
    
    Original recursive direction:
    - Starts: (0, 0)
    - Ends: (len(A), len(B)) ← Base cases are HERE
    - Base cases occur when i == len(A) or j == len(B)
    - Each call increments i and/or j (moves forward)

3. REVERSING FOR BOTTOM-UP:
    To go bottom-up, we REVERSE the loop direction:
    - Start filling: (len(A), len(B)) ← Fill base cases FIRST
    - End with: (0, 0) ← Final answer
    - Loop i: from len(A) DOWN TO 0
    - Loop j: from len(B) DOWN TO 0
    - Use previous results: dp[i+1][j], dp[i][j+1], dp[i+1][j+1]

4. DP TABLE DEFINITION:
    dp[i][j] = minimum edit distance to transform A[i:] into B[j:]

    Why this indexing?
    - dp[len(A)][j] = len(B) - j (insert remaining j characters)
    - dp[i][len(B)] = len(A) - i (delete remaining i characters)
    - dp[i][j] depends on: dp[i+1][j], dp[i][j+1], dp[i+1][j+1]

5. CONVERSION MAPPING:
    Recursive:              →  Bottom-Up DP:
    editDistance(i+1,j+1)   →  dp[i+1][j+1]  (substitute)
    editDistance(i+1,j)     →  dp[i+1][j]    (delete from A)
    editDistance(i,j+1)     →  dp[i][j+1]    (insert into A)

6. LOOP ORDER IS CRITICAL:
    Because dp[i][j] depends on dp[i+1][...] and dp[i][j+1],
    we MUST process:
    - i: from len(A) DOWN TO 0 (backward)
    - j: from len(B) DOWN TO 0 (backward)
    This ensures when we compute dp[i][j], all needed values are already computed.

========== IMPLEMENTATION ==========
"""

# Step 1: Create DP table (size: (len(A)+1) x (len(B)+1))
# dp[i][j] = edit distance for A[i:] and B[j:]
m, n = len(A), len(B)
dp = [[0] * (n + 1) for _ in range(m + 1)]

# Step 2: Fill BASE CASES (edges of the table)
# When we've exhausted one string, cost is the length of the remaining string

# Right edge: dp[i][n] = len(A) - i (delete all remaining chars of A)
for i in range(m + 1):
    dp[i][n] = m - i

# Bottom edge: dp[m][j] = len(B) - j (insert all remaining chars of B)
for j in range(n + 1):
    dp[m][j] = n - j

# Step 3: Fill table in REVERSE order (backward loops)
# Loop i from second-to-last row UP TO row 0
# Loop j from second-to-last column UP TO column 0
for i in range(m - 1, -1, -1):  # i: m-1, m-2, ..., 1, 0 (BACKWARD)
    for j in range(n - 1, -1, -1):  # j: n-1, n-2, ..., 1, 0 (BACKWARD)
        # Check if characters match
        if A[i] == B[j]:
            # MATCH: No operation needed, take diagonal value
            dp[i][j] = dp[i + 1][j + 1]
        else:
            # MISMATCH: Consider all 3 operations

            # Option 1: INSERT B[j] into A[i:]
            # After inserting, we still need to match A[i:] with B[j+1:]
            insert_cost = 1 + dp[i][j + 1]

            # Option 2: DELETE A[i] from A[i:]
            # After deleting, we need to match A[i+1:] with B[j:]
            delete_cost = 1 + dp[i + 1][j]

            # Option 3: SUBSTITUTE A[i] with B[j]
            # After substituting, we need to match A[i+1:] with B[j+1:]
            sub_cost = 1 + dp[i + 1][j + 1]

            # Take minimum
            dp[i][j] = min(insert_cost, delete_cost, sub_cost)

# Step 4: Answer is at dp[0][0] (edit distance for entire strings A and B)
start = time.time()
result = dp[0][0]
end = time.time()

print(f"Minimum Edit Distance: {result}")
print(f"Time: {end - start:.6f} seconds")
