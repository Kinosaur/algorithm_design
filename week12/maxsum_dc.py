# Kaung Khant Lin
# 6540131
# 542

import time

numbers = list(map(int, input().split()))

def maxCrossingSum(i, mid, k):
    sum_left = float('-inf')
    sum = 0
    
    # Include elements on the left of mid
    for j in range(mid, i - 1, -1):
        sum += numbers[j]
        sum_left = max(sum_left, sum)
    
    sum_right = float('-inf')
    sum = 0
    
    # Include elements on the right of mid
    for j in range(mid + 1, k + 1):
        sum += numbers[j]
        sum_right = max(sum_right, sum)
    
    return sum_left + sum_right

def maxSubSum(i, k):
    if i == k:
        return numbers[i]
    
    mid = (k + i) // 2
    
    left_max = maxSubSum(i, mid)
    right_max = maxSubSum(mid+1, k)
    crossing_max = maxCrossingSum(i, mid, k) # Step 6 using Step 5
    
    return max(left_max, right_max, crossing_max)

start = time.time()
result = maxSubSum(0, len(numbers) - 1)
end = time.time()

print(f"Maximum sum: {result}")
print(f"Time: {end - start:.6f} seconds")