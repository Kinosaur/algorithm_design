import time

numbers = list(map(int, input().split()))

def maxSubSum(i, k):
    if i == k:
        return numbers[i]
    
    mid = (k + i) // 2
    
    left_max = maxSubSum(i, mid)
    right_max = maxSubSum(mid+1, k)
    # TODO: crossing_max
    
    return max(left_max, right_max)

start = time.time()
result = maxSubSum(0, len(numbers) - 1)
end = time.time()

print(f"Maximum sum: {result}")
print(f"Time: {end - start:.6f} seconds")