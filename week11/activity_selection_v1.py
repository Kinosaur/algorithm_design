# Kaung Khant Lin
# 6540131
# 542

# Strategy 1 - Earlist Start Time
import sys

input_data = sys.stdin.read().split()
iterator = iter(input_data)

n = int(next(iterator))
activities = []
for _ in range(n):
    s = int(next(iterator))
    f = int(next(iterator))
    activities.append((s, f)) # Store as (start, finish)
    
# Sort activities by start time
activities.sort(key=lambda x: x[0])

selected_count = 0
last_finish_time = -1

for s,f in activities:
    if s > last_finish_time:
        selected_count += 1
        last_finish_time = f
        
print(selected_count)