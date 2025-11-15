# Kaung Khant Lin
# 6540131
# 542

# Online Judge Problem: Maximum Sum (2D Array)

n = int(input())

array = []
for i in range(n):
    row = list(map(int, input().split()))
    array.append(row)

max_sum = array[0][0]

for left in range(n):
    temp = [0] * n
    
    for right in range(left, n):
        for i in range(n):
            temp[i] += array[i][right]
        
        current_sum = 0
        for i in range(n):
            current_sum += temp[i]
            if current_sum > max_sum:
                max_sum = current_sum
            if current_sum < 0:
                current_sum = 0

print(max_sum)

# Applied knowledge from Kadane's Algorithm in 1D
# Learnt from https://youtu.be/-FgseNO-6Gk?si=yattqylwNopJL1kY for 2D
# Used copilot to check the algorithmagain before submission
