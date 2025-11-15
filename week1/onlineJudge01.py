# Kaung Khant Lin
# 6540131
# 542

# Online Judge Problem: Hyperjump

n = int(input())

if n == 0:
    print(0)
else:
    numbers = []
    for _ in range(n):
        numbers.append(int(input()))
    
    max_sum = 0
    current_sum = 0
    
    for i in range(n):
        current_sum = max(0, current_sum + numbers[i])
        if current_sum > max_sum:
            max_sum = current_sum
    
    print(max_sum)

# Applied knowledge from Kadane's Algorithm in 1D