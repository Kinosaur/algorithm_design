# Kaung Khant Lin
# 6540131
# 542

# Approach 1: Straightforward
import time

def sum(x, i, j):
    s = 0
    for k in range(i, j + 1):
        s += x[k]
    return s

numbers = list(map(int, input().split()))

start = time.process_time()

n = len(numbers)
max_sum = numbers[0]
max_i = 0
max_j = 0

for i in range(n):
    for j in range(i, n):
        current_sum = sum(numbers, i, j)
        if current_sum > max_sum:
            max_sum = current_sum
            max_i = i
            max_j = j

finish = time.process_time()

print(max_sum)
print(f"running time: {finish - start}")

# Largest test cases can run are up to 1000.in and it is taking forever for other cases.
# O(n^3)