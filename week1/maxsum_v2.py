# Kaung Khant Lin
# 6540131
# 542

# Approach 2: Accumulation Technique
import time

numbers = list(map(int, input().split()))
n = len(numbers)

start = time.process_time()

accumlist = [0] * n
accumlist[0] = numbers[0]
for i in range(1, n):
    accumlist[i] = accumlist[i - 1] + numbers[i]

max_sum = numbers[0]

for i in range(n):
    for j in range(i, n):
        
        # Calculate sum from i to j
        if i == 0:
            current_sum = accumlist[j]
        else:
            current_sum = accumlist[j] - accumlist[i - 1]
        
        if current_sum > max_sum:
            max_sum = current_sum

finish = time.process_time()

print(max_sum)
print(f"running time: {finish - start}")

# learnt from https://youtu.be/xbYr9JOC2Lk?si=pFbJVqrB_M5pnTJx
# https://youtu.be/yuws7YK0Yng?si=uA0zjOVJNIZbFtwL