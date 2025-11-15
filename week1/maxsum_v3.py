# Kaung Khant Lin
# 6540131
# 542

# Approach 3: Kadane's Algorithm
import time

numbers = list(map(int, input().split()))
n = len(numbers)

start = time.process_time()

max_sum = float('-inf')
current_sum = 0

for i in range(n):
    current_sum += numbers[i]
    max_sum = max(max_sum, current_sum)
    
    if current_sum < 0:
        current_sum = 0

finish = time.process_time()

print(max_sum)
print(f"running time: {finish - start}")

# learnt from https://youtu.be/hLPkqd60-28?si=hLAhjC1qzmRsOnuV