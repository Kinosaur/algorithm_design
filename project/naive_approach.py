def get_common(exercises, i, j):
    """
    Helper to find how many weights are shared by ALL exercises 
    from index i to j.
    """
    # Start with the weights of the first exercise in the range
    intersection = list(exercises[i])
    
    # Compare with every other exercise in the range
    for k in range(i + 1, j + 1):
        for w in range(len(intersection)):
            # Keep the minimum amount (intersection)
            intersection[w] = min(intersection[w], exercises[k][w])
            
    return sum(intersection)

def solve_recursive(i, j, exercises):
    """
    Naive Recursive function to find min operations for range [i, j].
    Try EVERY possible split point.
    """
    # BASE CASE: Single exercise
    if i == j:
        # Cost is Push all + Pop all
        # Sum of weights for this exercise * 2
        return sum(exercises[i]) * 2

    # RECURSIVE STEP: Try all splits
    # First, find savings for this specific range
    shared_count = get_common(exercises, i, j)
    savings = 2 * shared_count
    
    min_ops = float('inf')
    
    # Try splitting at k = i, i+1, ..., j-1
    for k in range(i, j):
        # Recursive calls
        left_cost = solve_recursive(i, k, exercises)
        right_cost = solve_recursive(k + 1, j, exercises)
        
        total = left_cost + right_cost - savings
        
        if total < min_ops:
            min_ops = total
            
    return min_ops

# --- Example Usage ---
# Sample Case 1: 3 exercises, 1 weight type
# Needs: 1, 2, 1
exercises = [[1], [2], [1]]
result = solve_recursive(0, 2, exercises)
print(f"Case #1: {result}")