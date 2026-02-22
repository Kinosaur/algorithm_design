import sys

# Increase recursion depth just in case, though E=100 usually fits
sys.setrecursionlimit(2000)

def get_common(exercises, i, j):
    """
    Helper to find shared weights. 
    (Same as before)
    """
    if i > j:
        return 0
    intersection = list(exercises[i])
    for k in range(i + 1, j + 1):
        for w in range(len(intersection)):
            intersection[w] = min(intersection[w], exercises[k][w])
    return sum(intersection)

def solve_memoized(i, j, exercises, memo):
    # 1. CHECK NOTEBOOK
    if (i, j) in memo:
        return memo[(i, j)]

    # 2. BASE CASE (Same as before)
    if i == j:
        result = sum(exercises[i]) * 2
        memo[(i, j)] = result  # Save it
        return result

    # 3. RECURSIVE STEP (Same logic)
    shared_count = get_common(exercises, i, j)
    savings = 2 * shared_count
    
    min_ops = float('inf')
    
    for k in range(i, j):
        # Pass the 'memo' notebook to children
        left_cost = solve_memoized(i, k, exercises, memo)
        right_cost = solve_memoized(k + 1, j, exercises, memo)
        
        total = left_cost + right_cost - savings
        
        if total < min_ops:
            min_ops = total
            
    # 4. SAVE TO NOTEBOOK
    memo[(i, j)] = min_ops
    return min_ops

# --- Verification ---
if __name__ == "__main__":
    # Sample Case 1
    exercises = [[1], [2], [1]]
    
    # Create an empty notebook
    memo = {} 
    
    result = solve_memoized(0, 2, exercises, memo)
    print(f"Result: {result}")
    
    # Just to show you what's inside the 'Notebook':
    print("\nWhat did we learn (Memo contents)?")
    for key, val in sorted(memo.items()):
        print(f"Range {key}: Cost {val}")